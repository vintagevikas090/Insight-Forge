from app.llm.models import get_llm
from app.schema.prompt_templates import PLANNER_PROMPT
from app.schema.output_models import AnalysisPlan


llm = get_llm().with_structured_output(AnalysisPlan)


def planner_agent(state):
    question = state["question"]
    profile = state["dataset_profile"]["llm_context"]

    prompt = PLANNER_PROMPT.format(profile=profile,question=question)
    response = llm.invoke(prompt)

    return {"analysis_plan": response.model_dump()}