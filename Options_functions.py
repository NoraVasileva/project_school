import csv
import os
import matplotlib.pyplot as plt
import datetime

from Class_School import School
from Groups import show_groups_database_with_students, groups_admin_menu
from Registration_functions import check_email
from print_functions import print_teacher_options, print_admin_options, print_users_management, \
    print_registrations, print_user_options, print_user_accounts, print_show_users, print_delete_account, \
    school_information


def teacher_options():
    """

    """
    while True:
        print_teacher_options()
        choice = input("\nEnter a number from 1 to 3:\t").strip()
        while choice != "1" and choice != "2" and choice != "3":
            print_teacher_options()
            choice = input("\nEnter a number from 1 to 3:\t").strip()
        if choice == "3":
            return
        elif choice == "2":
            teacher = School()
            teacher.show_teachers_database()
        else:
            show_groups_database_with_students()


def admin_options():
# TODO: да се поправи цикълът, защото не ме връща на предишните менюта като натиксам quit
    while True:
        print_admin_options()
        choice = input("\nEnter a number from 1 to 4:\t").strip()
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print_admin_options()
            choice = input("\nEnter a number from 1 to 4:\t").strip()
        if choice == "1":
            admin_options_1()
        elif choice == "2":
            groups_admin_menu()
        elif choice == "3":
            admin_options_5()
        elif choice == "4":
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
        student.show_students_or_teachers_database_for_approval("students_database_for_approval.csv", "student")
    elif choice_2 == "2":
        teacher = School()
        teacher.show_students_or_teachers_database_for_approval("teachers_database_for_approval.csv", "teacher")
    else:
        return


def admin_options_3():
    admin = School()
    print_user_accounts()
    students_database = "students_database.csv"
    teachers_database = "teachers_database.csv"
    users_database = "users_database.csv"
    choice_3 = input("\nEnter a number from 1 to 4:\t")
    while choice_3 != "1" and choice_3 != "2" and choice_3 != "3" and choice_3 != "4":
        print("\n*** Try again. ***")
        choice_3 = input("\nEnter a number from 1 to 4:\t")
    if choice_3 == "1":
        admin_options_4()
    elif choice_3 == "2":
        database, email = admin.edit_user()
        if database == students_database:
            admin.edit_student_or_user(students_database, "student", email)
        elif database == users_database:
            admin.edit_student_or_user(users_database, "user", email)
        elif database == teachers_database:
            admin.edit_teacher(teachers_database, email)
        else:
            print("\n*** Something went wrong. ***")
    elif choice_3 == "3":
        admin = School()
        print_delete_account()
        choice = input("\nEnter a number from 1 to 4:\t")
        if choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("\n*** Try again. ***")
            choice = input("\nEnter a number from 1 to 4:\t")
        if choice == "4":
            return
        elif choice == "1":
            admin.show_students_database()
            email = input("\nEnter student's e-mail addrres:\t")
            while check_email(email):
                print("\n*** Try again. ***")
                email = input("\nEnter student's e-mail addrres:\t")
            admin.delete_account(email, "student")
        elif choice == "2":
            admin.show_teachers_database()
            email = input("\nEnter teacher's e-mail addrres:\t")
            while check_email(email):
                print("\n*** Try again. ***")
                email = input("\nEnter teacher's e-mail addrres:\t")
            admin.delete_account(email, "teacher")
        elif choice == "3":
            admin.show_users_database()
            email = input("\nEnter user's e-mail addrres:\t")
            while check_email(email):
                print("\n*** Try again. ***")
                email = input("\nEnter user's e-mail addrres:\t")
            admin.delete_account(email, "user")
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

# TODO: да се довърши
def admin_options_5():
    school_information()
    choice = input("\nEnter a number from 1 to 3:\t")
    while choice != "1" and choice != "2" and choice != "3":
        print("\n*** Try again. ***")
        choice = input("\nEnter a number from 1 to 3:\t")
    if choice == "1":
        database = "groups_database.csv"
        if not os.path.exists(database):
            print(f"\n*** No study classes created yet. ***")
            return
        else:
            group_names = [] # това трябва да ми е х (от долу)
            number_of_students = [] # това трябва да ми е у (от ляво)
            with open(database, "r") as file:
                reader = csv.reader(file, delimiter="\t")
                for group in reader:
                    new_name = str(group)[2:-2]
                    group_names.append(new_name)
            for groups in range(len(group_names)):
                count = 0
                with open(f"{group_names[groups]}.csv", "r") as file:
                    reader = csv.reader(file, delimiter="\t")
                    for row in reader:
                        count += 1
                number_of_students.append(count - 1)
            plt.title("Number of students by groups")
            plt.xlabel("Groups")
            plt.ylabel("Number of students")
            plt.bar(group_names, number_of_students)
            plt.show()
    elif choice == "2":
        database = "teachers_database.csv"
        if not os.path.exists(database):
            print(f"\n*** No teacher's registrations created yet. ***")
            return
        else:
            # TODO: да редактирам слайсинга - вместо него да използвам datetime обект, който да е с точки и да изваждам от него.
            teachers_age = []
            years_of_experience = []
            age_and_experience_y = []
            date_now = datetime.datetime.now()
            year = date_now.strftime("%Y")
            with open(database, "r") as file:
                reader = csv.reader(file, delimiter="\t")
                for teacher in reader:
                    if teacher[5] == "Birth" and teacher[6] == "Work":
                        pass
                    else:
                        age = teacher[5][-4:]
                        age_result = int(year) - int(age)
                        teachers_age.append(age_result)
                        experience = teacher[6][-4:]
                        experience_result = int(year) - int(experience)
                        years_of_experience.append(experience_result)
            for age, experience in zip(teachers_age, years_of_experience):
                age_and_experience_y.append(age)
                age_and_experience_y.append(experience)
            teacher_info_x = []
            for num in range(1, int((len(age_and_experience_y) + 2) / 2)):
                teacher_info_x.append(f"age {num}")
                teacher_info_x.append(f"experience {num}")
            plt.title("Teacher's age and experience")
            plt.xlabel("Teacher's age and experience")
            plt.ylabel("Age, Experience")
            plt.bar(teacher_info_x, age_and_experience_y, color=["blue", "orange"] * int(len(age_and_experience_y) / 2))
            plt.show()
    elif choice == "3":
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
