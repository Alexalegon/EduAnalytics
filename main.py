from ManageTeacher import ManageTeacher;


# my_package/my_class.py
class UI:
    def __init__(self):
        print()

    # def login():

    def displayMenu(self):
        print("Welcome Menu")
        print("Press the following for login:\n1 for Admin\n2 for Teacher\n3 for Student")
        while True:
            try:
                role = int(input("Press the following for login:\n1 for Admin\n2 for Teacher\n3 for Student\n"))
                if (role != 1 and role != 2 and role != 3):
                    raise ValueError
                elif role == 1:
                    self.__adminUI()
                elif role == 2:
                    __self.teacherUI()
                elif role == 3:
                    self.__studentUI()
                # If the input is successfully converted to an integer, break out of the loop
                break
            except ValueError:
                print("Invalid input. Please enter 1 or 2 or 3.\n")

    def __adminUI(self):
        while True:
            try:
                role = int(input("Admin Dashboard:\n1 Add Teacher Data\n2 Teacher Analytics \n3 Student Analytics\n"))
                if (role != 1 and role != 2 and role != 3):
                    raise ValueError
                elif role == 1:
                     manageTeacher = ManageTeacher()
                     manageTeacher.addTeachers(input("Enter filename: "))
                elif role == 2:
                    print()
                elif role == 3:
                    print()
                # If the input is successfully converted to an integer, break out of the loop
                break
            except ValueError:
                print("Invalid input. Please enter 1 or 2 or 3.\n")

    def __teacherUI(self):
        print()

    def __studentUI(self):
        print()


if __name__ == "__main__":
    ui = UI()
    ui.displayMenu()