# Week 1.2, Session 2: Task 4
# Simple Number Comparer

"""
in this task we are creating a number comparer which takes in two numbers from the user
and tell the user wether the first nunber is higher or wether the second number is higher 
or tell the user if their both equal
"""

# Prompt the user to enter the numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Use an if statement to compare the two numbers
if num1 > num2: 
    print("The first number is bigger.")
elif num2 > num1:  
    print("The second number is bigger.")
else:
    print("Both numbers are Equal.")
