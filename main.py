
import sys

from src.menu import show_menu
from src.menu import open_observation_file
from src.menu import write_operator_statistics

def clear_screen():
    sys.stdout.write('\033[2J\033[H')
    sys.stdout.flush()

def main():
    while True:
        clear_screen()
        show_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            df = open_observation_file()
        elif choice == "2":
            if 'df' in locals():
                print("\n\nData Preview:")
                print(df)
            else:
                print("Please open an observation file first.")
        elif choice == "3":
            if 'df' in locals():
                clear_screen()
                write_operator_statistics(df)
            else:
                print("Please open an observation file first.")
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

        input("\nPress Enter to return to the menu...")

main()