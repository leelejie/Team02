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
        coh_days=[]
        dayofdeficit=[]
        index=1
        for value in reader:
            coh_days.append(value[0])
            coh_value.append(value[1])
        length=len(coh_value)
       
       

        while index<length:
            if float(coh_value[index-1])>float(coh_value[index]):
               
                diff = int(coh_value[index-1]) - int(coh_value[index])
            
                
                print(f" [CASH DEFICIT] DAYS: {coh_days[index]}, AMOUNT: USD{diff}")

        for num in coh_value:
            if num[0]<num[1]:
               print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE"  )
 
                


                             
               
            index+=1
        # if 
    

    
   
        
    cash_loss()