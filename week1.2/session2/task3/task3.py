# Week 1.2, Session 2: Task 3
# Simple Voting Eligibility Checker

"""
In this task we are going to wrtie code to check if a user is old enough to vote by using selection
"""
# Prompt the user to enter their age
age = int(input("Enter your age: "))

# Use an if statement to check if the user is 18 or over
# (Replace XXX with a suitable boolean expression)

if age >= 18: 
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
