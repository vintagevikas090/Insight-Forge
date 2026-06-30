from io import BytesIO
import pandas as pd
from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from app.services.analyst_service import analyst_service

router = APIRouter(prefix="/api", tags=["Analyst"])


@router.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    question: str = Form(...)
):
    try:
        content = await file.read()

        if file.filename.endswith(".csv"):
            df = pd.read_csv(BytesIO(content))

        elif file.filename.endswith((".xlsx", ".xls")):
            df = pd.read_excel(BytesIO(content))

        else:
            raise HTTPException(400, "Unsupported file format")

        response = analyst_service.analyze(df, question)

        return {
            "data": response["data"],
            "chart_config": response["chart_config"],
            "insight": response["insight"]
        }

    except Exception as e:
        raise HTTPException(500, str(e))