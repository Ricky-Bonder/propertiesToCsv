#!/usr/bin/python

import csv
import glob
import os
import configparser

header = ['key', 'english', 'italian', 'deutsch', 'french', 'spanish', 'ofFile']
files = ['root', 'cagepreparation', 'changepartialscreen', 'changetotalscreen', 'notification', 'reader', 'settings']
valueProperty = list()
path = '/home/rossola/VSCodeProjects/propertiesToCsv/propertiesFiles/'

with open('/home/rossola/VSCodeProjects/propertiesToCsv/properties.csv', 'a+') as csvFile:
    dw = csv.DictWriter(csvFile, delimiter=',', fieldnames=header)
    dw.writeheader()
    writer = csv.writer(csvFile)
    for file in files:
        seq = (path, file, '.properties')
        filepath = ''.join(seq)
        with open(filepath, errors='ignore') as f:
            for entry in f.readlines():
                if entry.endswith('\n'):
                    entry = entry.rstrip('\n')
                value = entry.split("=", 1)
                print("couple key-value: ", value)
                value.append('')
                value.append('')
                value.append('')
                value.append('')
                value.append(file)
                valueProperty.append(value)
            writer.writerows(valueProperty)
            writer.writerow('\n')
        valueProperty.clear()