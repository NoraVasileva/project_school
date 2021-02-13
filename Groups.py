from Class_School import School
import os


def create_group():
    print("\n*** Creating new study class ***")
    name = input("\nEnter class name: ").strip().title()
    while name == "":
        name = input("\nEnter class name again: ").strip().title()
    find = School()
    find.find_group(name)


def edit_group_name():
    print("\n*** Edit study class name")
    group = School()
    group.show_only_groups()
    name = input("\nWhich study class name do you want to edit?:\t").strip().title()
    name_csv = f"{name}.csv"
    if os.path.exists(name_csv):
        new_name = input("\nEnter new study class name:\t").strip().title()
        while new_name == "":
            new_name = input("\nEnter new study class name:\t").strip().title()
        new_name_csv = f"{new_name}.csv"
        os.rename(name_csv, new_name_csv)
        group.delete_group_name(name, new_name)


def delete_group():
    print("\n*** Delete study class ***")
    group = School()
    group.show_only_groups()
    name = input("\nWhich study class do you want to delete?:\t").strip().title()
    name_csv = f"{name}.csv"
    if not os.path.exists(name_csv):
        print("*** This study class do not exists. ****")
    else:
        group.delete_group(name, name_csv)


def groups_admin_menu():
    while True:
        print("\n*********** INFORMATION ABOUT STUDY CLASSES *********"
              "\n"
              "\nChoose a number from 1 to 5 from the below options:"
              "\n"
              "\n# 1: Show all study classes\n\n# 2: Create new study class\n\n# 3: Edit study class name"
              "\n\n# 4: Delete study class\n\n# 5: Quit"
              "\n*****************************************************")
        choice = input("\nEnter a number from 1 to 5:\t").strip()
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("\n*** Sorry, we don't have this option. ***")
            print("\n*********** INFORMATION ABOUT STUDY CLASSES *********"
                  "\n"
                  "\nChoose a number from 1 to 2 from the below options:"
                  "\n"
                  "\n# 1: Show all study classes\n\n# 2: Create new study class\n\n# 3: Edit study class name"
                  "\n\n# 4: Delete study class\n\n# 5: Quit"
                  "\n*****************************************************")
            choice = input("\nEnter a number from 1 to 2:\t").strip()
        if choice == "5":
            break
        elif choice == "1":
            group = School()
            group.show_groups_database_with_students()
        elif choice == "2":
            create_group()
        elif choice == "3":
            edit_group_name()
        elif choice == "4":
            delete_group()


def groups_teachers_menu():
    while True:
        print("\n*********** INFORMATION ABOUT STUDY CLASSES *********"
              "\n"
              "\nChoose a number from 1 to 2 from the below options:"
              "\n"
              "\n# 1: Show all study classes\n\n# 2: Quit"
              "\n*****************************************************")
        choice = input("\nEnter a number from 1 to 2:\t").strip()
        while choice != "1" and choice != "2":
            print("\n*** Sorry, we don't have this option. ***")
            print("\n*********** INFORMATION ABOUT STUDY CLASSES *********"
                  "\n"
                  "\nChoose a number from 1 to 2 from the below options:"
                  "\n"
                  "\n# 1: Show all study classes\n\n# 2: Quit"
                  "\n*****************************************************")
            choice = input("\nEnter a number from 1 to 2:\t").strip()
        if choice == "2":
            break
        else:
            group = School()
            group.show_groups_database_with_students()
