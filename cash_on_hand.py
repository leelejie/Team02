# integrated group project
from pathlib import Path
import csv


fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    def cash_loss():
        """
        This function identifies the days where the previous day is higher than the current day
        and computes the difference 
        """
        coh_value=[]
        coh_dayandvalue=[]
        index=1
        for value in reader: 
            coh_dayandvalue.append(value)
            coh_value.append(value[1])
        length=len(coh_value)
        while index<length:
            if float(coh_value[index-1])>float(coh_value[index]):
                print(coh_value[index])
            index+=1
            













            return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

    print(cash_loss())
