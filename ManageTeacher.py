import pandas as pd
from Teacher import Teacher

class ManageTeacher:

    def __init__(self):
        self.teacherList = []

    def addTeachers(self,fname):
        # read data and convert to panda data frame
        self.df = pd.read_csv(fname, sep=',', na_values=['?'])
        for index, row in self.df.iterrows():
            teacher = Teacher(row)
            self.teacherList.append(teacher)
        print("Succesfully added teacher data!")

    """ def removeTeacher(self,name):
        for item in self.teacherList:
            if item.name == name:
                self.teacherList.remove(item) """