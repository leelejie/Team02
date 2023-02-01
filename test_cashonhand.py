# integrated group project
from pathlib import Path
import csv


fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:

    
    reader = csv.reader(file)
    next(reader)
    dayandcoh_list=[]
    day_list=[]
    coh_list=[]
   

        #use of loops to go through every item in the list
    for line in reader:
        coh_list.append(line[1])
        day_list.append(line[0])
        dayandcoh_list.append(line)

   
        
    