# Week 1.3, Session 1: Task 5a
"""
here in this task it lists the character in a string into an alphabetical order
"""

course = "computer science"
courseList = list(course) # sets the strings as a list
courseList.sort() # sorts the list alphabetically
for ch in courseList: # loops through the charaters in the variable
	print(ch)


# create a list data structure of the characters from the course string
# sort the list into alphabetical order