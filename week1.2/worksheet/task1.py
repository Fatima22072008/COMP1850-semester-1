# Worksheet 1.2: Task 1 Solution
import sys
numberUser = int(input("enter your grade"))

print("numberUser")
if numberUser >= 70 and numberUser <= 100:
    print(f"{numberUser} is a Distinction")
elif numberUser >= 40 and numberUser <= 69:
    print(f"{numberUser} is a Pass")
elif numberUser >= 0 and numberUser <= 39:
    print(f"{numberUser} is a Fail")
elif numberUser > 100:
    sys.exit("Error: Grade must be an interger between 0 and 100")
elif numberUser < 0:
    sys.exit("Error: Grade must be an interger between 0 and 100")
else:
    sys.exit("Error: Grade must be an interger between 0 and 100")