import re
import functools 

maxLimits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

######## Task 1

def isTheGameImpossible(colorString):
    string = colorString.strip().split(' ')
    quantity = int(string[0].strip())
    color = string[1].strip()

    return quantity > maxLimits[color]

def mapToPossibleGames(string):
    gameIsImpossible = False
    arrayOfString = list(map(lambda x: x.split(','), string.split(':')[1].split(';')))
   
    for x in arrayOfString:
        if gameIsImpossible:
            break

        for color in x:
            if gameIsImpossible:
                break
            
            gameIsImpossible = isTheGameImpossible(color)
    return not gameIsImpossible


def calculateSumOfPossibleGameIndexes(array):
    sum = 0
    for index, game in enumerate(array):
        if game:
            sum = sum + index + 1
    return sum


def findAnswerTask1():
    input = open('input.txt')
    array = input.read().splitlines()
    possibleGames = list(map(mapToPossibleGames, array))
    result = calculateSumOfPossibleGameIndexes(possibleGames)
    print(result)


######## Task 2

def mapToMinSetOfCubesObject(string):
    object = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    arrayOfString = list(map(lambda x: x.split(','), string.split(':')[1].split(';')))
   
    for x in arrayOfString:
        for colorString in x:
            string = colorString.strip().split(' ')
            quantity = int(string[0].strip())
            color = string[1].strip()
            if quantity > object[color]:
                object[color] = quantity
    
    return object

def mapToPower(set):
    values = list(set.values())
    return functools.reduce(lambda a, b: a*b, values)

def calculateSum(arrayOfNumbers: list):
    return functools.reduce(lambda a, b: a+b, arrayOfNumbers)

def findAnswerTask2():
    input = open('input.txt')
    array = input.read().splitlines()
    minSetOfCubesArray = list(map(mapToMinSetOfCubesObject, array))
    arrayOfPowers = list(map(mapToPower, minSetOfCubesArray))
    result = calculateSum(arrayOfPowers)
    print(result)


findAnswerTask1()

findAnswerTask2()