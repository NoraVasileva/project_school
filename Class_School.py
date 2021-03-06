import csv
import os
import datetime
from copy import deepcopy
from Groups import find_group, show_only_groups
from print_functions import print_no_students, print_no_teachers, print_reg_4, print_teacher_information
from print_functions import print_edit_user, print_edit_user_information
from Registration_functions import check_name, check_email, \
    os_path_does_not_exists, date_check


class School:
    def os_path_exists_database(self, database):
        """
        Check for user accounts in the database.
        :param database: the name of the database
        :return: False or list of users
        """
        with open(database, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            temp_list = []
            for row in reader:
                temp_list.append(row)
            if len(temp_list) == 1:
                return False
            else:
                return temp_list

    def show_students_database(self):
        """
        List of all students from all groups. Option for administrator only.
        """
        database = "students_database.csv"
        if not os.path.exists(database):
            print_no_students()
            return
        else:
            self.os_path_exists_database(database)
            if self.os_path_exists_database is False:
                print_no_students()
            else:
                print("\n*** LIST OF STUDENTS IN PRIMARY SCHOOL 'PYTHON' ***")
                for student in self.os_path_exists_database(database):
                    print("\n\t\t", student[0], student[1], student[2])
                print("*" * 50)

    def show_teachers_database(self):
        """
        Display the list of teachers with the option to see the information about a specific teacher.
        """
        database = "teachers_database.csv"
        if not os.path.exists(database):
            print_no_teachers()
            return
        else:
            self.os_path_exists_database(database)
            if self.os_path_exists_database is False:
                print_no_teachers()
                return
            else:
                print("\n*** LIST OF TEACHERS IN PRIMARY SCHOOL 'PYTHON' ***")
                for teacher in self.os_path_exists_database(database):
                    print(f"\n\t\t{teacher[0]} {teacher[1]} {teacher[2]}")
                print("*" * 52)
            print("\n*** Do you want to see the information for a specific teacher? ***")
            choice = input("\nEnter Yes or No: ").capitalize().strip()
            while choice != "Yes" and choice != "No":
                print("\n*** We don't have this option. Try again. ***")
                choice = input("\nEnter Yes or No: ").capitalize().strip()
            if choice == "No":
                return
            else:
                email = input("\nEnter teacher's email address:\t")
                while check_email(email):
                    print("\n*** Try again. ***")
                    email = input("\nEnter teacher's email address:\t")
                with open("teachers_database.csv", "r") as file_1:
                    reader = csv.reader(file_1, delimiter="\t")
                    temp_list = []
                    for row in reader:
                        if email == row[2]:
                            temp_list.append(row[0])
                            temp_list.append(row[1])
                            temp_list.append(row[4])
                            temp_list.append(row[6])
                    if not temp_list:
                        print(f"\n*** Teacher with an e-mail address {email} does not exist. ***")
                    elif len(temp_list) == 4:
                        print("\n************* TEACHER INFORMATION *************")
                        print(f"\n\tName:"
                              f"\n\t\t{temp_list[0]}")
                        print(f"\n\tLast name:"
                              f"\n\t\t{temp_list[1]}")
                        print(f"\n\tStudy classes:")
                        groups = temp_list[2].split(";")
                        for gr in groups:
                            print(f'\t\t{gr}')
                        print(f"\n\tDate of commencement of work:"
                              f"\n\t\t{temp_list[3]}")
                        print("\n")
                        print("*" * 47)
                    else:
                        print("Something went wrong. Contact the administrator.")

    def delete_account(self, email, user_name):
        """
        Delete user's account from the database.
        :param email: user's e-mail address
        :param user_name: student, teacher or user
        """
        students_database = "students_database.csv"
        teachers_database = "teachers_database.csv"
        users_database = "users_database.csv"
        if user_name == "student":
            self.find_account(students_database, email)
            if os.path.exists("groups_database.csv"):
                with open("groups_database.csv", "r") as file:
                    reader = file.readlines()
                for gr in reader:
                    new_var = gr.replace('\n', '')
                    group = f"{new_var}.csv"
                    if os.path.exists(group):
                        with open(group, "r") as file_1:
                            reader = csv.reader(file_1, delimiter="\t")
                            for gr_1 in reader:
                                if gr_1[2] == email:
                                    self.overwriting_the_database(group, gr_1)
        elif user_name == "teacher":
            self.find_account(teachers_database, email)
        elif user_name == "user":
            self.find_account(users_database, email)

    def find_account(self, database, email):
        """
        Check if the database exists and have a registrations.
        Checks if the email address exists and deletes the user from the database.
        :param database: the name of the database
        :param email: user's e-mail address
        """
        os_path_exists_database = self.os_path_exists_database(database)
        if os_path_exists_database is False:
            print("\n*** There are no registrations yet. ***")
            return
        else:
            os_path_exists_student = self.os_path_exists(email, database)
            if os_path_exists_student is False:
                print(f"\n*** A user with an e-mail address {email} does not exists. ***")
            else:
                self.overwriting_the_database(database, os_path_exists_student)
                print(f"\n*** A user with an e-mail address {email} is deleted from the database. ***")

    def os_path_exists_registrations(self, database):
        """
        Check if there are existing registrations in the database.
        :param database: The name of the database
        :return: False or list of registrations
        """
        with open(database, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            temp_list = []
            for row in reader:
                temp_list.append(row)
            if len(temp_list) > 1:
                return temp_list
            else:
                return False

    def show_students_or_teachers_database_for_approval(self, database, user):
        """
        Display a list of new student/teacher registrations with options for approval or rejection.
        :param database: the name of the database
        :param user: teacher or student
        """
        if not os.path.exists(database):
            print("\n*** There are no registration requests yet. ***")
            return
        else:
            self.os_path_exists_registrations(database)
            if self.os_path_exists_registrations(database) is False:
                print("\n*** There are no registration requests yet. ***")
                return
            else:
                print_1 = ""
                if user == "student":
                    print_1 = "\n****************** STUDENT REGISTRATIONS LIST ****************"
                elif user == "teacher":
                    print_1 = "\n****************** TEACHER REGISTRATIONS LIST *****************"
                print(print_1)
                for users in self.os_path_exists_registrations(database):
                    print("\n\t\t", users[0], users[1], users[2])
                print("\n**************************************************************")
                print(print_1)
                print_reg_4()
                choice_3 = input("\nEnter a number from 1 to 3:\t").strip()
                while choice_3 != "1" and choice_3 != "2" and choice_3 != "3":
                    print("\n*** Try again. ***")
                    choice_3 = input("\nEnter a number from 1 to 3:\t").strip()
                if choice_3 == "1":
                    print("\n******************* APPROVAL OF REGISTRATION *****************")
                    email = input("\nEnter e-mail address:\t").strip()
                    while check_email(email):
                        print("\n*** Try again. ***")
                        email = input("\nEnter e-mail address:\t").strip()
                    print("\n\n*************************************************************")
                    if user == "student":
                        self.find_student(email)
                    elif user == "teacher":
                        self.find_teacher(email)
                elif choice_3 == "2":
                    print("\n******************* REJECTION OF REGISTRATION *****************")
                    email = input("\nEnter e-mail address:\t").strip()
                    while check_email(email):
                        print("\n*** Try again. ***")
                        email = input("\nEnter e-mail address:\t").strip()
                    print("\n")
                    print("*" * 63)
                    if user == "student":
                        self.deny_user(email, "student")
                    elif user == "teacher":
                        self.deny_user(email, "teacher")
                else:
                    return

    def os_path_exists(self, email, database):
        """
        Check if the email address exists in the database.
        :param email: student's email address
        :param database: the name of the database
        :return: False or list of student information
        """
        with open(database, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            temp_list = ""
            for row in reader:
                if row[2] == email:
                    temp_list = row
            if not temp_list:
                return False
            else:
                return temp_list

    def write_in_database(self, database, temp_list):
        """
        Add information in the database.
        :param database: the name of the database
        :param temp_list: list of information
        """
        with open(database, "a") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow(temp_list)

    def overwriting_the_database(self, database, user):
        """
        Overwriting the database with new information. Deleting unnecessary information.
        :param database: the name of the database
        :param user: list of user's information
        """
        users = []
        with open(database, "r") as file_1:
            reader = csv.reader(file_1, delimiter="\t")
            for row in reader:
                if row[2] != user[2]:
                    users.append(row)
        with open(database, "w") as file_2:
            writer = csv.writer(file_2, delimiter="\t")
            for user in users:
                writer.writerow(user)

    def find_student(self, email):
        """
        Add a student to the database with the option to enter a group.
        :param email: the student's email address
        """
        database_for_approval = "students_database_for_approval.csv"
        students_database = "students_database.csv"
        list_of_columns = ["First name", "Last name", "E-mail address", "Password"]
        list_of_columns_2 = ["First name", "Last name", "E-mail address"]
        temp_list = []
        self.os_path_exists(email, database_for_approval)
        if self.os_path_exists(email, database_for_approval) is False:
            print(f"\n*** A student with an email address '{email}' does not exist in the database. ***")
            return
        else:
            if not os.path.exists(students_database):
                os_path_does_not_exists(students_database, list_of_columns)
            if os.path.exists(students_database):
                for student in self.os_path_exists(email, database_for_approval):
                    temp_list.append(student)
                self.write_in_database(students_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was successfully approved. ***")
                self.overwriting_the_database(database_for_approval, temp_list)
            show_only_groups()
            group = input("\nIn which class you want to add the student? Enter class name:\t").title()
            while group == "":
                print("*** Try again. ***")
                group = input("\nIn which class you want to add the student? Enter class name:\t").title()
            group_database = f"{group}.csv"
            if os.path.exists(group_database):
                find_group(group)
                self.write_in_database(group_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]} was added successfully in {group}. ****")
            else:
                find_group(group)
                os_path_does_not_exists(group_database, list_of_columns_2)
                self.write_in_database(group_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]} was added successfully in {group}. ****")

    def find_email(self, database, email):
        """
        Check for e-mail address in the database.
        :param database: the name of the database
        :param email: user's e-mail address
        :return: False or list of user's information
        """
        with open(database, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            temp_list = []
            for row in reader:
                if row[2] == email:
                    temp_list.append(row[0])
                    temp_list.append(row[1])
                    temp_list.append(row[2])
                    temp_list.append(row[3])
            if not temp_list:
                return False
            else:
                return temp_list

    def add_in_list(self, database):
        """
        Open file and read it. Making a list from row 4.
        :param database: the name of the database
        return: list
        """
        with open(database, "r") as file:
            reader = csv.reader(file, delimiter="\t")
            all_classes = []
            for row in reader:
                all_classes.append(row[4])
            return all_classes

    def find_teacher(self, email):
        """
        Add a teacher to the database with the option to enter a group.
        :param email: the teacher's email address
        """
        database_for_approval = "teachers_database_for_approval.csv"
        database = "teachers_database.csv"
        columns = ["First name", "Last name", "E-mail address", "Password", "Class", "Birth", "Work"]
        temp_list = []
        if os.path.exists(database_for_approval):
            with open(database_for_approval, "r") as a_file:
                reader = csv.reader(a_file, delimiter="\t")
                for row in reader:
                    if row[2] == email:
                        temp_list.append(row[0])
                        temp_list.append(row[1])
                        temp_list.append(row[2])
                        temp_list.append(row[3])
                        temp_list.append(row[4])
                        temp_list.append(row[5])
                        temp_list.append(row[6])
                if not temp_list:
                    print(f"\n*** A teacher with an email address '{email}' does not exist in the database. ***")
                    return
                elif len(temp_list) == 7:
                    if not os.path.exists(database):
                        os_path_does_not_exists(database, columns)
                    choice = input("\nDo you want to enter the teacher's class name?"
                                   " Enter Yes or No: \t").title().strip()
                    while choice != "Yes" and choice != "No":
                        print("\n*** Try again. ***")
                        choice = input("\nDo you want to enter the teacher's class name?"
                                       " Enter Yes or No: \t").title().strip()
                    if choice == "Yes":
                        num = input("\nHow many classes do you want to add? Enter an integer from 1 to 4:\t").strip()
                        while num != "1" and num != "2" and num != "3" and num != "4":
                            print("\n*** Try again. ***")
                            num = input("\nHow many classes do you want to add? Enter an integer from 1 to 4:\t").strip()
                        if num == "1":
                            group = input("\nEnter the teacher's class name?:\t").strip().title()
                            while group.isspace() or group.isnumeric():
                                print("\n*** Try again. ***")
                                group = input("\nEnter the teacher's class name?:\t").strip().title()
                            self.add_in_list(database)
                            if group in self.add_in_list(database):
                                print(f"\n*** {group} already has a registered teacher. ***"
                                      f"\n*** You can add another class later in User account options. ***")
                            else:
                                temp_list[4] = group
                                print(f"\n*** {group} was successfully added to the teacher information. ***")
                        else:
                            num_1 = int(num)
                            str_num = ["first", "second", "third", "fourth"]
                            new_class_list = []
                            teacher_list = []
                            self.add_in_list(database)
                            for number in range(num_1):
                                teacher_class = input(f"\nEnter {str_num[number]} class name:\t").strip().title()
                                while teacher_class.isspace() or teacher_class.isnumeric():
                                    print("\n*** Try again. **")
                                    teacher_class = input(f"\nEnter {str_num[number]} class name:\t").strip().title()
                                new_class_list.append(teacher_class)
                                result = []
                                for num_class in range(len(self.add_in_list(database))):
                                    for num_group in range(len(new_class_list)):
                                        if new_class_list[num_group] in self.add_in_list(database)[num_class]:
                                            result.append(new_class_list[num_group])
                                if result:
                                    print(f"\n*** {teacher_class} already has a registered teacher. ***")
                                else:
                                    teacher_list.append(teacher_class)
                            temp_list[4] = ";".join(teacher_list)
                            print("\n *** Successfully added classes: ***")
                            for c in teacher_list:
                                print(f"\n\t\t{c}")
                            print("*" * 35)
                            print("\n*** You can add other class later in User accounts options. ***")
                    else:
                        print("\n*** You can add the name of the class later in User accounts options. ***")
                    if os.path.exists(database):
                        self.write_in_database(database, temp_list)
                        print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was "
                              f"successfully approved. ***")
                        self.overwriting_the_database(database_for_approval, temp_list)

    def deny_user(self, email, user):
        """
        Rejection of user registration. The information about the user is transferred to the user database.
        :param email: user's e-mail address
        :param user: teacher or student
        """
        user_terms = {
            "database_approval": None,
            "user_database": "users_database.csv",
            "columns": ["First name", "Last name", "E-mail address", "Password"],
            "temp_list": [],
            "person": None
        }
        if user == "student":
            user_terms["database_approval"] = "students_database_for_approval.csv"
            user_terms["person"] = "student"
        elif user == "teacher":
            user_terms["database_approval"] = "teachers_database_for_approval.csv"
            user_terms["person"] = "teacher"
        if os.path.exists(user_terms["database_approval"]):
            self.find_email(user_terms["database_approval"], email)
            if self.find_email(user_terms["database_approval"], email) is False:
                print(f'\n*** A {user_terms["person"]} with an email address "{email}" does not exist in the '
                      f'database. ***')
                return
            else:
                if not os.path.exists(user_terms["user_database"]):
                    os_path_does_not_exists(user_terms["user_database"], user_terms["columns"])
                if os.path.exists(user_terms["user_database"]):
                    for user in self.find_email(user_terms["database_approval"], email):
                        user_terms["temp_list"].append(user)
                    self.write_in_database(user_terms["user_database"], user_terms["temp_list"])
                self.overwriting_the_database(user_terms["database_approval"], user_terms["temp_list"])
                print(f"\n*** {user_terms['temp_list'][0]} {user_terms['temp_list'][1]}'s registration was rejected"
                      f" and added to users database. ***")
        else:
            print("\n*** There are no registration requests yet. ***")

    def show_users_database(self):
        """
        Display list of users from users database.
        """
        database = "users_database.csv"
        os_path_exists = os.path.exists(database)
        os_path_exists_database = self.os_path_exists_database(database)
        if not os_path_exists:
            print("\n*** There are no users to show yet. ***")
        if os_path_exists:
            if os_path_exists_database is False:
                print("\n*** There are no users to show yet. ***")
            else:
                printing_users = "\n*** LIST OF USERS IN PRIMARY SCHOOL 'PYTHON' ***"
                print(printing_users)
                for user in os_path_exists_database:
                    print("\n\t\t", user[0], user[1], user[2])
                print("\n")
                print("*" * len(printing_users))

    def edit_user(self):
        """
        Entering an e-mail address and a name of the database. Choosing a user to edit his information.
        Check if the database and the e-mail address exists.
        """
        user_terms = {
            "people": None,
            "person": None,
            "database": None,
            "email": None
                      }
        print_edit_user()
        choice = input("\nEnter a number from 1 to 4:\t")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("\n*** Try again. ***")
            choice = input("\nEnter a number from 1 to 4:\t")
        if choice == "4":
            return
        elif choice == "1":
            user_terms["database"] = "students_database.csv"
            user_terms["people"] = "students"
            user_terms["person"] = "student"
        elif choice == "2":
            user_terms["database"] = "teachers_database.csv"
            user_terms["people"] = "teachers"
            user_terms["person"] = "teacher"
        elif choice == "3":
            user_terms["database"] = "users_database.csv"
            user_terms["people"] = "users"
            user_terms["person"] = "user"
        if not os.path.exists(user_terms["database"]):
            print(f"\n*** There are no {user_terms['people']} to show yet. ***")
            return
        if os.path.exists(user_terms["database"]):
            self.os_path_exists_database(user_terms["database"])
            if self.os_path_exists_database(user_terms["database"]) is False:
                print(f"\n*** There are no {user_terms['people']} to show yet. ***")
                return
            else:
                printing = f"\n*** List of {user_terms['people']} in Primary School 'Python' ***"
                print(printing)
                for user in self.os_path_exists_database(user_terms["database"]):
                    print("\n\t\t", user[0], user[1], user[2])
                print("*" * len(printing))
                user_terms["email"] = input(f"\nEnter the email address of the {user_terms['person']} whose account"
                                            " you want to edit:\t").strip()
                while check_email(user_terms["email"]):
                    print("\n*** Try again. ***")
                    user_terms["email"] = input(f"\nEnter the email of the {user_terms['person']} whose account you want to edit:\t").strip()
        return user_terms["database"], user_terms["email"]

    def edit_student_or_user(self, database, user_name, email):
        """
        Editing student's or user's information. Show menu with options for the administrator.
        Overwriting the database with the edited information.
        :param database: the name of the database
        :param user_name: user's name
        :param email: teacher's e-mail address
        """
        edited_information_list = self.os_path_exists(email, database)
        original_info_list = deepcopy(edited_information_list)
        students_database = "students_database.csv"
        users_database = "users_database.csv"
        if edited_information_list is False:
            print(f"\n*** A user with an email address '{email}' "
                  f"does not exist in the database. ***")
            return
        else:
            print(f"\n****** USER INFORMATION ******\n\n\t\tFirst name: {edited_information_list[0]}"
                  f"\n\t\tLast name: {edited_information_list[1]}\n\t\tE-mail address: {edited_information_list[2]}")
            print("*" * 30)
            print_edit_user_information()
            choice_1 = input("\nEnter a number from 1 to 5:\t")
        while choice_1 != "1" and choice_1 != "2" and choice_1 != "3" and choice_1 != "4" \
                and choice_1 != "5":
            print("\n*** Try again. ***")
            choice_1 = input("\nEnter a number from 1 to 5:\t")
        if choice_1 == "1":
            first_name = input("\nEnter new first name:\t").strip().capitalize()
            while check_name(first_name, 2, 20):
                print("\n*** Try again. ***")
                first_name = input("\nEnter new name:\t").strip().capitalize()
            edited_information_list[0] = first_name
            print("\n*** First name edited successfully. ***")
        elif choice_1 == "2":
            last_name = input("\nEnter new last name:\t").strip().capitalize()
            while check_name(last_name, 5, 20):
                print("\n*** Try again. ***")
                last_name = input("\nEnter new last name:\t").strip().capitalize()
            edited_information_list[1] = last_name
            print("\n*** Last name edited successfully. ***")
        elif choice_1 == "3":
            email_1 = input("\nEnter new e-mail address:\t")
            while check_email(email_1):
                print("\n*** Try again. ***")
                email_1 = input("\nEnter new e-mail address:\t")
            edited_information_list[2] = email_1
            print("\n*** Email address edited successfully. ***")
        elif choice_1 == "4":
            password = input("\nEnter new password: \t")
            while password.isspace() or password == "" or len(password) < 6:
                print("\n*** Try again. ***")
                password = input("\nEnter new password: \t")
            edited_information_list[3] = password
            print("\n*** Password edited successfully. ***")
        if user_name == "student":
            self.overwriting_the_database(students_database, original_info_list)
            self.write_in_database(students_database, edited_information_list)
        elif user_name == "user":
            self.overwriting_the_database(users_database, original_info_list)
            self.write_in_database(users_database, edited_information_list)
        elif choice_1 == "5":
            return

    def edit_teacher(self, database, email):
        """
        Editing teacher's information. Show menu with options for the administrator.
        Overwriting the database with the edited information.
        :param database: the name of the database
        :param email: teacher's e-mail address
        """
        edited_information_list = self.os_path_exists(email, database)
        original_info_list = deepcopy(edited_information_list)
        teachers_database = "teachers_database.csv"
        date_now = datetime.datetime.now()
        year_now = int(date_now.year)
        if edited_information_list is False:
            print(f"\n*** A user with an email address '{email}' "
                  f"does not exist in the database. ***")
            return
        else:
            print(f"\n************** USER INFORMATION **************\n\n\t\tFirst name: {edited_information_list[0]}"
                  f"\n\t\tLast name: {edited_information_list[1]}\n\t\tE-mail address: {edited_information_list[2]}"
                  f"\n\t\tStudy classes: {edited_information_list[4]}"
                  f"\n\t\tBirth: {edited_information_list[5]}"
                  f"\n\t\tDate of commencement of work:{edited_information_list[6]}")
            print("*" * 46)
            print_teacher_information()
            choice_1 = input("\nEnter a number from 1 to 8:\t")
        while choice_1 != "1" and choice_1 != "2" and choice_1 != "3" and choice_1 != "4" \
                and choice_1 != "5" and choice_1 != "6" and choice_1 != "7" and choice_1 != 8:
            print("\n*** Try again. ***")
            choice_1 = input("\nEnter a number from 1 to 8:\t")
        if choice_1 == "8":
            return
        elif choice_1 == "1":
            first_name = input("\nEnter new first name:\t").strip().capitalize()
            while check_name(first_name, 2, 20):
                print("\n*** Try again. ***")
                first_name = input("\nEnter new name:\t").strip().capitalize()
            edited_information_list[0] = first_name
            print("\n*** First name edited successfully. ***")
        elif choice_1 == "2":
            last_name = input("\nEnter new last name:\t").strip().capitalize()
            while check_name(last_name, 5, 20):
                print("\n*** Try again. ***")
                last_name = input("\nEnter new last name:\t").strip().capitalize()
            edited_information_list[1] = last_name
            print("\n*** Last name edited successfully. ***")
        elif choice_1 == "3":
            email_1 = input("\nEnter new e-mail address:\t")
            while check_email(email_1):
                print("\n*** Try again. ***")
                email_1 = input("\nEnter new e-mail address:\t")
            edited_information_list[2] = email_1
            print("\n*** Email address edited successfully. ***")
        elif choice_1 == "4":
            password = input("\nEnter new password: \t")
            while password.isspace() or password == "" or len(password) < 6:
                print("\n*** Try again. ***")
                password = input("\nEnter new password: \t")
            edited_information_list[3] = password
            print("\n*** Password edited successfully. ***")
        elif choice_1 == "5":
            classes = input("Enter new study classes (ex.: First grade, Second grade):\t").strip().title()
            while classes.isalpha() is False or classes == "":
                print("\n*** Try again. ***")
                classes = input("Enter new study classes (ex.: First grade, Second grade):\t").strip().title()
            edited_information_list[4] = classes
            print("\n*** Classes edited successfully. ***")
        elif choice_1 == "6":
            date_of_birth = input("\nEnter date of birth. Enter an integer:\t").strip()
            month_of_birth = input("\nEnter month of birth. Enter an integer:\t").strip()
            year_of_birth = input("\nEnter year of birth. Enter an integer:\t").strip()
            while date_check(year_of_birth, month_of_birth, date_of_birth) is False or int(year_of_birth) < (
                    year_now - 75) or \
                    int(year_of_birth) >= year_now:
                print("\n*** Wrong information. Try again. ***")
                date_of_birth = input("\nEnter date of birth. Enter an integer:\t").strip()
                month_of_birth = input("\nEnter month of birth. Enter an integer:\t").strip()
                year_of_birth = input("\nEnter year of birth. Enter an integer:\t").strip()
            edited_information_list[5] = f"{date_of_birth}.{month_of_birth}.{year_of_birth}"
            print("\n*** Birth edited successfully. ***")
        elif choice_1 == "7":
            first_day_of_work = input("\nEnter first day of work. Enter an integer:\t").strip()
            first_month_of_work = input("\nEnter first month of work. Enter an integer:\t").strip()
            first_year_of_work = input("\nEnter first year of work. Enter an integer:\t").strip()
            while date_check(first_year_of_work, first_month_of_work, first_day_of_work) is False or \
                    int(first_year_of_work) >= year_now or int(first_year_of_work) < (year_now - 57):
                print("\n*** Wrong information. Try again. ***")
                first_day_of_work = input("\nEnter first day of work. Enter an integer:\t").strip()
                first_month_of_work = input("\nEnter first month of work. Enter an integer:\t").strip()
                first_year_of_work = input("\nEnter first year of work. Enter an integer:\t").strip()
            edited_information_list[6] = f"{first_day_of_work}.{first_month_of_work}.{first_year_of_work}"
            print("\n*** Work experience edited successfully. ***")
        self.overwriting_the_database(teachers_database, original_info_list)
        self.write_in_database(teachers_database, edited_information_list)
