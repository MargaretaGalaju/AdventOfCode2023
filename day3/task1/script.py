import re

PATTERN_TO_REPLACE = '^^^^^'

def findAnswerTask3():
    input = open('input.txt')
    array = input.read().splitlines()

    sumOfAllPartNumbers = 0

    for index, row in enumerate(array):
        result = mapToObjectsArray(row, index)

        for number in result:
            if isPartNumber(number, array):
                sumOfAllPartNumbers = sumOfAllPartNumbers + int(number['number'])
    print(sumOfAllPartNumbers)

def mapToObjectsArray(row, rowIndex):
    integersInArray = re.findall(r'\d+', row)
    newList = []
    duplicatedIntegers = {}

    for integer in integersInArray:
        pattern = r'(?<!\d){}(?!\d)'.format(re.escape(str(integer)))
        numberOfDuplicates = re.findall(pattern, row)
        
        if len(numberOfDuplicates) > 1:
            duplicatedIntegers[integer] = numberOfDuplicates

        if len(numberOfDuplicates) == 1:
            newRow = replacePatternToString(integer, row)
            firstIndex = len(newRow.split(PATTERN_TO_REPLACE)[0])
            lastIndex = len(integer) - 1 + firstIndex
            newList.append({
                'number': integer,
                'firstIndex': firstIndex,
                'lastIndex': lastIndex,
                'rowIndex': rowIndex
            })

    for integer in list(duplicatedIntegers.keys()):
        for index, x in enumerate(duplicatedIntegers[integer]):
            if index == 0:
                firstIndex = len(row.split(integer)[0])
                lastIndex = len(integer) - 1 + firstIndex

                newList.append({
                    'number': integer,
                    'firstIndex': firstIndex,
                    'lastIndex': lastIndex,
                    'rowIndex': rowIndex
                })
            if index == 1:
                newRow = replacePatternToString(integer, row)
                firstIndex = len(newRow.split(PATTERN_TO_REPLACE)[0])+len(integer)+len(newRow.split(PATTERN_TO_REPLACE)[1])
                lastIndex = len(integer) - 1 + firstIndex

                newList.append({
                    'number': integer,
                    'firstIndex': firstIndex,
                    'lastIndex': lastIndex,
                    'rowIndex': rowIndex
                })
    return newList

def isPartNumber(number, array):
    isPartNumber = False

    stringsToCheck = []
    
    firstPossibleIndexToCheck = number['firstIndex']-1 if number['firstIndex'] != 0 else 0
    lastPossibleIndexToCheck = number['lastIndex']+2 if number['lastIndex'] < (len(array[number['rowIndex']])-1) else (len(array[number['rowIndex']]))
    
    top = array[number['rowIndex']-1][firstPossibleIndexToCheck:lastPossibleIndexToCheck] if number['rowIndex'] > 0 else ''
    bottom = array[number['rowIndex']+1][firstPossibleIndexToCheck:lastPossibleIndexToCheck] if number['rowIndex'] < (len(array)-1) else ''
    left = array[number['rowIndex']][number['firstIndex']-1:number['firstIndex']] if number['firstIndex'] > 0 else ''
    right = array[number['rowIndex']][number['lastIndex']+1:number['lastIndex']+2] if number['lastIndex'] < (len(array[number['rowIndex']])-1) else ''
    
    stringsToCheck.append(top)
    stringsToCheck.append(bottom)
    stringsToCheck.append(left)
    stringsToCheck.append(right)

    for string in stringsToCheck:
        if isPartNumber:
            break
        if len(re.findall(r'[^.\d]', string)) > 0:
            isPartNumber = True
    
    return isPartNumber

def replacePatternToString(integer, string):    
    pattern = r'(?<!\d){}(?!\d)'.format(re.escape(str(integer)))
    return re.sub(pattern, PATTERN_TO_REPLACE, string)


findAnswerTask3()
