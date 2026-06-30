import pandas as pd


def load_data(file):
    if file.name.endswith(".csv"):
        try:
            return pd.read_csv(file)
        except UnicodeDecodeError:
            file.seek(0)

            try:
                return pd.read_csv(file, encoding="latin1")
            except UnicodeDecodeError:
                file.seek(0)
                return pd.read_csv(file, encoding="cp1252")

    if file.name.endswith((".xlsx", ".xls")):
        return pd.read_excel(file)

    raise ValueError("Unsupported file format")