# Week 1.3, Session 1: Task 1a
"""
In this tasks we use a while loop to print numbers up to and including 20
"""
i = 0 # setting the variable i as equal to 0

while i < 21:
	i = i + 1 # increments i by one
	if i % 4 == 0: # does the modulus of values of i and then output the ones which are divisible by 4 with no remainders
		print(i)
# Modify the loop to print numbers up to and including 20

# Add further logic so that a message is printed if the number is a multiple of 4
# Hint: we discused operators such as % and // in recent weeks