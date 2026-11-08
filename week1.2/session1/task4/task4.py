# Week 1.2, Session 1: Task 4
"""
here we are using different methods like intersection(), union(), add(), discard() and difference() to manipulate strings
"""
fruit = {"apple", "orange", "tomato"}
vegetables = {"leek", "tomato", "potato"}

# What do you think will be printed here? 
# the items that appear in both fruit and vegetables which it tomato
both = fruit.intersection(vegetables)
print(both)

# Why does the following code diplay five items?
# this is because it outputs everything in fruit and in vegetables
food = fruit.union(vegetables)
print(food)

# Add an item to fruit
fruit.add("cherry")
print(fruit)

# Remove an item from vegetables
vegetables.discard("leek")
print(vegetables)

# Find and display symmetric difference of the two sets
symDifference = fruit.difference(vegetables)
print(symDifference)