# Week 1.3, Session 1: Task 2b
"""
this program repeats any string that is enterned but has a break
condition whihc allows the user to stop the program
"""
print("This program will repeat everything you type.")
print("To exit the program type quit")

while True:
    user_input = input("Say something: ")
    if user_input == "quit":
            break # this is the break statement
    else:
        print(f"You said: {user_input}")

# As written the program has an infinite loop.
# Add a break statement so that if the user types 'quit' the program exits.