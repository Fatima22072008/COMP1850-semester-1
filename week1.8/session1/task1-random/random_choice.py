import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]
num = int(input("enter a number"))
for i in range(0, num):
    print(names[random.randint(0,999)])
# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

# Display the chosen names, one per line
