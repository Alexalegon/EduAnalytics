from Student import Student
import pandas as pd

class ManageStudent:

    def __init__(self):
        self.studentsList = []

    def addStudents(self,demographFile,performFile):
        # read data and convert to panda data frame
        self.df = pd.read_csv(demographFile, sep=',', na_values=['?'])
        self.df1 = pd.read_csv(performFile, sep=',', na_values=['?'])
        self.merged_df = pd.merge(self.df, self.df1, on='Name')
        for index, row in self.merged_df.iterrows():
            student = Student(row)
            self.studentsList.append(student)
        print("Succesfully added student data!")
