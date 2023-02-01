from pathlib import Path
import csv


fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    coh_value=[]
    coh_dayandvalue=[]
    current_number=0
    previous_number=0
    index=1
    for value in reader: 
        coh_dayandvalue.append(value)
        coh_value.append(value[1])
    length=len(coh_value)
    while index<length:
        if float(coh_value[index-1])>float(coh_value[index]):
                print(coh_value[index])
        index+=1
