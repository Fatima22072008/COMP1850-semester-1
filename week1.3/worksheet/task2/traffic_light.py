"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
#maxtime = int(input())  # read an integer number of steps (>0)

# Simulate the traffic light system up to time=maxtime in 1-second steps
for systime in range(41):
    if systime < 4:
        states = "red"
        print(f"Time {systime:03} State {states}")
    elif systime >= 4 and systime < 7:
        states = "red_amber"
        print(f"Time {systime:03} State {states}")
    elif systime >= 7 and systime < 12:
        states = "green"
        print(f"Time {systime:03} State {states}")
    elif systime >= 12 and systime < 15:
            states = "amber"
            print(f"Time {systime:03} State {states}")
    elif systime >= 15 and systime < 19:
            states = "red"
            print(f"Time {systime:03} State {states}")


# At the end of each step you should output the time and state using the statement on line 14