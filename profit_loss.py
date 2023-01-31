from pathlib import Path
import csv
fp = Path.cwd()/"CSV_reports"/"Profit and Loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    def profit_loss():
        """
        """
        prevprofit = 0
        count = 0
        for row in reader:
            if int(prevprofit) > int(row[4]) and count>0:
                diff = abs(int(row[4]) - int(prevprofit))
                return f"[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: {diff}"
            prevprofit = row[4]
            count+=1
        else:
            return f"[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    print(profit_loss())