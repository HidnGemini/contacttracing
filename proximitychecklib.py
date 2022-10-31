def csvToArray(inputCsv):
    import csv
    with open(inputCsv, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def getListOfFiles(dirName):
    import os
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles

def proximity(name, inputList):
    proximityList = []
    xVal = 'null'
    yVal = 'null'
    for i in range(len(inputList)):
        for j in range(len(inputList[0])):
            try:
                if inputList[i][j].lower() == name.lower():
                    xVal = i
                    yVal = j
                    break
            except IndexError:
                null = 'null'
    if xVal != 'null':
        for i in range(3):
            for j in range(3):
                xMod = i-1
                yMod = j-1
                try:
                    if xMod+xVal == abs(xMod+xVal) and yMod+yVal == abs(yMod+yVal):
                        proximityList.append(f'{inputList[xMod+xVal][yMod+yVal]}')
                except IndexError:
                    null = 'null'
    for item in proximityList:
        if item == '':
            proximityList.remove(item)
    return proximityList

def removeDoubles(inputList):
    inputList = list(dict.fromkeys(inputList))
    return inputList

def csvFromExcel(spreadsheet, filename):
    import pandas as pd

    read_file = pd.read_excel (spreadsheet)
    read_file.to_csv (('X:/WindowsSpots/Documents/code/python/proximity/xlsxs/' + filename), index = None, header=False)


if __name__ == '__main__':
    csvs = getListOfFiles('X:\WindowsSpots\Documents\code\python\proximity\charttest')
    print(csvs)
    finalContactList = []
    for file in csvs:
        print(file)
        chart = (csvToArray(file))
        contactList = proximity('Adam Stephens', chart)
        for item in contactList:
            finalContactList.append(item)
    result = removeDoubles(finalContactList)
    print(result)
