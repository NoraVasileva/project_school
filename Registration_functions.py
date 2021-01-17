from Project_2_test.Print.print_functions import print_registration
from Project_2_test.Classes.Class_Student import Student
from Project_2_test.Classes.Class_School import School
from Project_2_test.Classes.Class_Teacher import Teacher
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
    students = School()
    students.students_database_for_approval(student_reg)


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
    teachers = School()
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
    teachers.teachers_database_for_approval(teacher_reg)


def check_name(name, min_length_name, max_length_name):
    """
    Checking name length, if the name contains numbers and if the name is not empty.
    :param name: student's name for registration
    :param min_length_name: minimum name length
    :param max_length_name: maximum name length
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