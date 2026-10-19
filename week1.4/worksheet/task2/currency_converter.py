
"""
    Portfolio Task - Week 4

    By submitting this code you are declaring that all work in this file,
    other than any provided template code, was written and developed by
    you independently.

    Name:
"""

def currency_converter(amount, from_currency, to_currency):

    conversion_rate = {
        'GBP': {'CNY': 9.24, 'PHP': 75.00, 'INR': 109.06},
        'CNY': {'GBP': 0.11, 'PHP': 8.12, 'INR': 11.81},
        'PHP': {'CNY': 0.12, 'GBP': 0.01, 'INR': 1.45},
        'INR': {'PHP': 0.69, 'CNY': 0.09, 'GBP': 0.01}
    }
    
    # your code here
    return conversion_rate


amount = float(input("enter a vlaue"))
from_currency = input("enter the currency code of your ammount")
to_currency = input("the currency code of currency you want to conver to")
dictionary = currency_converter(amount, from_currency, to_currency)
ConvertedAmount =  amount * (dictionary[from_currency][to_currency])
print(ConvertedAmount)

# Submit only this file currency_converter.py with the completed function.

# for from_currency in conversion_rate:
      #  values = to_currency.get()
      #  ConvertedAmount = amount * values
# Remove any additional code you may have added during development and testing.
