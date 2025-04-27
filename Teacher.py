class Teacher:
    def __init__(self,row):
        self.name = row["Name"]
        self.age = row['Age']
        self.gender = row['Gender']
        self.usEducated = row['US Educated']
        self.yrsExp = row['Years Experience']
        self.subject = row['Subject']
        self.rating = row['Teacher Rating']

