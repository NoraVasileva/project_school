from Class_People import People


class Student(People):
    """Information about students"""
    def __init__(self, first_name, last_name, email, password):
        """Entering attributes"""
        super().__init__(first_name, last_name, email, password)
        self.__group = None

    def set_group(self, new_group):
        """Edit group attribute"""
        self.__group = new_group

    def get_group(self):
        """Display group attribute"""
        return self.__group

    def __str__(self):
        """Display the information about student"""
        return f"{super().get_first_name()}"\
               f"{super().get_last_name()}" \
               f"{super().get_email()}" \
               f"{super().get_password()}"
