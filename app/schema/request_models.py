from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str


class QuestionResponse(BaseModel):
    insight: str
    chart_config: dict | None
    data: list[dict]