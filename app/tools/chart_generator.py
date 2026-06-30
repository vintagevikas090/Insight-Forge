import plotly.express as px
import pandas as pd


def generate_chart(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        return None

    df = df.copy()

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    non_numeric_cols = [c for c in df.columns if c not in numeric_cols]

    try:
        # Single value -> Indicator Bar
        if len(df.columns) == 1:
            col = df.columns[0]

            df["Category"] = [col] * len(df)
            return px.bar(df, x="Category", y=col, title=col)

        # One categorical + one numeric -> Bar Chart
        if len(non_numeric_cols) >= 1 and len(numeric_cols) >= 1:
            return px.bar(df, x=non_numeric_cols[0], y=numeric_cols[0],
                title=f"{numeric_cols[0]} by {non_numeric_cols[0]}"
            )

        # Two numeric columns -> Scatter Plot
        if len(numeric_cols) >= 2:
            return px.scatter(df, x=numeric_cols[0], y=numeric_cols[1],
                title=f"{numeric_cols[1]} vs {numeric_cols[0]}"
            )

        # One numeric column -> Histogram
        if len(numeric_cols) == 1:
            return px.histogram(df, x=numeric_cols[0],
                title=f"Distribution of {numeric_cols[0]}"
            )

    except Exception as e:
        print(e)
        return None

    return None


