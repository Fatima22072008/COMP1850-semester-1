# Week 1.3, Session 1: Task 3b
"""
in this task we use len() to see wehther the list is empty or not
"""
fruit = ['apple','pear','banana','orange']

while fruit:
	print(fruit.pop())

# Add an else clause with a message that the list is now empty

if len(fruit) != 0: # checks that its not equal to 0
	print(" the list isnt empty")
else:
	print("list is empty")

