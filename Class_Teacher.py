from Class_People import People


class Teacher(People):
    """Information about teachers"""
    def __init__(self, **kwargs):
        """Entering attributes"""
        super().__init__(first_name=kwargs["first_name"], last_name=kwargs["last_name"],
                         email=kwargs["email"], password=kwargs["password"])
        self.__group = list(kwargs["group"])
        self.__date_of_birth = kwargs["date_of_birth"]
        self.__month_of_birth = kwargs["month_of_birth"]
        self.__year_of_birth = kwargs["year_of_birth"]
        self.__first_day_of_work = kwargs["first_day_of_work"]
        self.__first_month_of_work = kwargs["first_month_of_work"]
        self.__first_year_of_work = kwargs["first_year_of_work"]

    def add_group(self, group):
        """Add group into list"""
        self.__group.append(group)

    def delete_group(self, group):
        """Delete group from the list"""
        try:
            self.__group.remove(group)
        except:
            print("This group doesn't exist.")

    def get_group(self):
        """Display group list"""
        return self.__group

    def set_date_of_birth(self, new_date):
        """Edit date of birth attribute"""
        self.__date_of_birth = new_date

    def get_date_of_birth(self):
        """Display date of birth attribute"""
        return self.__date_of_birth

    def set_month_of_birth(self, new_month):
        """Edit month of birth attribute"""
        self.__month_of_birth = new_month

    def get_month_of_birth(self):
        """Display month of birth attribute"""
        return self.__month_of_birth

    def set_year_of_birth(self, new_year):
        """Edit year of birth attribute"""
        self.__year_of_birth = new_year

    def get_year_of_birth(self):
        """Display year of birth attribute"""
        return self.__year_of_birth

    def set_first_day_of_work(self, new_day):
        """Edit first day of work attribute"""
        self.__first_day_of_work = new_day

    def get_first_day_of_work(self):
        """Display first day of work attribute"""
        return self.__first_day_of_work

    def set_first_month_of_work(self, new_month):
        """Edit first month of work attribute"""
        self.__first_month_of_work = new_month

    def get_first_month_of_work(self):
        """Display first month of work attribute"""
        return self.__first_month_of_work

    def set_first_year_of_work(self, new_year):
        """Edit first year of work attribute"""
        self.__first_year_of_work = new_year

    def get_first_year_of_work(self):
        """Display first year of work attribute"""
        return self.__first_year_of_work

    def __str__(self):
        """Display the information about teacher"""
        return f"First name: {super().get_first_name()}," \
               f"Last name: {super().get_last_name()}, Group: {self.__group}"

