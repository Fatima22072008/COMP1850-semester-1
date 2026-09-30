"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.


monthly_savings = int(input(" What is the amount you want to save every month in pounds?"))
if type(monthly_savings) != int:
    print("please enter an interger / number")
else:
    print("valid input")

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
# print this out for the user with a suitable message.

yearly_savings = monthly_savings * 12
print(f"This is how much money you will save per month £{yearly_savings:.2f}")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
# print this out in the format £X.XX (to two decimal places).

interest_amount = yearly_savings * 0.008
final_amount = interest_amount + yearly_savings
print(f"£{final_amount:.2f}")
