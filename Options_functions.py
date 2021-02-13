from Class_School import School
from print_functions import print_teacher_options, print_admin_options, print_users_management, \
    print_registrations, print_user_options, print_user_accounts, print_show_users


def teacher_options():
    while True:
        print_teacher_options()
        choice = input("\nEnter a number from 1 to 3:\t").strip()
        while choice != "1" and choice != "2" and choice != "3":
            print_teacher_options()
            choice = input("\nEnter a number from 1 to 3:\t").strip()
        if choice == "3":
            break
        elif choice == "2":
            teacher = School()
            teacher.show_teachers_database()
        else:
            teacher = School()
            teacher.show_groups_database_with_students()


def admin_options():
# TODO: да се поправи цикълът, защото не ме връща на предишните менюта като натиксам quit

# TODO: да се довършат всички опции
    while True:
        print_admin_options()
        choice = input("\nEnter a number from 1 to 4:\t").strip()
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print_admin_options()
            choice = input("\nEnter a number from 1 to 4:\t").strip()
        if choice == "1":
            admin_options_1()
        else:
            return


def admin_options_1():
    print_users_management()
    choice_1 = input("\nEnter a number from 1 to 3:\t")
    while choice_1 != "1" and choice_1 != "2" and choice_1 != "3":
        print_users_management()
        choice_1 = input("\nEnter a number from 1 to 3:\t")
    if choice_1 == "1":
        admin_option_2()
    elif choice_1 == "2":
        admin_options_3()
    else:
        return


def admin_option_2():
    print_registrations()
    choice_2 = input("\nEnter a number from 1 to 3:\t")
    while choice_2 != "1" and choice_2 != "2" and choice_2 != "3":
        print_registrations()
        choice_2 = input("\nEnter a number from 1 to 3:\t")
    if choice_2 == "1":
        student = School()
        student.show_students_database_for_approval()
    elif choice_2 == "2":
        teacher = School()
        teacher.show_teachers_database_for_approval()
    else:
        return


def admin_options_3():
    print_user_accounts()
    choice_3 = input("\nEnter a number from 1 to 4:\t")
    while choice_3 != "1" and choice_3 != "2" and choice_3 != "3" and choice_3 != "4":
        print("\n*** Try again. ***")
        choice_3 = input("\nEnter a number from 1 to 4:\t")
    if choice_3 == "1":
        admin_options_4()
    elif choice_3 == "2":
        admin = School()
        admin.edit_user()
    elif choice_3 == "3":
# TODO: да се довърши
        pass
    else:
        return


def admin_options_4():
    print_show_users()
    choice_4 = input("\nEnter a number from 1 to 4:\t")
    while choice_4 != "1" and choice_4 != "2" and choice_4 != "3" and choice_4 != "4":
        print("\n*** Try again. ***")
        choice_4 = input("\nEnter a number from 1 to 4:\t")
    if choice_4 == "1":
        users = School()
        users.show_users_database()
    elif choice_4 == "2":
        users = School()
        users.show_students_database()
    elif choice_4 == "3":
        users = School()
        users.show_teachers_database()
    else:
        return


def user_options():
    while True:
        print_user_options()
        choice = input("\nEnter a number from 1 to 2:\t").strip()
        while choice != "1" and choice != "2":
            print_user_options()
            choice = input("\nEnter a number from 1 to 2:\t").strip()
        if choice == "2":
            return
        else:
            user = School()
            user.show_teachers_database()
