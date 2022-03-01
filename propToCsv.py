#!/usr/bin/python

import csv

header = ['', 'english', 'italian', 'deutsch', 'french', 'spanish']
valueProperty = list()


with open('/home/rossola/VSCodeProjects/propertiesToCsv/propertiesFiles/root/root.properties') as f:
    for entry in f.readlines():
        if entry.endswith('\n'):
            entry = entry.rstrip('\n')
        value = entry.split("=")
        print("couple key-value: ", value)
        valueProperty.append(value)
    print(valueProperty)
    with open('/home/rossola/VSCodeProjects/propertiesToCsv/properties.csv', 'a+') as csvFile:
            dw = csv.DictWriter(csvFile, delimiter=',', fieldnames=header)
            dw.writeheader()
            writer = csv.writer(csvFile)
            writer.writerows(valueProperty)