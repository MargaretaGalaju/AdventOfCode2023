import re
import functools 

daysDictionary = {
    "one" : "1",
    "two" : "2",
    "three" : "3",
    "four" : "4",
    "five" : "5",
    "six" : "6",
    "seven" : "7",
    "eight" : "8",
    "nine" : "9",
}


def getArrayFromFileInput():
    input = open("input/puzzle_input.txt")

    return input.read().splitlines()

def getArrayOfNumbersFromArrayOfStrings(arrayOfStrings):
    list = []

    for x in arrayOfStrings:
        list.append(getNumberFromString(x))
    return list

# def getNumberFromString(string: str):
#     separator = ''
#     integerString = separator.join(re.findall(r'\d+',string))

#     if (len(integerString) < 1):
#         return 0
    
#     lastIndex = len(integerString)-1
#     firstDigit = integerString[:1]
#     lastDigit = integerString[lastIndex:]
    
#     return int(firstDigit + lastDigit)


def getNumberFromString(string):
    arrayOfAllDigitsAndString = re.findall(r'one|two|three|four|five|six|seven|eight|nine|\d+', string)
    firstMatch = arrayOfAllDigitsAndString[0]

    arrayOfAllDigitsAndString2 = re.findall(r'enin|thgie|neves|xis|evif|ruof|eerht|owt|eno|\d+', string[::-1])
    lastMatch = arrayOfAllDigitsAndString2[0][::-1]

    firstDigit = firstMatch if daysDictionary.get(firstMatch) == None else daysDictionary.get(firstMatch)
    lastDigit = lastMatch if daysDictionary.get(lastMatch) == None else daysDictionary.get(lastMatch)

    if len(firstDigit) > 1:
        firstDigit = firstDigit[:1]
    
    if len(lastDigit) > 1:
        lastIndex = len((lastDigit))-1
        lastDigit = lastDigit[lastIndex:]

    return int(firstDigit + lastDigit)

def calculateSum(arrayOfNumbers: list):
    return functools.reduce(lambda a, b: a+b, arrayOfNumbers)

print(calculateSum(getArrayOfNumbersFromArrayOfStrings(getArrayFromFileInput())))