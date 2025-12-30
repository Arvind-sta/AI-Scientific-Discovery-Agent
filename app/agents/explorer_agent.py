import pandas as pd

def explore_data(df: pd.DataFrame) -> dict:
    summary = {
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "missing_values": df.isnull().sum().to_dict(),
        "numeric_summary": df.describe().to_dict()
    }

    corr_series = (
        df.select_dtypes(include="number")
          .corr()
          .abs()
          .unstack()
          .sort_values(ascending=False)
    )

    top_correlations = []
    for (col1, col2), value in corr_series.items():
        if col1 != col2:
            top_correlations.append({
                "feature_1": col1,
                "feature_2": col2,
                "correlation": float(round(value, 4))
            })
        if len(top_correlations) == 5:
            break

    return {
        "summary": summary,
        "top_correlations": top_correlations
    }
