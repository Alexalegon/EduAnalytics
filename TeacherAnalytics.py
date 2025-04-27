from Analytics import Analytics
import pandas as pd

class TeacherAnalytics(Analytics):
    def __init__(self,trainingFname,testingFname):
        super().__init__()
        # read data and convert to panda data frame
        self.df = pd.read_csv(trainingFname, sep=',', na_values=['?'])
        self.df_test = pd.read_csv(testingFname, sep=",", na_values=['?'])
        print(self.df)

