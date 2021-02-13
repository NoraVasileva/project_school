from Registration_functions import registration
from print_functions import print_first_menu
from Login_functions import login


def first_menu():
    """
    Menu with options for registration, login and quit.
    """
    while True:
        print_first_menu()
        choice = input("\nEnter a number from 1 to 3:\t").strip()
        while choice != "1" and choice != "2" and choice != "3":
            print("\n*** Sorry, we don't have this option. ***")
            print_first_menu()
            choice = input("\nEnter a number from 1 to 3:\t").strip()
        if choice == "3":
            break
        elif choice == "2":
            registration()
        elif choice == "1":
            login()

