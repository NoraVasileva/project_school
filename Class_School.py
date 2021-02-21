import csv
import os
from print_functions import print_no_students, print_no_teachers, print_reg_4
from print_functions import print_edit_user, print_edit_user_information
from Registration_functions import check_name, check_language, check_email, os_path_does_not_exists_group, \
    os_path_does_not_exists


class School:
# TODO: да помисля как да променя условията, които са ми if и else, да бъдат if, elif и else, за да нямам допълнителни условия в else.
# TODO: да преговоря PANDAS и да намеря bar plot, join функцията
# TODO: когато свършим целия проект да променим структурата на въвеждането във файловете, като използваме речници и Pandas
# num_list = [str(num) for num in range(1, 5)] # TODO: да преговоря циклите на един ред и речниците на един ред
# работи с по-малко елементи; речник на един ред: {num: num for num in range(1, 5)} - ключът и стойността са
# еднакви числа
# {key: value for key, value in zip(range(1, 5), range(10, 15)} - работи, когато ключът и
# стойността са с еднаква дължина на списъка. range(1, 5) ни е списъка с числа на ключовете, а range(10, 15) ни
# е списъка с числа на стойностите.
# създаване на списък от тупъли (с две променливи - v, v): [(v, v) for v in range(1, 5)]
# стойностите на променливите са еднакви числа
# TODO: да помисля как да направя речник от тупъли на един ред; да създам списък от обекти на един ред; речник
#  със списъци, които съдържат други списъци; да преговоря join

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
                    print(f"\n\t\t{teacher[0]} {teacher[1]}")
                print("*" * 52)
            print("\n*** Do you want to see the information for a specific teacher? ***")
            choice = input("\nEnter Yes or No: ").capitalize().strip()
            while choice != "Yes" and choice != "No":
                print("\n*** We don't have this option. Try again. ***")
                choice = input("\nEnter Yes or No: ").capitalize().strip()
            if choice == "No":
                return
            else:
                first_name = input("\nEnter teacher's first name: ").capitalize().strip()
                while check_name(first_name, 2, 20) and check_language(first_name):
                    print(f"\n*** Enter teacher's first name again. Wrong length (2-20) or language (en or bg)."
                          f" You had entered {first_name} ***")
                    first_name = input("\nEnter teacher's first name: ").capitalize().strip()
                last_name = input("\nEnter teacher's last name: ").capitalize().strip()
                while check_name(last_name, 5, 20) and check_language(last_name):
                    print(f"\n*** Enter teacher's name again. Wrong length (5-20) or language (en or bg)."
                          f" You had entered {last_name} ***")
                    last_name = input("\nEnter teacher's last name: ").capitalize().strip()
                with open("teachers_database.csv", "r") as file_1:
                    reader = csv.reader(file_1, delimiter="\t")
                    temp_list = []
                    for row in reader:
                        if first_name == row[0] and last_name == row[1]:
                            temp_list.append(row[0])
                            temp_list.append(row[1])
                            temp_list.append(row[4])
                            temp_list.append(row[6])
                    if not temp_list:
                        print(f"\n*** {first_name} {last_name} does not exist. ***")
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

    def os_path_exists_group(self, group):
        """
        Check if the group exists in the database.
        :param group: the name of the group
        :return: Boolean
        """
        find_group = False
        with open("groups_database.csv", "r") as file:
            list_groups = file.readlines()
            for row in list_groups:
                if group in row:
                    find_group = True
        return find_group

    def find_group(self, group):
        """
        Check if the group exists in the database. If the group does not exist, it is entered in the database.
        :param group: the name of the group
        """
        if not os.path.exists("groups_database.csv"):
            os_path_does_not_exists_group(group)
        elif self.os_path_exists_group(group) is False:
            os_path_does_not_exists_group(group)
        else:
            print(f"\n*** The {group} already exists. ***")

    def show_only_groups(self):
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

    def show_groups_database_with_students(self):
        if not os.path.exists("groups_database.csv"):
            print(f"\n*** No study classes created yet. ***")
        else:
            with open("groups_database.csv", "r") as file:
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
                with open("groups_database.csv", "r") as file_1:
                    reader = csv.reader(file_1, delimiter="\t")
                    temp_list = []
                    for row in reader:
                        if new_choice == row[0]:
                            temp_list.append(new_choice)
                    if not temp_list:
                        print(f"\n*** {new_choice} does not exist. ***")
                    elif len(temp_list) == 1:
                        csv_name = f"{row[0]}.csv"
                        group_name = new_choice.upper()
                        with open(csv_name, "r") as file_2:
                            reader_1 = csv.reader(file_2, delimiter="\t")
                            a = f"\n************** LIST OF {group_name} **************"
                            print(a)
                            for row_1 in reader_1:
                                print(f"\n\t\t{row_1[0]} {row_1[1]}")
                            print("\n", "*" * len(a))

    def delete_group_name(self, name, new_name):
# TODO: да се допише ако файлът съществува да му се промени и името - прехвърля се информацията от стария файл във файл с
# с новото име и после се изтрива стария файл;  след това се изтрива името на стария файл от базата от данни и се
# добавя новото име
        groups = list()
        with open("groups_database.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                groups.append(row)
                for gr in row:
                    if gr == name:
                        groups.remove(row)
        groups.append(new_name)
        with open("groups_database.csv", "a") as file:
            writer = csv.writer(file)
            for gr in groups:
                writer.writerow(gr)
        print(f"\n*** {name} was successfully edited to {new_name}. ***")

    def delete_group(self, name, name_csv):
        if os.path.exists(f"{name_csv}"):
            os.remove(name_csv)
            groups = list()
            with open("groups_database.csv", "r") as f:
                reader = csv.reader(f)
                for row in reader:
                    groups.append(row)
                    for gr in row:
                        if gr == name:
                            groups.remove(row)
            with open("groups_database.csv", "a") as file:
                writer = csv.writer(file)
                for gr in groups:
                    writer.writerow(gr)
            print(f"\n**** {name} deleted successfully. ***")

        else:
            print(f"\n*** {name} do not exists. ***")

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

    def os_path_exists_student(self, email, database):
        """
        Check if the email address exists in the database.
        :param email: student's email address
        :param database: the name of the database
        :return: False or list of student information
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
# TODO: да променя навсякъде където няма фор цикъл и въвеждам индекси в базата данни, трябва да записвам директно списъка
# (променливата без индекси). Да използвам само една функция за записване на файловете, защото вече нямам индекси
# Направено е с тази функция:
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
        :param user: user's information
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
        self.os_path_exists_student(email, database_for_approval)
        if self.os_path_exists_student(email, database_for_approval) is False:
            print(f"\n*** A student with an email address '{email}' does not exist in the database. ***")
            return
        else:
            if not os.path.exists(students_database):
                os_path_does_not_exists(students_database, list_of_columns)
            if os.path.exists(students_database):
                for student in self.os_path_exists_student(email, database_for_approval):
                    temp_list.append(student)
                self.write_in_database(students_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was successfully approved. ***")
                self.overwriting_the_database(database_for_approval, temp_list)
            student = School()
            student.show_only_groups()
            group = input("\nIn which class you want to add the student? Enter class name:\t").title()
            while group == "":
                print("*** Try again. ***")
                group = input("\nIn which class you want to add the student? Enter class name:\t").title()
            group_database = f"{group}.csv"
            if os.path.exists(group_database):
                self.find_group(group)
                self.write_in_database(group_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]} was added successfully in {group}. ****")
            else:
                self.find_group(group)
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

# НОВА ФУНКЦИЯ:
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

# НОВА ФУНКЦИЯ, КОЯТО СЪБИРА deny_student и deny_teacher в едно:
    def deny_user(self, email, user):
        """
        Rejection of user registration. The information about the user is transferred to the user database.
        :param email: user's e-mail address
        :param user: teacher or student
        """
        database_approval = None
        user_database = "users_database.csv"
        columns = ["First name", "Last name", "E-mail address", "Password"]
        temp_list = []
        person = None
        if user == "student":
            database_approval = "students_database_for_approval.csv"
            person = "student"
        elif user == "teacher":
            database_approval = "teachers_database_for_approval.csv"
            person = "teacher"
        if os.path.exists(database_approval):
            self.find_email(database_approval, email)
            if self.find_email(database_approval, email) is False:
                print(f"\n*** A {person} with an email address '{email}' does not exist in the database. ***")
                return
            else:
                if not os.path.exists(user_database):
                    os_path_does_not_exists(user_database, columns)
                if os.path.exists(user_database):
                    for user in self.find_email(database_approval, email):
                        temp_list.append(user)
                    self.write_in_database(user_database, temp_list)
                self.overwriting_the_database(database_approval, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was rejected and added "
                      f"to users database. ***")
        else:
            print("\n*** There are no registration requests yet. ***")

    # def deny_student(self, email):
    #    """
    #    Rejection of student registration. The information about the student is transferred to the user database.
    #    param email: student's e-mail address
    #    """
    #    database_approval = "students_database_for_approval.csv"
    #    database_users = "users_database.csv"
    #    columns = ["First name", "Last name", "E-mail address", "Password"]
    #    student_list = []
    #    if os.path.exists(database_approval):
    #        self.find_email(database_approval, email)
    #        if self.find_email(database_approval, email) is False:
    #            print(f"\n*** A student with an email address '{email}' does not exist in the database. ***")
    #            return
    #        else:
    #            if not os.path.exists(database_users):
    #                os_path_does_not_exists(database_users, columns)
    #            if os.path.exists(database_users):
    #                for user in self.find_email(database_approval, email):
    #                    student_list.append(user)
    #                self.write_in_database(database_users, student_list)
    #            self.overwriting_the_database(database_approval, student_list)
    #            print(f"\n*** {student_list[0]} {student_list[1]}'s registration was rejected and added "
    #                  f"to users database. ***")
    #    else:
    #        print("\n*** There are no registration requests yet. ***")

    # def deny_teacher(self, email):
    #     """
    #     Rejection of teacher registration. The information about the teacher is transferred to the user database.
    #     :param email: teacher's e-mail address
    #     """
    #     database_approval = "teachers_database_for_approval.csv"
    #     database_users = "users_database.csv"
    #     columns = ["First name", "Last name", "E-mail address", "Password"]
    #     teacher_list = []
    #     if os.path.exists(database_approval):
    #         with open(database_approval, "r") as file:
    #             reader = csv.reader(file, delimiter="\t")
    #             temp_list = []
    #             for row in reader:
    #                 if row[2] == email:
    #                     temp_list.append(row[0])
    #                     temp_list.append(row[1])
    #                     temp_list.append(row[2])
    #                     temp_list.append(row[3])
    #             if not temp_list:
    #                 print(f"\n*** A teacher with an email address '{email}' does not exist in the database. ***")
    #                 return
    #             else:
    #                 if not os.path.exists(database_users):
    #                     with open(database_users, "w") as file_1:
    #                         writer = csv.writer(file_1, delimiter="\t")
    #                         writer.writerow(columns)
    #                 if os.path.exists(database_users):
    #                     with open(database_users, "a") as file_2:
    #                         writer = csv.writer(file_2, delimiter="\t")
    #                         writer.writerow([
    #                             temp_list[0],
    #                             temp_list[1],
    #                             temp_list[2],
    #                             temp_list[3]
    #                         ])
    #                 with open(database_approval, "r") as file_3:
    #                     teachers = []
    #                     reader = csv.reader(file_3, delimiter="\t")
    #                     for row in reader:
    #                         if row[2] != temp_list[2]:
    #                             teachers.append(row)
    #                 with open(database_approval, "w") as file_4:
    #                     writer = csv.writer(file_4, delimiter="\t")
    #                     for teacher in teachers:
    #                         writer.writerow(teacher)
    #                 print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was rejected and added "
    #                       f"to users database. ***")
    #     else:
    #         print("\n*** There are no registration requests yet. ***")

    def show_users_database(self):
        """
        Display list of users from users database.
        """
        database = "users_database.csv"
        if not os.path.exists(database):
            print("\n*** There are no users to show yet. ***")
        if os.path.exists(database):
            self.os_path_exists_database(database)
            if self.os_path_exists_database(database) is False:
                print("\n*** There are no users to show yet. ***")
            else:
                printing_users = "\n*** LIST OF USERS IN PRIMARY SCHOOL 'PYTHON' ***"
                print(printing_users)
                for user in self.os_path_exists_database(database):
                    print("\n\t\t", user[0], user[1], user[2])
                print("\n")
                print("*" * len(printing_users))

# TODO: да се довърши:
    def edit_user(self):
        students_database = "students_database.csv"
        teachers_database = "teachers_database.csv"
        users_database = "users_database.csv"
        people = None
        person = None
        database = None
        print_edit_user()
        choice = input("\nEnter a number from 1 to 4:\t")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("\n*** Try again. ***")
            choice = input("\nEnter a number from 1 to 4:\t")
        if choice == "1":
            database = students_database
            people = "students"
            person = "student"
        elif choice == "2":
            database = teachers_database
            people = "teachers"
            person = "teacher"
        elif choice == "3":
            database = users_database
            people = "users"
            person = "user"
        if not os.path.exists(database):
            print(f"\n*** There are no {people} to show yet. ***")
            return
        if os.path.exists(database):
            self.os_path_exists_database(database)
            if self.os_path_exists_database(database) is False:
                print(f"\n*** There are no {people} to show yet. ***")
                return
            else:
                printing = f"\n*** List of {people} in Primary School 'Python' ***"
                print(printing)
                for user in self.os_path_exists_database(database):
                    print("\n\t\t", user[0], user[1], user[2])
                print("*" * len(printing))
                email = input(f"\nEnter the email address of the {person} whose account"
                              " you want to edit:\t").strip()
                while check_email(email):
                    print("\n*** Try again. ***")
                    email = input(f"\nEnter the email of the {person} whose account you want to edit:\t").strip()



                self.os_path_exists_student(students_database, email)
                if self.os_path_exists_student(students_database, email) is False:
                    print(f"\n*** A student with an email address '{email}' "
                          f"does not exist in the database. ***")
                    return
                else:
                    edited_information_list = []
                    for user in self.os_path_exists_student(students_database, email):
                        edited_information_list.append(user)
                    print(f"\n****** USER INFORMATION ******\n\n\t\tFirst name: {edited_information_list[0]}"
                          f"\n\t\tLast name: {edited_information_list[1]}\n\t\tE-mail address: {edited_information_list[2]}")
                    print("*" * 30)
                    print_edit_user_information()
                    choice_1 = input("\nEnter a number from 1 to 5:\t")
                    while choice_1 != "1" and choice_1 != "2" and choice_1 != "3" and choice_1 != "4"\
                            and choice_1 != "5":
                        print("\n*** Try again. ***")
                        choice_1 = input("\nEnter a number from 1 to 5:\t")
                    if choice_1 == "1":
                        first_name = input("\nEnter new first name:\t").strip().capitalize()
                        while check_name:
                            print("\n*** Try again. ***")
                            first_name = input("\nEnter new name:\t").strip().capitalize()
                        edited_information_list[0] = first_name
                        print("\n*** First name edited successfully. ***")
                    elif choice_1 == "2":
                        last_name = input("\nEnter new last name:\t").strip().capitalize()
                        while check_name:
                            print("\n*** Try again. ***")
                            last_name = input("\nEnter new last name:\t").strip().capitalize()
                        edited_information_list[1] = last_name
                        print("\n*** Last name edited successfully. ***")
                    elif choice_1 == "3":
                        pass


                                    # groups = list()
                                    # with open("groups_database.csv", "r") as f:
                                    #     reader = csv.reader(f)
                                    #     for row in reader:
                                    #         groups.append(row)
                                    #         for gr in row:
                                    #             if gr == name:
                                    #                 groups.remove(row)
                                    # groups.append(new_name)
                                    # with open("groups_database.csv", "a") as file:
                                    #     writer = csv.writer(file)
                                    #     for gr in groups:
                                    #         writer.writerow(gr)
                                    # print(f"\n*** {name} was successfully edited to {new_name}. ***")




# имената на файловете трябва да са идентични с имената на групите. След като администраторът създаде нова група
# трябва отдолу да напиша да се създава и файл със същото име, за да може да се принтират учениците от
# show_groups_database функцията
# няма да има втори файл за учениците, които са одобрени, а ще се местят директно от списъка за одобрение във файла на групата




