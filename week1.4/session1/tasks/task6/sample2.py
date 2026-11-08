# Week 4, Session 1: Task 3

# You are given function add_two_numbers. Your task is to inspect the code,
# and the run the program and observe the output.

"""
in this task two numbers are added together 
"""
def add_two_numbers(num1, num2): #  takes two parameters
    num1 = float(num1) #  sets it as a float
    num2 = float(num2)
    return (num1 + num2)     # What happen if you remove the parenthesis ()? doesnt make a difference
                                


# Check if the following lines produce the correct output
print(add_two_numbers(3, 4))
print(add_two_numbers(num1=3, num2=4))
print(add_two_numbers(3, num2=4))

# Why does the next line work?
print(add_two_numbers("3", "4"))
#  because their being casted as a float within the function

# What happens if you try this? Uncomment the code to find out.
print(add_two_numbers("three", "four"))
# it doesnt work cause its not an interger its a string 