import csv
import os

from print_functions import print_registration, print_reg_1, print_reg_2, print_reg_3
from Class_Student import Student
from Class_Teacher import Teacher
import datetime
import re


def registration():
    """
    Registration form with options for students and teachers.
    """
    print_registration()
    role = input("\nPlease enter a number from 1 to 3:\t").strip()
    while role != "1" and role != "2" and role != "3":
        print("\n*** Sorry, we don't have this option. ***")
        print_registration()
        role = input("\nPlease enter a number from 1 to 3:\t").strip()
    if role == "1":
        student_registration()
    elif role == "2":
        teacher_registration()
    else:
        return


def student_registration():
    """
    Registration form for students. Entering personal data.
    """
    pr = "\n************* REGISTRATION FORM FOR STUDENTS *************"
    print(pr)
    first_name = input("\nWhat is your first name:\t").strip().capitalize()
    while check_name(first_name, 2, 20) and check_language(first_name):
        print(f"\n*** Enter your first name again. Wrong length (2-20) or language (en or bg).\
         Your first name is {first_name} ***")
        first_name = input("\nWhat is your first name:\t").strip().capitalize()
    last_name = input("\nWhat is your last name:\t").strip().capitalize()
    while check_name(last_name, 5, 20) and check_language(last_name):
        print(f"\n*** Enter your last name again. Wrong length (5-20) or language (en or bg).\
         Your last name is {last_name} ***")
        last_name = input("\nWhat is your last name:\t").strip().capitalize()
    email = input("\nEnter your e-mail address:\t").strip()
    while check_email(email):
        print("\n*** This e-mail address is not recognized. ***")
        email = input("\nEnter another e-mail address:\t").strip()
    password_1 = input("\nEnter a password (enter at least six characters):\t").strip()
    password_2 = input("\nEnter your password again:\t").strip()
    while check_new_password(password_1, password_2):
        print("\n*** Your password is incorrect. Try again. ***")
        password_1 = input("\nEnter a password (enter at least six characters):\t").strip()
        password_2 = input("\nEnter your password again:\t").strip()
    print("*" * len(pr))
    student_reg = Student(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password_1
    )
    students_database_for_approval(student_reg)


def students_database_for_approval(student: Student):
    """
    Check if the student has already created a registration. If there is no registration, a new one is created.
    :param student: object from class Student
    """
    students_database = "students_database.csv"
    students_database_for_approval = "students_database_for_approval.csv"
    list_columns = ["First name", "Last name", "E-mail address", "Password"]

    if not os.path.exists(students_database):
        os_path_does_not_exists(students_database, list_columns)
    if os.path.exists(students_database):
        os_path_exists(students_database, student)
        if os_path_exists is True:
            print_reg_1()
            return
    if not os.path.exists(students_database_for_approval):
        os_path_does_not_exists(students_database_for_approval, list_columns)
    if os.path.exists(students_database_for_approval):
        os_path_exists(students_database_for_approval, student)
        if os_path_exists is True:
            print_reg_2()
            return
        else:
            with open(students_database_for_approval, "a") as file:
                writer = csv.writer(file, delimiter="\t")
                temp_list = [
                    student.get_first_name(),
                    student.get_last_name(),
                    student.get_email(),
                    student.get_password()
                ]
                writer.writerow([temp_list[0], temp_list[1], temp_list[2], temp_list[3]])
                print_reg_3()


def teacher_registration():
    """
    Registration form for teachers. Entering personal data.
    """
    date_now = datetime.datetime.now()
    year_now = int(date_now.year)
    pr = "\n************* REGISTRATION FORM FOR TEACHERS *************"
    print(pr)
    first_name = input("\nWhat is your first name?:\t").strip().capitalize()
    while check_name(first_name, 2, 20) and check_language(first_name):
        print(f"\n*** Enter your first name again. Wrong length (2-20) or language (en or bg).\
         Your first name is {first_name} ***")
        first_name = input("\nWhat is your first name?:\t").strip().capitalize()
    last_name = input("\nWhat is your last name?:\t").strip().capitalize()
    while check_name(last_name, 5, 20) and check_language(last_name):
        print(f"\n*** Enter your last name again. Wrong length (5-20) or language (en or bg).\
         Your last name is {last_name} ***")
        last_name = input("\nWhat is your last name?:\t").strip().capitalize()
    date_of_birth = input("\nOn what date were you born? Enter an integer:\t").strip()
    month_of_birth = input("\nIn what month were you born? Enter an integer:\t").strip()
    year_of_birth = input("\nIn what year were you born? Enter an integer:\t").strip()
    while date_check(year_of_birth, month_of_birth, date_of_birth) is False or int(year_of_birth) < (year_now - 75) or\
            int(year_of_birth) >= year_now:
        print("\n*** Wrong information. Try again. ***")
        date_of_birth = input("\nOn what date were you born? Enter an integer:\t").strip()
        month_of_birth = input("\nIn what month were you born? Enter an integer:\t").strip()
        year_of_birth = input("\nIn what year were you born? Enter an integer:\t").strip()
    first_day_of_work = input("\nOn what date did you start working as a teacher? Enter an integer:\t").strip()
    first_month_of_work = input("\nIn which month did you start working as a teacher? Enter an integer:\t").strip()
    first_year_of_work = input("\nIn what year did you start working as a teacher? Enter an integer:\t").strip()
    while date_check(first_year_of_work, first_month_of_work, first_day_of_work) is False or\
            int(first_year_of_work) >= year_now or int(first_year_of_work) < (year_now - 57):
        print("\n*** Wrong information. Try again. ***")
        first_day_of_work = input("\nOn what date did you start working as a teacher? Enter an integer:\t").strip()
        first_month_of_work = input("\nIn which month did you start working as a teacher? Enter an integer:\t").strip()
        first_year_of_work = input("\nIn what year did you start working as a teacher? Enter an integer:\t").strip()
    if int(year_of_birth) < year_now - 75 or int(year_of_birth) > year_now - 18 or \
            int(first_year_of_work) < int(year_of_birth) + 16:
        print("\n*** We are sorry, but you cannot register on our site. ***\n*** Please contact an administrator. ***")
        return
    email = input("\nEnter your e-mail address:\t").strip()
    while check_email(email):
        print("\n*** This e-mail address is not recognized. ***")
        email = input("\nEnter another e-mail address:\t").strip()
    password_1 = input("\nEnter a password (enter at least six characters):\t").strip()
    password_2 = input("\nEnter your password again:\t").strip()
    while check_new_password(password_1, password_2):
        print("\n*** Your password is incorrect. Try again. ***")
        password_1 = input("\nEnter a password (enter at least six characters):\t").strip()
        password_2 = input("\nEnter your password again:\t").strip()
    print("*" * len(pr))
    teacher_reg = Teacher(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password_1,
        group="No study class",
        date_of_birth=date_of_birth,
        month_of_birth=month_of_birth,
        year_of_birth=year_of_birth,
        first_day_of_work=first_day_of_work,
        first_month_of_work=first_month_of_work,
        first_year_of_work=first_year_of_work
    )
    teachers_database_for_approval(teacher_reg)


def teachers_database_for_approval(teacher: Teacher):
    """
    Check if the teacher has already created a registration. If there is no registration, a new one is created.
    :param teacher: class Teacher
    """
    teachers_database = "teachers_database.csv"
    teachers_database_for_approval = "teachers_database_for_approval.csv"
    list_columns = [
            "First name",
            "Last name",
            "E-mail address",
            "Password",
            "Class",
            "Birth",
            "Work"
        ]
    if not os.path.exists(teachers_database):
        os_path_does_not_exists(teachers_database, list_columns)
    if os.path.exists(teachers_database):
        os_path_exists(teachers_database, teacher)
        if os_path_exists is True:
            print_reg_1()
            return
    if not os.path.exists(teachers_database_for_approval):
        os_path_does_not_exists(teachers_database_for_approval, list_columns)
    if os.path.exists(teachers_database_for_approval):
        os_path_exists(teachers_database_for_approval, teacher)
        if os_path_exists is True:
            print_reg_2()
            return
        else:
            with open(teachers_database_for_approval, "a") as file:
                a = teacher.get_first_day_of_work()
                b = teacher.get_first_month_of_work()
                c = teacher.get_first_year_of_work()
                work = f"{a}.{b}.{c}"
                d = teacher.get_date_of_birth()
                e = teacher.get_month_of_birth()
                f = teacher.get_year_of_birth()
                birth = f"{d}.{e}.{f}"
                writer = csv.writer(file, delimiter="\t")
                temp_list = [
                    teacher.get_first_name(),
                    teacher.get_last_name(),
                    teacher.get_email(),
                    teacher.get_password(),
                    "No study class",
                    birth,
                    work
                ]
                writer.writerow([
                    temp_list[0],
                    temp_list[1],
                    temp_list[2],
                    temp_list[3],
                    temp_list[4],
                    temp_list[5],
                    temp_list[6]
                ])
                print_reg_3()


def os_path_exists(database, user):
    """
    Check if the email address exists in the database upon registration.
    :param database: the name of the database
    :param user: class Teacher or class Student
    :return: Boolean
    """
    with open(database, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        temp_list = []
        for row in reader:
            if row[2] == user.get_email():
                temp_list.append(row[2])
    if len(temp_list) == 1:
        return True
    else:
        return False


def os_path_does_not_exists(database, list_of_columns):
    """
    Enter the column names in the student database.
    :param database: the name of the database
    """
    with open(database, "w") as new_file:
        writer = csv.writer(new_file, delimiter="\t")
        writer.writerow(list_of_columns)


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


def check_name(name, min_length_name, max_length_name):
    """
    Checking name length, if the name contains numbers and if the name is not empty.
    :param name: student's name for registration
    :param min_length_name: minimum name length - 2 for first name; 5 for last name
    :param max_length_name: maximum name length - 20
    :return: Boolean
    """
    return name.isspace() or name.isalpha() is False or len(name) > max_length_name or len(name) < min_length_name


def check_email(email):
    """
    Checking e-mail address for mistakes.
    :param email: user's e-mail address
    :return: Boolean
    """
    return email.isspace() or email == "" or email.endswith("@") or email.startswith("@") or email.count("@") > 1 or\
           email.count("@") == 0


def check_new_password(password_1, password_2):
    """
    Checking passwords for mistakes.
    :param password_1: user's password
    :param password_2: repetition of the user's password
    :return: Boolean
    """
    return password_1.isspace() or password_1 == "" or len(password_1) < 6 or password_1 != password_2


def date_check(year, month, day):
    """
    Verification of date of birth information.
    :param year: year of birth
    :param month: month of birth
    :param day: year of birth
    :return: Boolean
    """
    try:
        datetime.date(int(year), int(month), int(day))
        return True
    except:
        return False


def check_language(text):
    if bool(re.search('[а-яА-Я]', text)) and bool(re.search('[A-Za-z]', text)):
        return False
    if bool(re.search('[а-яА-Я]', text)):
        return True
    if bool(re.search('[A-Za-z]', text)):
        return True
    return False
