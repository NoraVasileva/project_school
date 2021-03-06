def print_first_menu():
    """
    Printing menu for registration, login and quit.
    1: Log in; 2: Register; 3: Quit
    """
    print("\n******* PRIMARY SCHOOL 'PYTHON' *******\n\nOPTIONS:\n\n# 1: Log in\n\n# 2: Register\
            \n\n# 3: Quit\n\n*************************************")


def print_registration():
    """
    Printing registration form with options.
    1: Student; 2: Teacher; 3: Quit
    """
    print("\n******* Please fill in the registration form ******"
          "\n"
          "\nChoose a number from 1 to 3 from the below options:"
          "\n"
          "\n# 1: Student\n\n# 2: Teacher\n\n# 3: Quit\n"
          "\n****************************************************")


def print_login():
    """
    Printing login form with options.
    1: Student; 2: Teacher; 3: Administrator; 4: Quit
    """
    print("*********** Please fill in the login form **********"
          "\n"
          "\nChoose a number from 1 to 4 from the below options:"
          "\n"
          "\n# 1: Student\n\n# 2: Teacher\n\n# 3: Administrator\n\n# 4: Quit\n"
          "*****************************************************")


def print_teacher_options():
    """
    Printing teacher's menu with options.
    1: Show all study classes; 2: Show all teachers; 3: Quit
    """
    print("\n******************* TEACHER'S MENU *****************"
          "\n\nChoose a number from 1 to 3 from the below options:"
          "\n\n# 1: Show all study classes\n\n# 2: Show all teachers\n\n# 3: Quit"
          "\n\n****************************************************")


def print_admin_options():
    """
    Printing administrator's menu with options.
    1: Users management; 2: Class management; 3: School information; 4: Quit
    """
    print("\n******************* ADMINISTRATOR'S MENU *****************"
          "\n\nChoose a number from 1 to 4 from the below options:"
          "\n\n# 1: Users management\n\n# 2: Class management\n\n# 3: School information\n\n# 4: Quit"
          "\n**********************************************************")


def print_users_management():
    """
    Printing users management menu with options for the administrator.
    1: Registrations; 2: User accounts; 3: Quit
    """
    print("\n******************* USERS MANAGEMENT *****************"
          "\n\nChoose a number from 1 to 3 from the below options:"
          "\n\n# 1: Registrations\n\n# 2: User accounts\n\n# 3: Quit"
          "\n\n****************************************************")


def print_user_accounts():
    """
    Printing user accounts menu with options for the administrator.
    1: Show users; 2: Edit user; 3: Delete user; 4: Quit
    """
    print("\n******************* USERS ACCOUNTS *****************"
          "\n\nChoose a number from 1 to 4 from the below options:"
          "\n\n# 1: Show users\n\n# 2: Edit user \n\n# 3: Delete user\n\n# 4: Quit"
          "\n\n****************************************************")


def print_show_users():
    """
    Printing user accounts menu with options for the administrator.
    1: Show users; 2: Show students; 3: Show teachers; 4: Quit
    """
    print("\n******************* USERS ACCOUNTS *****************"
          "\n\nChoose a number from 1 to 4 from the below options:"
          "\n\n# 1: Show users\n\n# 2: Show students\n\n# 3: Show teachers\n\n# 4: Quit"
          "\n\n****************************************************")


def print_registrations():
    """
    Printing menu with registrations for approval with options for the administrator.
    1: Student registrations; 2: Teacher registrations; 3: Quit
    """
    print("\n******************* REGISTRATIONS *****************"
          "\n\nChoose a number from 1 to 3 from the below options:"
          "\n\n# 1: Student registrations\n\n# 2: Teacher registrations\n\n# 3: Quit"
          "\n\n**************************************************")


def print_edit_user():
    """
    Printing menu with options about editing user's accounts for the administrator.
    1: Edit student's account; 2: Edit teacher's account; 3: Edit user's account; 4: Quit
    """
    print("\n***************** ACCOUNT EDITING ****************"
          "\n\nChoose a number from 1 to 4 from the below options:"
          "\n\n# 1: Edit student's account\n\n# 2: Edit teacher's account"
          "\n\n# 3: Edit user's account\n\n# 4: Quit"
          "\n\n**************************************************")


def print_edit_user_information():
    """
    Printing menu with options about editing user's information for the administrator.
    1: Edit first name; 2: Edit last name; 3: Edit e-mail address; 4: Edit password; 5: Quit
    """
    print("\n***************** ACCOUNT EDITING ****************"
          "\n\nChoose a number from 1 to 5 from the below options:"
          "\n\n# 1: Edit first name\n\n# 2: Edit last name"
          "\n\n# 3: Edit e-mail address\n\n# 4: Edit password \n\n# 5: Quit"
          "\n\n**************************************************")


def print_user_options():
    """
    Printing user's menu with options.
    1: Show all teachers; 2: Quit
    """
    print("\n******************* USER'S MENU *****************"
          "\n\nChoose a number from 1 to 2 from the below options:"
          "\n\n# 1: Show all teachers\n\n# 2: Quit"
          "\n*************************************************")


def print_reg_1():
    """
    Printing information on existing registration.
    """
    print("\n*** You already have a registration! Please login. ***")


def print_reg_2():
    """
    Printing of information regarding the requested registration.
    """
    print("\n*** Your registration was already submitted for approval! ***")
    print("\n*** If your registration is not approved within 24 hours, "
          "you will have user status only ***")
    print("\n*** Use login option. ***")


def print_reg_3():
    """
    Printing of information about new registration.
    """
    print("\n*** Your registration was successfully submitted for approval! ***")
    print("\n*** If your registration is not approved within 24 hours, "
          "you will have user status only ***")
    print("\n*** You can now login. ***")


def print_reg_4():
    """
    Printing options for approving or rejecting registrations.
    1: Approve; 2: Reject; 3: Quit
    """
    print("\n\nDo you want to approve or reject a registration?"
          "\n\nChoose a number from 1 to 3 from the below options:"
          "\n\n# 1: Approve\n\n# 2: Reject\n\n# 3: Quit"
          "\n\n*********************************************************")


def print_no_students():
    """
    Printing information that there are no students.
    """
    print("\n*** There are no students to show yet. ***")


def print_no_teachers():
    """
    Printing information that there are no teachers.
    """
    print("\n*** There are no teachers to show yet. ***")


def print_teacher_information():
    """
    Printing menu with options about editing teachers's information for the administrator.
    1: Edit first name; 2: Edit last name; 3: Edit e-mail address; 4: Edit password; 5: Edit study classes
    6: Edit birth"; 7: Edit work experience; 8: Quit"
    """
    print("\n***************** ACCOUNT EDITING ****************"
          "\n\nChoose a number from 1 to 8 from the below options:"
          "\n\n# 1: Edit first name\n\n# 2: Edit last name"
          "\n\n# 3: Edit e-mail address\n\n# 4: Edit password"
          "\n\n# 5: Edit study classes\n\n# 6: Edit birth"
          "\n\n# 7: Edit work experience\n\n# 8: Quit"
          "\n\n**************************************************")


def print_edit_info():
    """
    Printing menu with options about editing user's information for the administrator.
    1: Edit students information; 2: Edit teachers information; 3: Edit users information; 4: Quit"
    """
    print("\n***************** ACCOUNT EDITING ****************"
          "\n\nChoose a number from 1 to 4 from the below options:"
          "\n\n# 1: Edit students information\n\n# 2: Edit teachers information"
          "\n\n# 3: Edit users information\n\n# 4: Quit"
          "\n\n**************************************")


def print_delete_account():
    """
    Printing menu with options about deleting user's information for the administrator.
    1: Delete students information; 2: Delete teachers information; 3: Delete users information; 4: Quit"
    """
    print("\n***************** ACCOUNT EDITING ****************"
          "\n\nChoose a number from 1 to 4 from the below options:"
          "\n\n# 1: Delete students information\n\n# 2: Delete teachers information"
          "\n\n# 3: Delete users information\n\n# 4: Quit"
          "\n\n**************************************")


def print_class_menu():
    """
    Printing menu with options about study classes for the administrator.
    1: Show all study classes; 2: Create new study class; 3: Edit study class name; 4: Delete study class; 5: Quit"
    """
    print("\n*********** INFORMATION ABOUT STUDY CLASSES *********"
          "\n"
          "\nChoose a number from 1 to 5 from the below options:"
          "\n"
          "\n# 1: Show all study classes\n\n# 2: Create new study class\n\n# 3: Edit study class name"
          "\n\n# 4: Delete study class\n\n# 5: Quit"
          "\n*****************************************************")


def school_information():
    """
    Printing menu with options about the school for the administrator.
    1:  Number of students by groups; 2: Age and years of experience; 3: Quit"
    """
    print("\n*********** INFORMATION ABOUT PRIMARY SCHOOL 'PYTHON' *********"
          "\n"
          "\nChoose a number from 1 to 3 from the below options:"
          "\n# 1: Showing the number of students by groups\n\n# 2: Showing the age and years "
          "of experience of the teachers\n\n# 3: Quit"
          "\n*****************************************************")
