class Student:

    def __init__(self):
        self
    
    def __init__(self,row):
        self.name = row["Name"]
        self.gradeLevel = row['Grade Level']
        self.gender = row['Gender']
        self.eslStatus= row['ESL Status']
        self.povertyStatus = row['Above Poverty Line']
        self.gpa = row['GPA']
        self.attendance = ['Attendance (%)']
        self.behavReferrals = ['Behavior Referrals']

    