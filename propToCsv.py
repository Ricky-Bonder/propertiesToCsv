#!/usr/bin/python

import csv
import glob
import os
import configparser

languages = ['↓ KEYS ↓ (do not edit)', 'ENGLISH', 'ITALIANO', 'DEUTSCH', 'FRANÇAIS', 'ESPAÑOL', 'Of File (do not edit)  ']
files = ['cagepreparation', 'changepartialscreen', 'changetotalscreen', 'notification', 'reader', 'settings']
valueProperty = list()
path = '~/VSCodeProjects/propertiesToCsv'

with open(os.path.expanduser(path)+'/properties.csv', 'a+') as csvFile:
    dw = csv.DictWriter(csvFile, delimiter=',', fieldnames=languages)
    dw.writeheader()
    writer = csv.writer(csvFile)
    for file in files:
        seq = (os.path.expanduser(path)+"/propertiesFiles/", file, '.properties')
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