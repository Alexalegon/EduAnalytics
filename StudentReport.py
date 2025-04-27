from Report import Report
import pandas as pd
class StudentReport(Report):

    def __init__(self, id):
        self.id = id
        self.dfReport = pd.read_csv("studentrecords.csv", sep=',', na_values=['?'])
        self.dfInfo= pd.read_csv("studentinfo.csv", sep=',', na_values=['?'])
        self.record = self.dfReport.iloc[id]
        self.printInfo(self.dfInfo)
        self.printReport(self.record)