# Week 1.3, Session 2: Word Counter

# We want to read in a text file, and calculate how many words are in it. 
# You can use any of the .txt files to test this - or even make your own.
"""
In this task we are going to read a textfile line by line and remove the empty spaces 
between the data and print the number of words
"""
# open and read the file
filename = input("enter the file name")
with open(filename, "r") as infile:
    insidefile = infile.read() # reads the data line by line

numWords = insidefile.split() # removes the empty space in the data
print(len(numWords))


# calculate the number of words
# hint: you could use .split() to break up by spaces
# hint: watch out for empty lines that might give you empty strings

# display the wordcount

# Here are the word counts you should get:
# story.txt - 290
# story2.txt - 326
# glasses.txt - 210