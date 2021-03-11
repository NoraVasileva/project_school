from Function_first_menu import first_menu
from Login_functions import login
from Registration_functions import registration

if __name__ == '__main__':
    while True:
        first_menu()
        choice = input("Enter a number from 1 to 3:\t").strip()
        print("")
        while choice != "1" and choice != "2" and choice != "3":
            print("*** Sorry, we don't have this option. ***")
            print("")
            first_menu()
            choice = input("Enter a number from 1 to 3:\t").strip()
            print("")
        if choice == "1":
            print("")
            login()
        elif choice == "2":
            print("")
            registration()
        elif choice == "3":
            print("*** Thank you for visiting our site. Have a nice day! ***")
            break
