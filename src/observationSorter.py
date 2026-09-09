import pandas as pd

# Load the CSV file into a pandas DataFrame
def load_df(filename):
    df = pd.read_csv(filename)
    return df

# Group by operator and count the occurrences. Display in descending order of total observations.
def count_observations(df):
    total_observations = df.groupby('operator').size().reset_index(name='total_observations')
    total_observations = total_observations.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return total_observations

# Group by cause code and count the occurrences. Display in descending order of total observations.
def count_cause_codes(df):
    cause_code_counts = df.groupby('category').size().reset_index(name='total_observations')
    cause_code_counts = cause_code_counts.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return cause_code_counts

# Filter the DataFrame by the specified date
def count_cause_codes_by_date(df, date):

    filtered_df = df[df['date'] == date]
    cause_code_counts = filtered_df.groupby('category').size().reset_index(name='total_observations')
    cause_code_counts = cause_code_counts.sort_values(by='total_observations', ascending=False).reset_index(drop=True)
    return cause_code_counts

# Group by operator and category, then count the occurrences
def generate_most_common_operator_defect(df):
    # Filter for defects only
    defect_df = df[df['proc_ind'] == False]  
    # Group by each operator, category pair and count the occurrences
    counts_df = defect_df.groupby(['operator', 'category']).size().reset_index(name='total_observations')
    # Sort counts by descending order of total observations for each operator
    sorted_counts_df = counts_df.sort_values(by=['operator', 'total_observations'], ascending=[True, False])
    # Drop duplicates to keep only the highest count for each operator
    highest_counts_df = sorted_counts_df.drop_duplicates(subset=['operator'], keep='first').reset_index(drop=True)
    return highest_counts_df

# Write a DataFrame to a CSV file
def write_to_csv(df, filename):
    df.to_csv(filename, index=False)
    print(f"Data written to {filename}")