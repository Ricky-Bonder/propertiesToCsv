#!/usr/bin/python

import csv
import pandas
from itertools import chain
import configparser


languages = ['ENGLISH', 'ITALIANO', 'DEUTSCH', 'FRANÇAIS', 'ESPAÑOL']
files = ['root', 'cagepreparation', 'changepartialscreen', 'changetotalscreen', 'notification', 'reader', 'settings']

keyProperty = list()
valueProperty = list()

rowCompleteEnglish = list()
rowCompleteItalian = list()
rowCompleteGerman = list()
rowCompleteFrench = list()
rowCompleteSpanish = list()

englishValuesFinal = list()

with open('/home/rossola/VSCodeProjects/propertiesToCsv/properties.csv', 'rb') as csvFile:
    reader = pandas.read_csv(csvFile)
    ofFileColumn = reader.iloc[:, 6]
    ofFileName = ofFileColumn.values
    print(ofFileName)

    firstColumn = reader.iloc[:, 0]
    keyProperty = firstColumn.values
    print(keyProperty)

    for column in range(1, 6):
        valuesColumn = reader.iloc[:, column]
        valueProperty = valuesColumn.values
        print("@@",valueProperty)
        if column == 1:
            rowCompleteEnglish = list(zip(keyProperty, valueProperty, ofFileName))
        elif column == 2:
            rowCompleteItalian = list(zip(keyProperty, valueProperty, ofFileName))
        elif column == 3:
            rowCompleteGerman = list(zip(keyProperty, valueProperty, ofFileName))            
        elif column == 4:
            rowCompleteFrench = list(zip(keyProperty, valueProperty, ofFileName))
        elif column == 5:
            rowCompleteSpanish = list(zip(keyProperty, valueProperty, ofFileName))
        
    for file in files:
        for entry in rowCompleteEnglish:
            if file == entry[2]:
                entry = list(entry)
                entry.pop(2)
                print("file: ", file, " - put: ", entry)
                entry = tuple(entry)
                mapped = '='.join(entry)
                mapped = mapped+"\n"
                englishValuesFinal.append(mapped)
                print(englishValuesFinal)
                with open('/home/rossola/VSCodeProjects/propertiesToCsv/english/'+file+'_en.properties', 'w+') as configfile:
                    configfile.writelines(englishValuesFinal)
        

        
    
    