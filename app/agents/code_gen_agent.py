from app.llm.models import get_llm
from app.schema.prompt_templates import CODE_GEN_PROMPT


llm = get_llm()


def clean_code(code):
    code = code.strip()

    if code.startswith("```python"):
        code = code.replace("```python", "", 1)

    if code.endswith("```"):
        code = code[:-3]

    return code.strip()


def code_gen_agent(state):
    question = state["question"]
    plan = state["analysis_plan"]
    profile = state["dataset_profile"]["llm_context"]

    prompt = CODE_GEN_PROMPT.format(
        profile=profile,
        plan=plan,
        question=question
    )

    response = llm.invoke(prompt)
    code = clean_code(response.content)

    return {"generated_code": code}