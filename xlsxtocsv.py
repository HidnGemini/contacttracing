from proximitychecklib import *

dir = 'X:\WindowsSpots\Documents\code\python\proximity/xlsxs/'

xlsxs = getListOfFiles(dir)

for item in xlsxs:
    print(item)
    xlName = item.replace(dir, '')
    csvName = xlName.replace('.xlsx', '.csv')
    print(csvName)
    csvFromExcel(item, csvName)
