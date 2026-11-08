"""
    this program takes a file which contains students IDs and the hours late that work was submitted
    it needs to convert the minutes late into days, hours and minutes
    all file handling has been done - the section you need to edit is marked by comments below
"""

with open("_data/lateness_data.csv") as f: # allows us to open the file and call it a variable
    data = f.readlines() # allows us to read the file 

data = [line.strip().split(",") for line in data] 
# strip goes through and gets rid of the empty space
# split seperates the words 

for row in data: # allows us to iterate



    # minutes_late is the number of minutes late a submission was made
    minutes_late = int(row[1])

    # for each of these, we need to work out how to turn 'minutes_late' into the right value
    # for example: if minutes_late is 2000, then days = 1, hours = 9, minutes = 20
    # hint: there are 1440 minutes in a day (24 * 60)
    
    days = 0
    hours = 0
    minutes = 0
    """
    here were calculating from days to hours to minutes 
    """
    days = minutes_late // 1440
    minutes_late = minutes_late - (1440 * days)
    hours = minutes_late // 60
    minutes_late = minutes_late - (60 * hours)
    minutes = minutes_late
    print(f"Student {row[0]}: {days}D {hours}H {minutes}M")

