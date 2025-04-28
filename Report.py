class Report:
    def __init__(self,id):
        self.ID = id
    
    def printReport(self,df):
         print(df)
      
    def printInfo(self,df):
         print(df.iloc[self.ID])