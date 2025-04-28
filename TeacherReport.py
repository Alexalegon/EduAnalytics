import pandas as pd
from Report import Report

class TeacherReport(Report):
     def __init__(self, id):
        super().__init__(id)
        self.dfReport = pd.read_csv("teacherreport.csv", sep=',', na_values=['?'])
        self.dfInfo= pd.read_csv("teacherdata.csv", sep=',', na_values=['?'])
        self.printInfo(self.dfInfo)
        self.printReport(self.dfReport)
        
      