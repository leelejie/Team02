# integrated group project
from pathlib import Path
import csv


fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    def cash_loss(option):
        
        prev_cash = 0
        count = 0
        #use of loops to go through every item in the list
        if option == "cash":

            for num in reader:
            #if statement so that if the previous day is higher than the current day in the statement it will commit the code below 
                if int(prev_cash)>int(num[1]) and count>0:

            #calculating the difference in the cash and use of abs to remove the negative sign to display the difference in the return statement
                   diff = abs(int(num[1]) - int(prev_cash))

            #return back the day and the difference of the cash deficit
                   return f"[CASH DEFICIT] DAY: {num[0]}, AMOUNT: {diff}"

                prev_cash = num[1]
                count+=1

            #if the previous day is lower than the current day it will commit the code below
            else:
                return f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"

    print(cash_loss("cash"))
