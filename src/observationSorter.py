import pandas as pd

def load_df(filename):
    df = pd.read_csv(filename)
    return df

def group_by_operator(df):
    operator_stats = df.groupby('Operator').count()
    sorted_stats = operator_stats.sort_values(by='Observation', ascending=False)
    return sorted_stats


