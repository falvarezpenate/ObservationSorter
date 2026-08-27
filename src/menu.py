import pandas as pd

from .observationSorter import load_df
from .observationSorter import total_observations

def show_menu():
    print("Menu:")
    print("1. Open Observation File")
    print("2. View Data")
    print("3. Count Total Observations by Operator")
    print("4. Find Most Common Cause Code")
    print("5. Exit")

def open_observation_file():
    filename = input("Enter the path to the observation file: ")
    if filename == "":
        print("No file path provided. Please try again. Returning to menu...")
        return None
    else:
        try:
            df = load_df(filename)
            if df.empty:
                print("The observation file is empty.")
            else:
                print("Observation file opened successfully.")
            return df
        except FileNotFoundError:
            print(f"File not found: '{filename}'. Please check the path and try again.")
            return None
        except pd.errors.EmptyDataError:
            print(f"The file '{filename}' is empty. Please provide a valid observation file.")
            return None
        except Exception as e:
            print(f"An error occurred while opening the file: {e}")
            return None

def write_operator_statistics(df):
    sorted_operator_stats = total_observations(df)
    return sorted_operator_stats


