from pydantic import BaseModel

class AnalysisPlan(BaseModel):
    analysis_type: str
    steps: list[str]
    chart_type: str

class ChartConfig(BaseModel):
    chart_type: str
    x: str
    y: str
    title: str