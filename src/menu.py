import pandas as pd

from .observationSorter import load_df
from .observationSorter import create_operator_statistics

def show_menu():
    print("Menu:")
    print("1. Open Observation File")
    print("2. View Data")
    print("3. Write Operator Specific Statistics (as .csv)")
    print("4. Exit")

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
    sorted_operator_stats = create_operator_statistics(df)
    return sorted_operator_stats


