# Week 1.3, Session 1: Task 4b
"""
in this task we are listing multiples of 3 between 3 and 50
"""

for k in range(2,49): # loops through values of k between 3 and 50
  k = k + 1  # increments k by one
  if k % 3 == 0:
    print(k)

# create a for loop and use range to print the list of numbers 
# between 3 and 50 that are divisible by 3