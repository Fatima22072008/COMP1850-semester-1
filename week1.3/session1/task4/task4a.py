# Week 1.3, Session 1: Task 4a
"""
in this task we're outputing the sum of squares of even number up to and including 20 using a for loop
"""
sum = 0 # sets the variable as euqal to 0

for k in range(1,20): # uses a for loop between 1 and 20
    if k % 2 == 0: # checks if k mod 2 is equal to 0
        sum = sum + k ** 2 # increments sum by k to the power of 2
print(sum)


# modify the code to sum the squares of even numbers up to and including 20

# modify the code to print the sum at each iteration