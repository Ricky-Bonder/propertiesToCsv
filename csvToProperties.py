#!/usr/bin/python

import csv
import pandas
from itertools import chain
import configparser


header = ['english', 'italian', 'deutsch', 'french', 'spanish']
keyProperty = list()
valueProperty = list()

englishValues = list()
englishValuesFinal = list()

with open('/home/rossola/VSCodeProjects/propertiesToCsv/properties.csv', 'rb') as csvFile:
    
    reader = pandas.read_csv(csvFile)
    first_column = reader.iloc[:, 0]
    
    keyProperty = first_column.values
    print(keyProperty)
    
    i=1
    for language in header:
        print(language)
        valuesColumn = reader.iloc[:, i]
        valueProperty = valuesColumn.values
        print(valueProperty)
        englishValues = list(zip(keyProperty, valueProperty))
        print("ENG: ", englishValues)
        # i += 1
        
    for entry in englishValues:
        mapped = '='.join(entry)
        mapped = mapped+"\n"
        print(mapped)
        englishValuesFinal.append(mapped)
        
    with open('/home/rossola/VSCodeProjects/propertiesToCsv/testFile.properties', 'w+') as configfile:
        configfile.writelines(englishValuesFinal)
        
    
    