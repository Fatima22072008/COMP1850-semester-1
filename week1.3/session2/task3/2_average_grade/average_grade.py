# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open 'student_data.csv' to read each student's grades
# hint: skip the header row with data[1:]

with open("student_data.csv", "r") as infile:
    readFile = infile.read()
    value = readFile.split()
    value = value[1:]
    for x in value:
        print(x)
        maths = int(value[3])
        science = int(value[4])
        history = int(value[5])
        average = (maths + science + history)/3
        

# Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3
ReportFile = open("report.txt")


# Open a file called 'report.txt'
# Write each student's name and their average grade to the report
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
