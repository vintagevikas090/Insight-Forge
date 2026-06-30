from app.llm.config import MODEL_PROVIDER, MODELS, GROQ_API_KEY, GOOGLE_API_KEY, NVIDIA_API_KEY


def get_llm(temperature=0):
    if MODEL_PROVIDER == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(model=MODELS["groq"], api_key=GROQ_API_KEY, temperature=temperature)

    if MODEL_PROVIDER == "gemini":
        from langchain_google_genai import ChatGoogleGenerativeAI
        return ChatGoogleGenerativeAI(model=MODELS["gemini"], google_api_key=GOOGLE_API_KEY, temperature=temperature)

    if MODEL_PROVIDER == "nvidia":
        from langchain_nvidia_ai_endpoints import ChatNVIDIA
        return ChatNVIDIA(model=MODELS["nvidia"], api_key=NVIDIA_API_KEY, temperature=temperature, timeout=300)

    raise ValueError(f"Unsupported provider: {MODEL_PROVIDER}")