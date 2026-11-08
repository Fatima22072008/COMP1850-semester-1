# Week 1.2, Session 1: Task 1
"""
in this task we create a list an use methods such as .append() which adds something ot the list and udes .remove()
to remove something from the list. To replace something in the list with another item you can simiply do it by making
use of the lists index. You can use .insert() in order to place something into the list and chose what postion it's
inserted into
"""
# Create a shopping list
shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list
shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list
shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
shopping[3] = "grapes"

# Add yoghurt, just after milk
shopping.insert(0, "yoghurt")

print(shopping)