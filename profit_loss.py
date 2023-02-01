from pathlib import Path
import csv
#creating a file to csv file
fp = Path.cwd()/"CSV_reports"/"Profit and Loss.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) #skip header
    
    def profit_loss():
        """
        - This function computes the difference in the net profit column
        if the net profit on the current day is lower than the previous day
        - Otherwise it returns net profit surplus if all the net profit for the
        current day is higher than the previous day
        """
        #creating prevprofit variable to store the previous net profit value
        #creating count variable to track the different rows in the data
        #creating noprofitdeficit variable to track the output values. "true" when there is no output "false" when there is
        prevprofit = 0
        count = 0
        noprofitdeficit = True

        #for loop to go through every row of data in the list of data
        for row in reader:

            #use of conditionals where code will be committed if current day net profit is lower than previous day
            if int(prevprofit) > int(row[4]) and count>0:

                #assigning noprofitdeficit to be false as a result of if statement
                noprofitdeficit = False

                #calculating the difference in net profit
                diff = int(prevprofit) - int(row[4])

                #prints the output desired if the if statement occurs
                print(f"[PROFIT DEFICIT] DAY: {row[0]}, AMOUNT: USD{diff}")
            
            #reassign a new value to the variable to store the updated previous data
            #count to track the row number in the dataset so as to skip the first row 
            prevprofit = row[4]
            count+=1
        
        #if statement for when there is no output values meaning all the current values are higher than the previous value
        if noprofitdeficit == True:
            
            #prints the output desired if the if statement occurs
            print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    
    #executing the function
    profit_loss()