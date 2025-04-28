from Report import Report
import pandas as pd
class StudentReport(Report):

    def __init__(self, id):
        super().__init__(id)
        self.dfReport = pd.read_csv("studentperformance.csv", sep=',', na_values=['?'])
        self.dfInfo= pd.read_csv("studentdemographics.csv", sep=',', na_values=['?'])
        self.record = self.dfReport.iloc[id]
        self.printInfo(self.dfInfo)
        self.printReport(self.record)