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
        #creating prevprofit variable to store the previous net profit value
        #creating count variable to track the different rows in the data
        prevprofit = 0
        count = 0

        #for loop to go through every row of data in the list of data
        for row in reader:

            #use of conditionals where code will run if current day net profit is lower than previous day
            if int(prevprofit) > int(row[4]) and count>0:

                #calculate the difference in net profit
                diff = int(prevprofit) - int(row[4])
                noprofitdeficit = False

                #prints the output desired if the if statement occurs
                print(f"[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: {diff}")
            
            prevprofit = row[4]
            count+=1
        if noprofitdeficit == True:
            print("no result")
    profit_loss()