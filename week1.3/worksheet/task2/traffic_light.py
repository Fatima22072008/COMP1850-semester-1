"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input())  # read an integer number of steps (>0)
if maxtime > 0:
    numberSteps = maxtime
    state = "red"
    print(f"Time {systime:03} State {state}")
else:
    print("error")

# Simulate the traffic light system up to time=maxtime in 1-second steps
while systime <= 39:
    systime = systime + 1
    

for i in states.keys():
     while i == "red" and systime < states["red"] and systime <= maxtime:
         print(f"Time {systime:03} States {i}")
         systime = systime + 1
     else:
       print("error")

# At the end of each step you should output the time and state using the statement on line 14