# Worksheet 1.2: Task 2 Solution
from util import read_numbers

numbers = read_numbers()
print(numbers)

sortNumbers = numbers.sort()
minNumbers = min(numbers)
print(minNumbers)
maxNumbers = max(numbers)

numbersSum = sum(numbers)
numbersLength = len(numbers)
numbersMean = numbersSum / numbersLength
print(numbersMean)

