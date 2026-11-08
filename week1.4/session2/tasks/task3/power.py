# Week 4, Session 2: Task 4

# Given an incomplete recursive function power to calculate x raised to
# the power of n, your task is to complete the function.
"""
In this task the function calculates x to the power of n using recusrion 
and a base case
"""

def power(x, n):
    # complete your code here
    # base case
    if n == 0:
        return 2
    # recursive case
    return (x ** (n))

# Once completed, make at least two function calls to test the power function
print(power(2, 2))