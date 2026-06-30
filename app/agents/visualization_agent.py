from app.llm.models import get_llm
from app.schema.output_models import ChartConfig
from app.schema.prompt_templates import VISUALIZATION_PROMPT

import pandas as pd


llm = get_llm().with_structured_output(ChartConfig)


def visualization_agent(state):
    result = state["execution_result"]

    if not isinstance(result, pd.DataFrame):
        return {"chart_config": None}

    question = state["question"]
    plan = state["analysis_plan"]

    prompt = VISUALIZATION_PROMPT.format(
        question=question,
        plan=plan,
        columns=list(result.columns)
    )

    response = llm.invoke(prompt)

    return {"chart_config": response.model_dump()}