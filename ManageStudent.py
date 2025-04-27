from Student import Student
import pandas as pd

class ManageStudent:

    def __init__(self):
        self.studentsList = []

    def addStudents(self,fname):
        # read data and convert to panda data frame
        self.df = pd.read_csv(fname, sep=',', na_values=['?'])
        for index, row in self.df.iterrows():
            student = Student(row)
            self.studentsList.append(student)
        print("Succesfully added student data!")
