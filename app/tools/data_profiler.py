import pandas as pd


def get_dataset_summary(df: pd.DataFrame):
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": int(df.duplicated().sum())
    }


def get_sample_data(df: pd.DataFrame, n=5):
    return df.head(n).to_dict(orient="records")


def profile_dataset(df):
    return {
        "summary": get_dataset_summary(df),
        "llm_context": get_llm_context(df)
    }

def get_llm_context(df):
    return {
        "columns": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "sample_rows": df.head(3).to_dict("records")
    }