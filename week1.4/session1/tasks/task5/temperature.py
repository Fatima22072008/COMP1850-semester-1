# Week 4, Session 1: 

# To convert a temperature from Celsius to Fahrenheit. 
# There are two main tasks involved:
#   (1) validating the temperature 
#   (2) converting Celsius to Fahrenheit.

# These are now defined in a separate function.

# Given the two functions and the following code to get the temperature
# from a user, complete the rest of the program to use these functions to
# print the temperature in Fahrenheit if the temperature from the user
# is within the range, otherwise print "The temperature is out of range."

"""
In this task it cheks the temeprature is in a vlaid range and converts it from celsisus
to farhrenheit
"""
def valid_temperature(temperature):
    if temperature >= -100 and temperature <= 100:
        # checks if temp is in valid range
        return True
    else:
        return False


def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    #  conversion of celsisu to farenheight 
    return fahrenheit


# test the functions
# Complete the rest of the code here
celsius = float(input("Enter temperature in Celsius: "))

if valid_temperature(celsius) == True:
    print(celsius_to_fahrenheit(celsius))
else:
    print("your temp isnt real")
