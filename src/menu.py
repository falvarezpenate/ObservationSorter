import os
import pandas as pd
from .observationSorter import load_df, count_observations, count_cause_codes, count_cause_codes_by_date, generate_most_common_operator_defect, write_to_csv


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

        
# Prints the menu options to the console
def show_menu():
    print("Menu:")
    print("1. Open Observation File")
    print("2. View Data")
    print("3. Count Total Observations by Operator")
    print("4. Find Most Common Cause Code")
    print("5. Find Most Common Cause Code by Operator")
    print("6. Exit")

# Opens the observation file and returns the DataFrame
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

# Calls helper function to count total observations by operator and returns the sorted DataFrame
def write_operator_statistics(df):
    sorted_operator_stats = count_observations(df)
    return sorted_operator_stats

# Calls helper function to count cause codes and returns the sorted DataFrame
def write_cause_code_statistics(df):
    date = input("Enter a date (mm/dd/yyyy) to filter the cause codes (or press Enter to display all): ")
    if date:
        # Split the date string into tokens
        date_tokens = date.split('/')
        # Check that date entered is valid.
        if len(date_tokens) != 3 or not all(token.isdigit() for token in date_tokens):
            print("Invalid date format. Please use mm/dd/yyyy.")
            return None

        sorted_cause_code_stats = count_cause_codes_by_date(df, date)
        # Check if the filtered DataFrame is empty
        if sorted_cause_code_stats.empty:
            print(f"\nNo cause codes found for the date {date}.")
            return None
    else:
        sorted_cause_code_stats = count_cause_codes(df)
    return sorted_cause_code_stats

# Calls helper function to find the most common cause code by operator and returns the DataFrame
def write_most_common_operator_defect(df):
    most_common_defects = generate_most_common_operator_defect(df)
    return most_common_defects

def save_output(df, default_filename):
    res = input("Do you want to save the output to a CSV file? (y/n): ")
    if res.lower() == 'y':
        filename = input(f"Enter the filename to save the output (default: {default_filename}): ")
        if not filename:
            filename = default_filename
        write_to_csv(df, "output/" + filename)
