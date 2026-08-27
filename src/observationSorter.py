import pandas as pd

def load_df(filename):
    df = pd.read_csv(filename)
    return df

def count_observations(df):
    total_observations = df.groupby('operator').size().reset_index(name='total_observations')
    total_observations = total_observations.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return total_observations
