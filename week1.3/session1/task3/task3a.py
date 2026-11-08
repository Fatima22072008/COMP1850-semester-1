# Week 1.3, Session 1: Task 3a
"""
this task uses a while loop to output numbers which arent multiple of 3 from 0 to 20
"""
i = 0 # sets the variable i as 0

while i < 20:
    i = i + 1
    if i % 3 > 0: # does i mod 3
        print(i)

# Add logic using continue so that multiples of 3 are not printed out
# Hint: we discused operators such as % and // in recent weeks

# Hint 2: there are several ways to do this - using truthy/falsey values is the least code