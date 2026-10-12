"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
# maxtime = int(input())  # read an integer number of steps (>0)

# Simulate the traffic light system up to time=maxtime in 1-second steps
for x in states:
    state = "red"
    print(f"Time {systime:03} State {state}")
    systime = systime + 1

for x in states:
    state = "red_amber"
    systime = systime + 1
    print(f"Time {systime:03} State {state}")

# for i in states.keys():
   #  while i == "red" and systime < states["red"] and systime <= maxtime:
       #  print(f"Time {systime:03} States {i}")
        # systime = systime + 1

# At the end of each step you should output the time and state using the statement on line 14