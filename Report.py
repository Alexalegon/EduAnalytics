class Report:
    def __init__(self,id):
        self.id = id
        self.printInfo()
        self.printReport()
    
    def printReport(self,df):
         print(df)
      
    def printInfo(self,df):
         print(df.iloc[self.id])