import csv
import os
# TODO: да попитам Милена дали импортите трябва да са от гитхъб или локални, защото в момента са смесени
from Github_project_school.Registration_functions import check_name, check_language
from Github_project_school.print_functions import print_reg_1, print_reg_2, print_reg_3, print_no_students, \
    print_no_teachers, print_reg_4
from Project_2_test.Classes.Class_Student import Student
from Project_2_test.Classes.Class_Teacher import Teacher
from Project_2_test.Print.print_functions import print_edit_user, print_edit_user_information
from Project_2_test.Registration.Registration_functions import check_email


class School:

# TODO: да преговоря PANDAS и да намеря bar plot, typora
# TODO: когато свършим целия проект да променим структурата на въвеждането във файловете, като използваме речници и Pandas

    def os_path_exists(self, database, user):
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

    def os_path_does_not_exists(self, database, list_of_columns):
        """
        Enter the column names in the student database.
        :param database: the name of the database
        """
        with open(database, "w") as new_file:
            writer = csv.writer(new_file, delimiter="\t")
            writer.writerow(list_of_columns)

    def students_database_for_approval(self, student: Student):
        """
        Check if the student has already created a registration. If there is no registration, a new one is created.
        :param student: class Student
        """
        students_database = "students_database.csv"
        students_database_for_approval = "students_database_for_approval.csv"
        list_columns = ["First name", "Last name", "E-mail address", "Password"]

        if not os.path.exists(students_database):
            self.os_path_does_not_exists(students_database, list_columns)
        if os.path.exists(students_database):
            self.os_path_exists(students_database, Student)
            if self.os_path_exists is True:
                print_reg_1()
                return
        if not os.path.exists(students_database_for_approval):
            self.os_path_does_not_exists(students_database_for_approval, list_columns)
        if os.path.exists(students_database_for_approval):
            self.os_path_exists(students_database_for_approval, Student)
            if self.os_path_exists is True:
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

    def teachers_database_for_approval(self, teacher: Teacher):
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
            self.os_path_does_not_exists(teachers_database, list_columns)
        if os.path.exists(teachers_database):
            self.os_path_exists(teachers_database, Teacher)
            if self.os_path_exists is True:
                print_reg_1()
                return
        if not os.path.exists(teachers_database_for_approval):
            self.os_path_does_not_exists(teachers_database_for_approval, list_columns)
        if os.path.exists(teachers_database_for_approval):
            self.os_path_exists(teachers_database_for_approval, Teacher)
            if self.os_path_exists is True:
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

    def os_path_exists_database(self, database):
        """
        Check for student accounts in the database.
        :param database: the name of the database
        :return: False or list of students
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
                    print(f"\n*** Enter teacher's first name again. Wrong length (2-20) or language (en or bg).\
                     You had entered {first_name} ***")
                    first_name = input("\nEnter teacher's first name: ").capitalize().strip()
                last_name = input("\nEnter teacher's last name: ").capitalize().strip()
                while check_name(last_name, 5, 20) and check_language(last_name):
                    print(f"\n*** Enter teacher's name again. Wrong length (5-20) or language (en or bg).\
                     You had entered {last_name} ***")
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
        if os.path.exists("groups_database.csv"):
            with open("groups_database.csv", "r") as file:
                reader = csv.reader(file)
                temp_list = []
                for row in reader:
                    if row == group:
                        temp_list.append(group)
                if temp_list:
                    return True
                else:
                    return False

    def os_path_does_not_exists_group(self, group):
        """
        Add a new group to the database.
        :param group: the name of the group
        """
        with open("groups_database.csv", "a") as file:
            writer = csv.writer(file, newline="")
            writer.writerow([group])
            print(f"\n*** The {group} was created successfully. ***")

    def find_group(self, group):
        """
        Check if the group exists in the database. If the group does not exist, it is entered in the database.
        :param group: the name of the group
        """
        if not os.path.exists("groups_database.csv"):
            self.os_path_does_not_exists_group(group)
        else:
            if self.os_path_exists_group(group) is False:
                self.os_path_does_not_exists_group(group)
            else:
                print(f"\n*** The {group} already exists. ***")

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

    def delete_group_name(self, name, new_name):
# TODO: да се допише ако файлът съществува да му се промени и името - прехвърля се информацията от стария файл в файл с
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

# НОВА ФУНКЦИЯ:
    def os_path_exists_registrations(self, database):
        """
        Check if there are existing registrations in the database.
        :param database: The name of the database
        :return: False or list of registrations
        """
        with open(database, "r") as file:
            reader = csv.reader(file)
            temp_list = []
            for row in reader:
                temp_list.append(row)
            if len(temp_list) > 1:
                return temp_list
            else:
                return False

    def show_students_database_for_approval(self):
        """
        Display a list of new student registrations with options for approval or rejection.
        """
        database = "students_database_for_approval.csv"
        if not os.path.exists(database):
            print("\n*** There are no registration requests yet. ***")
            return
        else:
            self.os_path_exists_registrations(database)
            if self.os_path_exists_registrations is False:
                print("\n*** There are no registration requests yet. ***")
                return
            else:
                print("\n****************** STUDENT REGISTRATIONS LIST ****************")
                for student in self.os_path_exists_registrations(database):
                    print("\n\t\t", student[0], student[1], student[2])
                print("\n**************************************************************")
                print("\n******************* STUDENT REGISTRATIONS *****************")
                print_reg_4()
                choice_3 = input("\nEnter a number from 1 to 3:\t").strip()
                while choice_3 != "1" and choice_3 != "2" and choice_3 != "3":
                    print("\n*** Try again. ***")
                    choice_3 = input("\nEnter a number from 1 to 3:\t").strip()
                if choice_3 == "1":
                    print("\n******************* APPROVAL OF REGISTRATION *****************")
                    email = input("\nEnter student's e-mail address:\t").strip()
                    while check_email(email):
                        print("\n*** Try again. ***")
                        email = input("\nEnter student's e-mail address:\t").strip()
                    print("\n\n*************************************************************")
                    student = School()
                    student.find_student(email)
                elif choice_3 == "2":
                    print("\n******************* REJECTION OF REGISTRATION *****************")
                    email = input("\nEnter student's e-mail address:\t").strip()
                    while check_email(email):
                        print("\n*** Try again. ***")
                        email = input("\nEnter student's e-mail address:\t").strip()
                    print("\n")
                    print("*" * 63)
                    student = School()
                    student.deny_student(email)
                else:
                    return

    def show_teachers_database_for_approval(self):
        # TODO: да използвам функцията os_path_exists_registrations за да съкратя кода
        if os.path.exists("teachers_database_for_approval.csv"):
            with open("teachers_database_for_approval.csv", "r") as file:
                reader = csv.reader(file, delimiter="\t")
                temp_list = []
                for row in reader:
                    temp_list.append(row)
                if len(temp_list) > 1:
                    print("\n****************** TEACHER REGISTRATIONS LIST *****************")
                    for teacher in temp_list:
                        print("\n", teacher[0], teacher[1], teacher[2])
                    print("\n\n**************************************************************")
                    print("\n******************* TEACHER REGISTRATIONS *****************")
                    print_reg_4()
                    choice_3 = input("\nEnter a number from 1 to 3: ").strip()
                    while choice_3 != "1" and choice_3 != "2" and choice_3 != "3":
                        print("\n*** Try again. ***")
                        choice_3 = input("\nEnter a number from 1 to 3: ").strip()
                    if choice_3 == "1":
                        print("\n******************* APPROVAL OF REGISTRATION *****************")
                        email = input("\nEnter teacher's e-mail address:\t").strip()
                        while check_email(email):
                            print("\n*** Try again. ***")
                            email = input("\nEnter teacher's e-mail address:\t").strip()
                        print("\n\n*************************************************************")
                        teacher = School()
                        teacher.find_teacher(email)
                    elif choice_3 == "2":
                        print("\n******************* REJECTION OF REGISTRATION *****************")
                        email = input("\nEnter teacher's e-mail address:\t").strip()
                        while check_email(email):
                            print("\n*** Try again. ***")
                            email = input("\nEnter teacher's e-mail address:\t").strip()
                        print("\n")
                        print("*" * 63)
                        teacher = School()
                        teacher.deny_teacher(email)
                    else:
                        return
                else:
                    print("\n*** There are no registration requests yet. ***")
                    return
        else:
            print("\n*** There are no registration requests yet. ***")


# НОВА ФУНКЦИЯ:
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

# НОВА ФУНКЦИЯ:
    def write_in_group_database(self, database, file_list):
        """
        Add student's information in group database.
        :param database: the name of the group database
        :param file_list: list of student's information
        """
        with open(database, "a") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow([
                file_list[0],
                file_list[1],
                file_list[2]
            ])

# НОВА ФУНКЦИЯ:
    def write_in_database(self, database, user_list):
        """
        Add user information in the database.
        :param database: the name of the database
        :param user_list: list of user's information
        """
        with open(database, "a") as file:
            writer = csv.writer(file, delimiter="\t")
            writer.writerow([
                user_list[0],
                user_list[1],
                user_list[2],
                user_list[3]
            ])

    def find_student(self, email):
        """
        Add a student to the database with the option to enter a group.
        :param email: the student's email address
        """
        database_for_approval = "students_database_for_approval.csv"
        students_database = "students_database.csv"
        groups_database = "groups_database.csv"
        list_of_columns = ["First name", "Last name", "E-mail address", "Password"]
        temp_list = []
        self.os_path_exists_student(email, database_for_approval)
        if self.os_path_exists_student is False:
            print(f"\n*** A student with an email address '{email}' does not exist in the database. ***")
            return
        else:
            if not os.path.exists(students_database):
                self.os_path_does_not_exists(students_database, list_of_columns)
            if os.path.exists(students_database):
                for student in self.os_path_exists_student(email, database_for_approval):
                    temp_list.append(student)
                self.write_in_database(students_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was successfully approved. ***")
                with open(database_for_approval, "r") as file_1:
                    students = []
                    reader = csv.reader(file_1, delimiter="\t")
                    for row in reader:
                        if row[2] != temp_list[2]:
                            students.append(row)
                self.os_path_does_not_exists(database_for_approval, list_of_columns)
                with open(database_for_approval, "a") as file_2:
                    writer = csv.writer(file_2, delimiter="\t")
                    for student in students:
                        writer.writerow(student)
            student = School()
            student.show_only_groups()
            group = input("\nIn which class you want to add the student? Enter class name:\t").title()
            while group == "":
                print("*** Try again. ***")
                group = input("\nIn which class you want to add the student? Enter class name:\t").title()
            group_database = f"{group}.csv"
            if os.path.exists(group_database):
                self.write_in_group_database(group_database, temp_list)
                print(f"\n*** {temp_list[0]} {temp_list[1]} was added successfully in {group}. ****")
            else:
                self.os_path_does_not_exists(group_database, list_of_columns)
                self.write_in_group_database(group_database, temp_list)
                print(f"\n*** The {group} was created successfully. ***"
                      f"\n*** {temp_list[0]} {temp_list[1]} was added successfully "
                      f"in {group}. ****")
        # if os.path.exists(groups_database):
        #     with open(groups_database, "r") as file_3:
        #         reader = csv.reader(file_3, delimiter="\t")
        #         temp_list_1 = []
        #         for gr in reader:
        #             if gr == group:
        #                 temp_list_1.append(gr)
        #         if not temp_list_1:
        #             with open(groups_database, "a") as file_4:
        #                 writer = csv.writer(file_4, delimiter="\t")
        #                 writer.writerow([f"{group}"])
        # else:
        #     with open(groups_database, "a") as file_5:
        #         writer = csv.writer(file_5, delimiter="\t")
        #         writer.writerow([f"{group}"])

# НОВА ФУНКЦИЯ:
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

    def deny_student(self, email):
        database_approval = "students_database_for_approval.csv"
        database_users = "users_database.csv"
        columns = ["First name", "Last name", "E-mail address", "Password"]
        student_list = []
        if os.path.exists(database_approval):
            self.find_email(database_approval, email)
            if self.find_email(database_approval, email) is False:
                print(f"\n*** A student with an email address '{email}' does not exist in the database. ***")
                return
            else:
                if not os.path.exists(database_users):
                    self.os_path_does_not_exists(database_users, columns)
                if os.path.exists(database_users):
                    for user in self.find_email(database_approval, email):
                        student_list.append(user)
                    self.write_in_database(database_users, student_list)
                with open(database_approval, "r") as file:
                    students = []
                    reader = csv.reader(file, delimiter="\t")
                    for row in reader:
                        if row[2] != student_list[2]:
                            students.append(row)
                with open(database_approval, "w") as file_1:
                    writer = csv.writer(file_1, delimiter="\t")
                    for student in students:
                        writer.writerow(student)
                print(f"\n*** {student_list[0]} {student_list[1]}'s registration was rejected and added "
                      f"to users database. ***")
        else:
            print("\n*** There are no registration requests yet. ***")

    def find_teacher(self, email):
        if os.path.exists("teachers_database_for_approval.csv"):
            with open("teachers_database_for_approval.csv", "r") as a_file:
                reader = csv.reader(a_file, delimiter="\t")
                temp_list = []
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
                    if not os.path.exists("teachers_database.csv"):
                        with open("teachers_database.csv", "w") as b_file:
                            writer = csv.writer(b_file, delimiter="\t")
                            writer.writerow([
                                "First name",
                                "Last name",
                                "E-mail address",
                                "Password",
                                "Class",
                                "Birth",
                                "Work"
                            ])
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
                            with open("teachers_database.csv", "r") as c_file:
                                reader = csv.reader(c_file, delimiter='\t')
                                classes = []
                                temp_list_1 = []
                                for row in reader:
                                    classes.append(row[4])
                                for gr in range(len(classes)):
                                    if group in classes[gr]:
                                        temp_list_1.append(group)
                            if temp_list:
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
                            with open("teachers_database.csv", "r") as d_file:
                                reader = csv.reader(d_file, delimiter="\t")
                                all_classes = []
                                for row in reader:
                                    all_classes.append(row[4])
                            for number in range(num_1):
                                teacher_class = input(f"\nEnter {str_num[number]} class name:\t").strip().title()
                                while teacher_class.isspace() or teacher_class.isnumeric():
                                    print("\n*** Try again. **")
                                    teacher_class = input(f"\nEnter {str_num[number]} class name:\t").strip().title()
                                new_class_list.append(teacher_class)
                                result = []
                                for num_class in range(len(all_classes)):
                                    for num_group in range(len(new_class_list)):
                                        if new_class_list[num_group] in all_classes[num_class]:
                                            result.append(new_class_list[num_group])
                                if result:
                                    print(f"\n*** {teacher_class} already has a registered teacher. ***")
                                else:
                                    teacher_list.append(teacher_class)
                            if len(teacher_list) == 1:
                                groups = teacher_list[0]
                            elif len(teacher_list) == 2:
                                groups = f"{teacher_list[0]};{teacher_list[1]}"
                            elif len(teacher_list) == 3:
                                groups = f"{teacher_list[0]};{teacher_list[1]};{teacher_list[2]}"
                            elif len(teacher_list) == 4:
                                groups = f"{teacher_list[0]};{teacher_list[1]};{teacher_list[2]};{teacher_list[3]}"
                            temp_list[4] = groups
                            print("\n *** Successfully added classes: ***")
                            for c in teacher_list:
                                print(f"\n\t\t{c}")
                            print("*" * 35)
                            print("\n*** You can add other class later in User accounts options. ***")
                    else:
                        print("\n*** You can add the name of the class later in User accounts options. ***")
                    if os.path.exists("teachers_database.csv"):
                        with open("teachers_database.csv", "a") as e_file:
                            writer = csv.writer(e_file, delimiter="\t")
                            writer.writerow([
                                temp_list[0],
                                temp_list[1],
                                temp_list[2],
                                temp_list[3],
                                temp_list[4],
                                temp_list[5],
                                temp_list[6]
                            ])
                        print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was "
                              f"successfully approved. ***")
                        with open("teachers_database_for_approval.csv", "r") as f_file:
                            teachers = []
                            reader = csv.reader(f_file, delimiter="\t")
                            for row in reader:
                                if row[2] != temp_list[2]:
                                    teachers.append(row)
                        with open("teachers_database_for_approval.csv", "w") as g_file:
                            writer = csv.writer(g_file, delimiter="\t")
                            for teacher in teachers:
                                writer.writerow([
                                    teacher[0],
                                    teacher[1],
                                    teacher[2],
                                    teacher[3],
                                    teacher[4],
                                    teacher[5],
                                    teacher[6]
                                ])

    def deny_teacher(self, email):
        if os.path.exists("teachers_database_for_approval.csv"):
            with open("teachers_database_for_approval.csv", "r") as file:
                reader = csv.reader(file, delimiter="\t")
                temp_list = []
                for row in reader:
                    if row[2] == email:
                        temp_list.append(row[0])
                        temp_list.append(row[1])
                        temp_list.append(row[2])
                        temp_list.append(row[3])
                if not temp_list:
                    print(f"\n*** A teacher with an email address '{email}' does not exist in the database. ***")
                    return
                else:
                    if not os.path.exists("users_database.csv"):
                        with open("users_database.csv", "w") as file_1:
                            writer = csv.writer(file_1, delimiter="\t")
                            writer.writerow(["First name", "Last name", "E-mail address", "Password"])
                    if os.path.exists("users_database.csv"):
                        with open("users_database.csv", "a") as file_2:
                            writer = csv.writer(file_2, delimiter="\t")
                            writer.writerow([
                                temp_list[0],
                                temp_list[1],
                                temp_list[2],
                                temp_list[3]
                            ])
                    with open("teachers_database_for_approval.csv", "r") as file_3:
                        teachers = []
                        reader = csv.reader(file_3, delimiter="\t")
                        for row in reader:
                            if row[2] != temp_list[2]:
                                teachers.append(row)
                    with open("teachers_database_for_approval.csv", "w") as file_4:
                        writer = csv.writer(file_4, delimiter="\t")
                        for teacher in teachers:
                            writer.writerow(teacher)
                    print(f"\n*** {temp_list[0]} {temp_list[1]}'s registration was rejected and added "
                          f"to users database. ***")
        else:
            print("\n*** There are no registration requests yet. ***")

    def show_users_database(self):
        if not os.path.exists("users_database.csv"):
            print("\n*** There are no users to show yet. ***")
        if os.path.exists("users_database.csv"):
            with open("users_database.csv", "r") as file:
                reader = csv.reader(file, delimiter="\t")
                temp_list = []
                for row in reader:
                    temp_list.append(row)
            if len(temp_list) == 1:
                print("\n*** There are no users to show yet. ***")
            else:
                printing_users = "\n*** LIST OF USERS IN PRIMARY SCHOOL 'PYTHON' ***"
                print(printing_users)
                for user in temp_list:
                    print("\n\t\t", user[0], user[1], user[2])
                print("\n")
                print("*" * len(printing_users))

# TODO: да се довърши:
    def edit_user(self):
        print_edit_user()
        choice = input("\nEnter a number from 1 to 4:\t")
        while choice != "1" and choice != "2" and choice != "3" and choice != "4":
            print("\n*** Try again. ***")
            choice = input("\nEnter a number from 1 to 4:\t")
            # "\n\n# 1: Edit student's account\n\n# 2: Edit teacher's account"
            # "\n\n# 3: Edit user's account\n\n# 4: Quit"
        if choice == "1":
            if not os.path.exists("students_database.csv"):
                print("\n*** There are no students to show yet. ***")
                return
            if os.path.exists("students_database.csv"):
                with open("students_database.csv", "r") as file:
                    reader = csv.reader(file, delimiter="\t")
                    temp_list = []
                    for row in reader:
                        temp_list.append(row)
                    if len(temp_list) == 1:
                        print("\n*** There are no students to show yet. ***")
                        return
                    else:
                        printing = "\n*** LIST OF STUDENTS IN PRIMARY SCHOOL 'PYTHON' ***"
                        print(printing)
                        for student in temp_list:
                            print("\n\t\t", student[0], student[1], student[2])
                        print("*" * len(printing))
                        email = input("\nEnter the email address of the student whose account"
                                      " you want to edit:\t").strip()
                        while email.endswith("@gmail.com") is False and email.endswith("@abv.bg") is False \
                                and email.endswith("@yahoo.com") is False and email.endswith("@hotmail.com") is False \
                                and email.endswith("@aol.com") is False and email.endswith("@live.com") is False \
                                and email.endswith("@outlook.com") is False:
                            print("\n*** Try again. ***")
                            email = input("\nEnter the email of the student whose account you want to edit:\t").strip()
                            with open("students_database.csv", "r") as file_1:
                                reader = csv.reader(file_1, delimiter="\t")
                                temp_list = []
                                for row in reader:
                                    if row[2] == email:
                                        temp_list.append(row[0])
                                        temp_list.append(row[1])
                                        temp_list.append(row[2])
                                        temp_list.append(row[3])
                                if not temp_list:
                                    print(f"\n*** A student with an email address '{email}' "
                                          f"does not exist in the database. ***")
                                    return
                                else:
                                    edited_information_list = temp_list
                                    print(f"\n****** USER INFORMATION ******\n\n\t\tFirst name: {temp_list[0]}"
                                          f"\n\t\tLast name: {temp_list[1]}\n\t\tE-mail address: {temp_list[2]}")
                                    print("*" * 30)
                                    print_edit_user_information()
                                    choice_1 = input("\nEnter a number from 1 to 5:\t")
                                    while choice_1 != "1" and choice_1 != "2" and choice_1 != "3" and choice_1 != "4"\
                                            and choice_1 != "5":
                                        print("\n*** Try again. ***")
                                        choice_1 = input("\nEnter a number from 1 to 5:\t")
                                    if choice_1 == "1":
                                        first_name = input("\nEnter new first name:\t").strip().capitalize()
                                        while first_name.isspace() or first_name.isnumeric():
                                            print("\n*** Try again. ***")
                                            first_name = input("\nEnter new name:\t").strip().capitalize()
                                        edited_information_list[0] = first_name
                                        print("\n*** First name edited successfully. ***")
                                    elif choice_1 == "2":
                                        last_name = input("\nEnter new last name:\t").strip().capitalize()
                                        while last_name.isspace() or last_name.isnumeric():
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
# няма да има втори файл за учениците, които са одобрени, а ще се местят директно от списъка за одобрение въw файла на групата




