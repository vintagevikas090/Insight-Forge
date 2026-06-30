from typing import Any
from typing_extensions import TypedDict
import pandas as pd


class GraphState(TypedDict):
    question: str
    df: pd.DataFrame

    dataset_profile: dict
    analysis_plan: dict

    generated_code: str
    execution_result: Any

    chart_config: dict
    insight: str

    final_response: dict