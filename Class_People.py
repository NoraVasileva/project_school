class People:
    """
    Information about students, users and teachers.
    """

    def __init__(self, first_name, last_name, email, password):
        """
        Entering attributes.
        :param first_name: user's first name
        :param last_name: user's last name
        :param email: user's e-mail address
        :param password: user's password
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    def set_first_name(self, new_name):
        """
        Edit first name attribute.
        :param new_name: user's edited first name
        """
        self.__first_name = new_name

    def get_first_name(self):
        """
        Display first name attribute.
        """
        return self.__first_name

    def set_last_name(self, new_name):
        """
        Edit last name attribute.
        :param new_name: user's edited last_name
        """
        self.__last_name = new_name

    def get_last_name(self):
        """
        Display last name attribute.
        """
        return self.__last_name

    def set_email(self, new_email):
        """
        Edit e-mail attribute.
        :param new_email: user's edited e-mail address
        """
        self.__email = new_email

    def get_email(self):
        """
        Display e-mail attribute.
        """
        return self.__email

    def set_password(self, new_password):
        """
        Edit password attribute.
        :param new_password: user's edited password
        """
        self.__password = new_password

    def get_password(self):
        """
        Display password attribute.
        """
        return self.__password
