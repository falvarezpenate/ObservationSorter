import pandas as pd

def load_df(filename):
    df = pd.read_csv(filename)
    return df
