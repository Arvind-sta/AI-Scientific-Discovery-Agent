from scipy.stats import pearsonr
import pandas as pd

def correlation_test(df: pd.DataFrame, col1: str, col2: str):
    clean_df = df[[col1, col2]].dropna()
    corr, p_value = pearsonr(clean_df[col1], clean_df[col2])

    return {
        "correlation": corr,
        "p_value": p_value,
        "significant": p_value < 0.05
    }
