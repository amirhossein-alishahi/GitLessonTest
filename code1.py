import csv

csvFile = open('data.csv')

csvReader = csv.DictReader(csvFile)

listOfDict = []

for item in csvReader:
    listOfDict.append(item)
    print(item)