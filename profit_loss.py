from pathlib import Path
import csv
fp = Path.cwd()/"CSV_reports"/"Profit and Loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    def profit_loss():
        """
        - This function computes the difference in net profit column
        if the net profit on the current day is lower than the previous day
        - 
        """
        prevprofit = 0
        count = 0
        for row in reader:
            if int(prevprofit) > int(row[4]) and count>0:
                diff = int(prevprofit) - int(row[4])
                return(f"[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: {diff}")
            prevprofit = row[4]
            count+=1
        else:
            return(f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    print(profit_loss())    