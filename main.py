from ManageTeacher import ManageTeacher;
from TeacherAnalytics import TeacherAnalytics
from TeacherReport import TeacherReport
from StudentReport import StudentReport
from ManageStudent import ManageStudent
import os
# my_package/my_class.py
class UI:
    def __init__(self):
        print()

    # def login():

    def displayMenu(self):
        print("Education Analytics Menu\nPlease Follow the Instructions on the Screen\n")
        while True:
            try:
                role = int(input("Press the following for login:\n1 for Admin\n2 for Teacher\n3 for Student\n"))

                if role == 1:
                    self.__adminUI()
                elif role == 2:
                    self.__teacherUI()
                elif role == 3:
                    self.__studentUI()
                else: raise ValueError
                # break out of the loop
                break
            except ValueError:
                print("Invalid input. Please enter 1 or 2 or 3.\n")

    def __adminUI(self):
        while True:
            try:
                task = int(input('Admin Dashboard:\n1 Add Teacher Data\n2 Add Student Data\n3 Teacher Analytics \n'))

                if task == 1:
                     manageTeacher = ManageTeacher()
                     fname = input("Enter file name: \n")
                     if os.path.exists(fname):
                        manageTeacher.addTeachers(fname)
                     else: raise NameError

                elif task == 2:
                     manageStudent = ManageStudent()
                     fname = input("Enter file name for demographic data: \n")
                     if os.path.exists(fname):
                        fname1 = input("Enter file name for peformance data\n")
                        if os.path.exists(fname1):
                            manageStudent.addStudents(fname,fname1)
                        else: raise NameError
                     else: raise NameError

                elif task == 3:
                    trainingTchr = input("Enter training data file name:\n")
                    if os.path.exists(trainingTchr):
                        testingTchr = input("Enter testing data file name:\n")
                        if os.path.exists(testingTchr):
                            tchrAnalytics = TeacherAnalytics(trainingTchr,testingTchr)
                        else: raise NameError
                    else: raise NameError
                    
                else: raise ValueError
                # break out of the loop
                break
            except ValueError:
                print("Invalid input. Please enter 1 or 2 or 3.\n")
            except NameError:
                print("File does not exist, returning to Menu")

    def __teacherUI(self):
        while True:
            try:
                task = int(input("Teacher Dashboard:\n1 View Report\n"))
                if task == 1:
                    id = int(input("Enter id: \n"))
                    teacherReport = TeacherReport(id)
                else:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 1\n")
    
    def __studentUI(self):
        while True:
            try:
                task = int(input("Student Dashboard:\n1 View Report\n"))
                if task == 1:
                    id = int(input("Enter id: \n"))
                    studentReport = StudentReport(id)
                else: raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter 1 or 2\n")  


if __name__ == "__main__":
    ui = UI()
    ui.displayMenu()