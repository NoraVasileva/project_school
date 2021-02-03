from Project_2_test.Function_first_menu import first_menu
from Project_2_test.Login.Login_functions import login
from Project_2_test.Registration.Registration_functions import registration

if __name__ == '__main__':
    while True:
        first_menu()
        choice = input("Enter a number from 1 to 3:\t").strip()
        print("")
        while choice != "1" and choice != "2" and choice != "3":
            print("*** Sorry, we don't have this option. ***")
            print("")
            first_menu()
            choice = input("Enter a number from 1 to 3:\t").strip()
            print("")
        if choice == "1":
            print("")
            login()
        elif choice == "2":
            print("")
            registration()
        elif choice == "3":
            print("*** Thank you for visiting our site. Have a nice day! ***")
            break

# TODO: на всички def който пиша трябва да им пиша обяснение в """""
# TODO: следващия път да обсъдим с Милена как се работи по-подробно в командния ред - пример: базовите файлове
# да се вкарат в конфигурацията (да са създадени предварително файловете и да правим проверка дали съществуват в main файла)
# и се изтриват проверките от файла Class_School.
# TODO: Като завърша проекта да научим с Милена виртуалните среди