import pandas as pd

def load_df(filename):
    df = pd.read_csv(filename)
    return df

def count_observations(df):
    total_observations = df.groupby('operator').size().reset_index(name='total_observations')
    total_observations = total_observations.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return total_observations

def count_cause_codes(df):
    cause_code_counts = df.groupby('category').size().reset_index(name='total_observations')
    cause_code_counts = cause_code_counts.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return cause_code_counts

def count_cause_codes_by_date(df, date):
    # Filter the DataFrame by the specified date
    filtered_df = df[df['date'] == date]
    cause_code_counts = filtered_df.groupby('category').size().reset_index(name='total_observations')
    cause_code_counts = cause_code_counts.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return cause_code_counts