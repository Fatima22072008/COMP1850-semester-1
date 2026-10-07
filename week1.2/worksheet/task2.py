# Worksheet 1.2: Task 2 Solution
import sys

try:
    from util import read_numbers
    numbers = read_numbers()
except:
    sys.exit("Error: no numbers provided")

sortNumbers = numbers.sort()
minNumbers = min(numbers)
maxNumbers = max(numbers)

numbersSum = sum(numbers)
numbersLength = len(numbers)
numbersMean = numbersSum / numbersLength

numbersMod = numbersLength // 2
numbersOddEven = numbersLength / 2

if numbersMod == 1 and numbersLength == 2:
    numbersMedian = (minNumbers + maxNumbers) / 2
elif numbersMod == 1:
    numbersMedian = numbers[numbersMod]
else:
    Median1 = numbers[numbersMod]
    Median2 = numbers[numbersMod - 1]
    numbersMedian = (Median1 + Median2) / 2

print(f"Minimum = {minNumbers}")
print(f"Maximum = {maxNumbers}")
print(f"Mean = {numbersMean:.1f}")
print(f"Median = {numbersMedian}")