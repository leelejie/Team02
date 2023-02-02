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
        dayofdeficit=[]
        index=1
        for value in reader:
            coh_dayandvalue.append(value)
            coh_value.append(value[1])
        length=len(coh_value)
       
        while index<length:
            if float(coh_value[index-1])>float(coh_value[index]):
               
                diff = int(coh_value[index-1]) - int(coh_value[index])
                print(index)

                for num in dayofdeficit:
                   coh_dayandvalue.append(num[0])

                days = dayofdeficit[1]
                print(days)
                return f"[CASH DEFICIT] DAY:{days}  AMOUNT: {diff}"
                # dayofdeficit.append(coh_dayandvalue(index))                
               
            index+=1
        
        

        
   
        
    cash_loss()