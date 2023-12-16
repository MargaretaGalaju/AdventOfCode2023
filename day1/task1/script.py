import re
import functools 

def getArrayFromFileInput():
    input = open("input/puzzle_input.txt")

    return input.read().splitlines()

def getArrayOfNumbersFromArrayOfStrings(arrayOfStrings):
    list = []

    for x in arrayOfStrings:
        list.append(getNumberFromString(x))
    return list

def getNumberFromString(string: str):
    separator = '' 
    integerString = separator.join(re.findall(r'\d+',string))

    if (len(integerString) < 1):
        return 0
    
    lastIndex = len(integerString)-1
    firstDigit = integerString[:1]
    lastDigit = integerString[lastIndex:]
    
    return int(firstDigit + lastDigit)

def calculateSum(arrayOfNumbers: list):
    return functools.reduce(lambda a, b: a+b, arrayOfNumbers)

print(calculateSum(getArrayOfNumbersFromArrayOfStrings(getArrayFromFileInput())))
