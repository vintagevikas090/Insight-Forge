from app.llm.models import get_llm
from app.schema.prompt_templates import INSIGHT_PROMPT

import pandas as pd


llm = get_llm(temperature=0.3)


def insight_gen_agent(state):
    question = state["question"]
    result = state["execution_result"]

    if isinstance(result, pd.DataFrame):
        data = result.head(20).to_string()
    else:
        data = str(result)

    prompt = INSIGHT_PROMPT.format(
        question=question,
        result=data
    )

    response = llm.invoke(prompt)

    return {"insight": response.content}