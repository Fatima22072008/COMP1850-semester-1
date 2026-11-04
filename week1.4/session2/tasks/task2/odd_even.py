# Week 4, Session 2: Task 2

# Given an incomplete function odd_even and a docstring.
# Your task is to complete the function based on the details
# in the docstring.


def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """
    evens = 0
    odds = 0 # sets the variables as equal to 0
    for values in lstIntegers:
        """
            increments the evnens if their modlus of 2 prodces 0 as all even numbers are divisible by 2
            otherwise increments odds
            """
        if values % 2 == 0: # does the modulus, anythin mod 2 produces 0 meaning its even 
            evens += 1
        else:
            odds += 1
    return [evens, odds]
    # Complete your code here


# Check if correct output is produced
print(odd_even([1, 2, 3, 4, 5]))  # Output: [3, 2]
