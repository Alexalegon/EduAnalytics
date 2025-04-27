class Student:
    
    def __init__(self,row):
        self.name = row["Name"]
        self.age = row['Grade Level']
        self.gender = row['Gender']
        self.usEducated = row['ESL Status']
        self.yrsExp = row['Above Poverty Line']

    