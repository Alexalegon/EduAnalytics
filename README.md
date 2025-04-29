README

User Documentation

Installation Instructions:

This program runs on the command line using the python interpreter. Hence first we must install python on our machine by following these instructions:
1)	Install Python 3.10 or newer from python.org. 
a)	Simply navigate to www.python.org/downloads/
b)	Click on the download python button 
c)	Choose appropriate operating system version
d)	Run the exe and install python on your machine
 
Next, we download the program from the GitHub repository for the program.
2)	Download the program as a zip file from the program GitHub repository.
 
3)	Extract the folder in the desired directory.

4)	Open a command line terminal and navigate to the directory where the program is located, for example: cd   path/to /program

5)	Run the program by typing: python main.py
 

How to use the Software:
1)	Admin Role:
 
-	1 Add Teacher Data: Upload teacher demographic/performance data: Upload CSV files with US education status, age, gender, years of experience, subject, and teacher rating.
-	The filename that should be passed in is: teacherdata.csv
-	2 Add Student Data: Upload student performance data: Upload CSV files containing GPA, attendance, and discipline referrals. The demographics filename that should be passed in is: studentdemographics.csv. The performance filename that should be passed in is studentperformance.csv
-	3 Teacher Analytics: Run machine learning analyses: based on  attributes (age, gender, education status, or years of experience) and run analytics to evaluate teacher performance. Training data filename that should be passed in is: teacherdata_training.csv. Testing data filename that should be passed in id teacherdata_testing.csv

 
2)	Teacher Role:
 
-	1 View Report: View teacher information and class performance summary: shows quartiles, averages, pass rates and the averages across all classes. The id must be integer between 1 to 24.

3)	Student Role:
 
-	1 View Report: View personal performance: Log in to view own GPA, attendance, and discipline records. The id must be integer between 1 to 99.

4)	Important Notes:
-	Always input the correct CSV file names when prompted.
-	If the wrong file name or a corrupted file is entered, the system will return to the main menu with an error message.
 

