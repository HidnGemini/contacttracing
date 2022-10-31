from proximitychecklib import *
import PySimpleGUI as sg
#D:\Documents\python\proximity\charts
form = sg.FlexForm('Data Entry')
window = [
          [sg.Text('Please enter student name and csv folder')],
          [sg.Text('Name', size=(15, 1)), sg.InputText('')],
          [sg.Text('Folder Directory', size=(15, 1)), sg.InputText('')],
          [sg.Submit(), sg.Cancel()]
         ]
button, input = form.layout(window).Read()
studName = input[0]
fileDir = input[1]
csvs = getListOfFiles(fileDir)
finalContactList = []
for file in csvs:
    chart = (csvToArray(file))
    contactList = proximity(studName, chart)
    for item in contactList:
        finalContactList.append(item)
result = removeDoubles(finalContactList)
print(result)
