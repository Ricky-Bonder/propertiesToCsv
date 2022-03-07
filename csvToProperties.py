#!/usr/bin/python

import csv
import pandas
from itertools import chain
import configparser
from pathlib import Path



languages = ['english', 'italian', 'german', 'french', 'spanish']
files = ['cagepreparation', 'changepartialscreen', 'changetotalscreen', 'notification', 'reader', 'settings']

keyProperty = list()
valueProperty = list()

rowCompleteEnglish = list()
rowCompleteItalian = list()
rowCompleteGerman = list()
rowCompleteFrench = list()
rowCompleteSpanish = list()

rowsCompleteList = [rowCompleteEnglish, rowCompleteItalian, rowCompleteGerman, rowCompleteFrench, rowCompleteSpanish]

englishValuesFinal = list()
italianValuesFinal = list()
germanValuesFinal = list()
frenchValuesFinal = list()
spanishValuesFinal = list()

languagesValuesFinal = [englishValuesFinal, italianValuesFinal, germanValuesFinal, frenchValuesFinal, spanishValuesFinal]
countryCodeList = ['en', 'it', 'de', 'fr', 'es']

with open('/home/rossola/VSCodeProjects/propertiesToCsv/properties.csv', 'rb') as csvFile:
    reader = pandas.read_csv(csvFile)
    ofFileColumn = reader.iloc[:, 6]
    ofFileName = ofFileColumn.values

    firstColumn = reader.iloc[:, 0]
    keyProperty = firstColumn.values

    for column in range(1, 6):
        valuesColumn = reader.iloc[:, column]
        valueProperty = valuesColumn.values
        print("language ",column, "values: ",valueProperty)
        if column == 1:
            rowsCompleteList[0] = list(zip(keyProperty, valueProperty, ofFileName))
        elif column == 2:
            rowsCompleteList[1] = list(zip(keyProperty, valueProperty, ofFileName))
        elif column == 3:
            rowsCompleteList[2] = list(zip(keyProperty, valueProperty, ofFileName))            
        elif column == 4:
            rowsCompleteList[3] = list(zip(keyProperty, valueProperty, ofFileName))
        elif column == 5:
            rowsCompleteList[4] = list(zip(keyProperty, valueProperty, ofFileName))
    

    for language in range(0, 5):
        Path(languages[language]).mkdir(parents=True, exist_ok=True)
        for file in files:
            languagesValuesFinal[language].clear()
            for entry in rowsCompleteList[language]:
                if file == entry[2]:
                    entry = list(entry)
                    entry.pop(2)
                    print("file: ", file, " - put: ", entry)
                    entry = tuple(entry)
                    mapped = '='.join(entry)
                    mapped = mapped+"\n"
                    languagesValuesFinal[language].append(mapped)
                    # print("final file content: ", languagesValuesFinal[language])
                    with open('/home/rossola/VSCodeProjects/propertiesToCsv/'+languages[language]+'/'+file+'_'+countryCodeList[language]+'.properties', 'w+') as configfile:
                        configfile.writelines(languagesValuesFinal[language])