import pandas as pd

import csv

with open('data.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

rows = []
newfields = ['','']
with open('data.csv', 'w' , newline='') as file:
    writer = csv.Dictwriter(file)
    for row in rows:
        writer.writer(row)