from pathlib import Path
import csv


fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    
    def cash_loss():
        """
        This function identifies the days where cash on hand for the previous day is higher than the current day
        and computes the difference between them
        No parameters required
        """
        prev_cash = 0
        count = 0
        nocashdeficit = True

        #for loop to go through every data
        for num in reader:

            #The code will execute when the below condition is met which is that the previous day has higher cash than current day
            if nocashdeficit == True:            
                #prints the output if statement occurs
                print("[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")

            if int(prev_cash) > int(num[1]) and count>0:

                #assigning nocashdeficit to be false as a result of if statement
                nocashdeficit = False

                #calculating the difference in cash 
                diff = int(prev_cash) - int(num[1])

                #prints the output if the if statement occurs
                print(f"[CASH DEFICIT] DAY: {num[0]}, AMOUNT: USD{diff}")
            
            #reassign a new value to the variable to store the updated previous data
            #count to track the row number in the dataset so as to skip the first row 
            prev_cash = num[1]
            count+=1
        
            #if statement for when the current values are higher than the previous value and will execute the code below
       
    
    #executes the function
    cash_loss()
            
        
        













        

    print(cash_loss())


