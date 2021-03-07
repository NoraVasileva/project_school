import os
import csv

from print_functions import print_class_menu


def groups_admin_menu():
    while True:
        print_class_menu()
        choice = input("\nEnter a number from 1 to 5:\t").strip()
        while choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5":
            print("\n*** Try again. ***")
            choice = input("\nEnter a number from 1 to 2:\t").strip()
        if choice == "5":
            return
        elif choice == "1":
            show_groups_database_with_students()
        elif choice == "2":
            create_group()
        elif choice == "3":
            edit_group_name()
        elif choice == "4":
            delete_group()


def show_groups_database_with_students():
    """
    Display a list of study classes with option to see the information about a particular study class.
    """
    database = "groups_database.csv"
    if not os.path.exists(database):
        print(f"\n*** No study classes created yet. ***")
        return
    else:
        with open(database, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            print("\n******* LIST OF STUDY CLASSES *******")
            for row in reader:
                print(f"\n\t\t{row[0]}")
            print("\n")
            print("*" * 37)
        print("\n*** Do you want to see the list of students in a particular study class? ***")
        choice = input("\nEnter Yes or No:\t").capitalize().strip()
        while choice != "Yes" and choice != "No":
            print("\n*** We don't have this option. Try again. ***")
            choice = input("\nEnter Yes or No: ").capitalize().strip()
        if choice == "No":
            return
        else:
            new_choice = input("\nEnter study class name: ").title().strip()
            while new_choice.isspace() and new_choice.isalpha() is False:
                print("\n*** Try again. ***")
                new_choice = input("\nEnter study class name: ").title().strip()
            with open(database, "r") as file_1:
                reader = csv.reader(file_1, delimiter="\t")
                temp_list = []
                for row in reader:
                    if new_choice == row[0]:
                        temp_list.append(new_choice)
                if not temp_list:
                    print(f"\n*** {new_choice} does not exist. ***")
                    return
                else:
                    csv_name = f"{temp_list[0]}.csv"
                    group_name = new_choice.upper()
                    with open(csv_name, "r") as file_2:
                        reader_1 = csv.reader(file_2, delimiter="\t")
                        a = f"\n************** LIST OF {group_name} **************"
                        print(a)
                        for row_1 in reader_1:
                            print(f"\n\t\t{row_1[0]} {row_1[1]} {row_1[2]}")
                        print("\n", "*" * len(a))


def create_group():
    print("\n*** Creating new study class ***")
    name = input("\nEnter class name:\t").strip().title()
    while name == "":
        name = input("\nEnter class name again:\t").strip().title()
    find_group(name)


def edit_group_name():
    database = "groups_database.csv"
    print("\n*** Edit study class name ***")
    show_only_groups()
    name = input("\nWhich study class name do you want to edit?:\t").strip().title()
    name_csv = f"{name}.csv"
    groups = []
    if os.path.exists(name_csv):
        new_name = input("\nEnter new study class name:\t").strip().title()
        while new_name == "":
            new_name = input("\nEnter new study class name:\t").strip().title()
        new_name_csv = f"{new_name}.csv"
        os.rename(name_csv, new_name_csv)
        with open(database, "r") as f:

            reader = f.readlines()
            for row in reader:
                new_var = row.replace('\n', '')
                groups.append(new_var)
        groups.remove(name)
        groups.append(new_name)
        with open(database, "w") as file:
            list_of_groups = []
            for gr in range(len(groups)):
                list_of_groups.append(groups[gr]+"\n")
            file.writelines(list_of_groups)
        print(f"\n*** {name} was successfully edited to {new_name}. ***")
    else:
        print(f"\n*** Study class '{name}' does not exists. ***")
        return


def delete_group():
    database = "groups_database.csv"
    print("\n*** Delete study class ***")
    show_only_groups()
    name = input("\nWhich study class do you want to delete?:\t").strip().title()
    while name == '':
        print("\n*** Try again. ***")
        name = input("\nWhich study class do you want to delete?:\t").strip().title()
    name_csv = f"{name}.csv"
    if not os.path.exists(name_csv):
        print(f"*** {name} do not exists. ****")
        return
    else:
        print("\n*** Do you want to transfer the information from the deleted file to another file? ***")
        choice = input("\nEnter Yes or No:\t").strip().capitalize()
        while choice != "Yes" and choice != "No":
            print("\n*** Try again. ***")
            choice = input("\nEnter Yes or No:\t").strip().capitalize()
    if choice == "No":
        os.remove(name_csv)
        print(f"\n*** {name} was deleted successfully. ***")
    else:
        new_name = input("\nEnter the name of the file to which you want to transfer the information:\t").strip().title()
        while new_name == "":
            print("\n*** Try again. ***")
            new_name = input("\nEnter the name of the file to which you want to transfer the information:\t").strip().title()
        new_name_csv = f"{new_name}.csv"
        if not os.path.exists(f"{new_name_csv}"):
            print(f"*** {new_name} do not exists. ****")
            return
        else:
            temp_list = []
            with open(name_csv, "r") as file:
                reader = csv.reader(file, delimiter="\t")
                for row in reader:
                    if row[0] == "First name":
                        pass
                    else:
                        temp_list.append(row)
            with open(new_name_csv, "a") as f:
                writer = csv.writer(f, delimiter="\t")
                for user in temp_list:
                    writer.writerow(user)
            os.remove(name_csv)
            print(f"\n*** {name} was deleted successfully. ***")
            print(f"\n*** The information was successfully moved to {new_name}. ***")
            with open(database, "r") as f:
                groups = []
                reader = f.readlines()
                for row in reader:
                    new_var = row.replace('\n', '')
                    groups.append(new_var)
            groups.remove(name)
            with open(database, "w") as file:
                list_of_groups = []
                for gr in range(len(groups)):
                    list_of_groups.append(groups[gr] + "\n")
                file.writelines(list_of_groups)


def os_path_exists_group(group):
    """
    Check if the group exists in the database.
    :param group: the name of the group
    :return: Boolean
    """
    find_groups = False
    with open("groups_database.csv", "r") as file:
        list_groups = file.readlines()
        for row in list_groups:
            if group in row:
                find_groups = True
    return find_groups


def os_path_does_not_exists_group(group):
    """
    Add a new group to the database.
    :param group: the name of the group
    """
    with open("groups_database.csv", "a") as file:
        # TODO: да попитам Милена, защо ми дава грешка на закоментирания ред
        # writer = csv.writer(file, newline="")
        writer = csv.writer(file, delimiter="\t")
        writer.writerow([group])
        print(f"\n*** The {group} was created successfully. ***")


def show_only_groups():
    """
    Display groups in the database.
    """
    if not os.path.exists("groups_database.csv"):
        print(f"\n*** No study classes created yet. ***")
    elif os.path.exists("groups_database.csv"):
        with open("groups_database.csv", "r") as file:
            reader = csv.reader(file, delimiter="\t")
            print("\n******* LIST OF STUDY CLASSES *******")
            print("\n")
            for row in reader:
                len_row = len(row)
                for row_1 in range(len_row):
                    print("\t\t\t", row[row_1], end="")
                    print('\n')
            print("\n")
            print("*" * 37)


def find_group(group):
    """
    Check if the group exists in the database. If the group does not exist, it is entered in the database.
    :param group: the name of the group
    """
    if not os.path.exists("groups_database.csv"):
        os_path_does_not_exists_group(group)
    elif os_path_exists_group(group) is False:
        os_path_does_not_exists_group(group)
    else:
        print(f"\n*** The {group} already exists. ***")


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
            return
        else:
            show_groups_database_with_students()
