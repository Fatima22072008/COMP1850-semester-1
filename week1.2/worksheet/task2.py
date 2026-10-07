# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

try:
    numbers = read_numbers()
except:
    sys.exit("Error!")

sortNumbers = numbers.sort()
minNumbers = min(numbers)
maxNumbers = max(numbers)

numbersSum = sum(numbers)
numbersLength = len(numbers)
numbersMean = numbersSum / numbersLength

numbersMod = numbersLength // 2
numbersMedian = numbers[numbersMod]

print(f"Minimum = {minNumbers}")
print(f"Maximum = {maxNumbers}")
print(f"Mean = {numbersMean:.1f}")
print(f"Median = {numbersMedian}")