import random

# Get user to input how many random numbers they want
num = int(input("enter a number"))
# Generate this many random numbers
# Write the random numbers to a file named random.txt, one number per line
for i in range(num):
    print(random.randint(0,999))
    