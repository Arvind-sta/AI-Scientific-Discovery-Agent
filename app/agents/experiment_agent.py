from app.core.statistics import correlation_test

def run_experiment(df, col1, col2):
    result = correlation_test(df, col1, col2)
    return result
