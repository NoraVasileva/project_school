from Project_2_test.Login.Options_functions import admin_options, user_options, teacher_options
from Project_2_test.Print.print_functions import print_login
import os
import csv

from Project_2_test.Registration.Registration_functions import check_email


def login():
    """
    Login form with options for students, teachers and administrator.
    """
    while True:
        print_login()
        role = input("\nPlease enter a number from 1 to 4:\t").strip()
        while role != "1" and role != "2" and role != "3" and role != "4":
            print("\n*** Sorry, we don't have this option. ***")
            print_login()
            role = input("\nPlease enter a number from 1 to 4:\t").strip()
        if role == "1":
            student_login()
        elif role == "2":
            teacher_login()
        elif role == "3":
            admin_login()
        else:
            return


def student_login():
    """
    Login form for students. Entering email address and password.
    If the student's email and password are in the databases, it will be possible to login.
    """
    pr = "\n************** LOGIN FORM FOR STUDENTS **************"
    print("\n*** Hello, please fill in your information ***")
    email = input("\nEnter your e-mail address:\t").strip()
    while check_email(email):
        print("\n*** This e-mail address is not recognized. ***")
        email = input("\nEnter another e-mail address:\t").strip()
    password = input("\nEnter a password (enter at least six characters):\t").strip()
    while check_password:
        print("\n*** Your password is incorrect. Try again. ***")
        password = input("\nEnter a password (enter at least six characters):\t").strip()
    print("*" * len(pr))
    check_database_for_approval = check_login_user("students_database_for_approval.csv", email, password, string_name="user")
    check_users_database = check_login_user("users_database.csv", email, password, string_name="user")
    check_students_database = check_login_user("students_database.csv", email, password, string_name="user")

    if check_database_for_approval is False and check_users_database is False and check_students_database is False:
        print("\n*** Login failed! You must have a registration to login. ***")


def teacher_login():
    """
    Login form for teachers. Entering email address and password.
    If the teacher's email and password are in the databases, it will be possible to login.
    """
    pr = "\n************** LOGIN FORM FOR TEACHERS **************"
    print("\n*** Hello, please fill in your information ***")
    email = input("\nEnter your e-mail address:\t").strip()
    while check_email(email):
        print("\n*** This e-mail address is not recognized. ***")
        email = input("\nEnter another e-mail address:\t").strip()
    password = input("\nEnter a password (enter at least six characters):\t").strip()
    while check_password(password):
        print("\n*** Your password is incorrect. Try again. ***")
        password= input("\nEnter a password (enter at least six characters):\t").strip()
    print("*" * len(pr))

    check_database_for_approval = check_login_user("teachers_database_for_approval.csv", email, password, string_name="user")
    check_teachers_database = check_login_user("teachers_database.csv", email, password, string_name="teacher")
    check_users_database = check_login_user("users_database.csv", email, password, string_name="user")

    if check_database_for_approval is False and check_teachers_database is False and check_users_database is False:
        print("\n*** Login failed! You must have a registration to login. ***")


def admin_login():
    """
    Login form for administrator. Entering email address, password and special password.
    If the administrator's email and passwords are correct, it will be possible to login.
    """
    print("\n*** Hello, please fill in your information ***")
    email = input("\nEnter your e-mail address:\t").strip()
    while email != "admin@pythonschool.com":
        print("\n*** Enter your e-mail address again. ***")
        email = input("\nEnter your e-mail address:\t").strip()
    password_1 = input("\nEnter a password:\t").strip()
    while password_1 != "adminpassword":
        print("\n*** Your password is incorrect. Try again. ***")
        password_1 = input("\nEnter a password:\t").strip()
    admin_password = input("\nEnter your administrator password:\t").strip()
    while admin_password != "*123*":
        print("\n*** Your administrator password is incorrect. Try again. ***")
        admin_password = input("\nEnter your administrator password again:\t").strip()
    admin_options()


def check_login_user(csv_file_name, email, password, string_name):
    if os.path.exists(csv_file_name):
        with open(csv_file_name, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            for row in reader:
                if row[2] == email and row[3] != password:
                    print("*** Wrong password. Try again. ***")
                    password = input("\nEnter a password (enter at least six characters):\t").strip()
                elif row[2] == email and row[3] == password:
                    if string_name == "user":
                        user_options()
                        return
                    else:
                        teacher_options()
                        return
    else:
        return False


def check_password(password):
    """
    Checking password for mistakes.
    :param password: user's password
    :return: Boolean
    """
    return password.isspace() or password == "" or len(password) < 6
