#to import the csv file into the file
from pathlib import Path
import csv

#creates a file path towards the csv file 
fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
#read csv file to access and append the data
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    #skip header
    next(reader)
    #function to calculate the difference in the cash deficit days 
    
    def coh_function():
        #docstrings to describe function
        """
        This function identifies the days where the previous day is higher than the current day
        and computes the difference 
        """
        #creates empty lists for the variables below
        coh_list=[]
        day_list=[]
        coh_day_list=[]
        listdeficit_day=[]
        listdeficit_diff=[]
        
            
            
        #this appends all the days and cash on hand to a nested list with 
        #respective [day,cash on hand] as a sublist
        coh_day_list.append(values)

        #to find how many data sets there are(range) and assign it to length
        length=len(day_list)
        
        #use of enumerate to take note of the count as index
        for index, (day,coh) in enumerate(coh_day_list):

            #ensure that index is less than length and more than 0, meaning the below will not execute
            #for indexes greater than the length of the list and below 0 index as there is no previous value for 0
            if 0<index<length:
                
                #for every time the for loop is executed, prev_coh; the previous cash on hand
                #would be the value of coh in coh_list with a index of index-1 compared to the current value 
                #with index 1 assigned
                #float function used to convert string to foat for comparison of current and previous 
                #value to take place
                prev_coh=float(coh_list[index-1])

                #conditional if statement: executed if a previous day's cash is higher than the current day
                if float(coh)<prev_coh:

                    #append days with deficit into empty list
                    listdeficit_day.append(day)  

                    

                    #to append the days and the difference in the values of the days when the previous 
                    # day's cash is higehr than the current day into empty lists
                    listdeficit_diff.append(float(prev_coh)-float(coh))

        #to find the number of values in the list
        lengthd=len(listdeficit_day)

        #if the list of the days where there's a cash deficit is not empty
        #it means that there are days with cash deficit.
        # it'll commit the code below
        if listdeficit_day!=[]:
            
            #loops through the every data and to iterate over the range of the number of deficit days  
            for count in range(lengthd):   

                #Assigns all the values in the lists into variables to display in the statement    
                d_day=listdeficit_day[count]
                d_dif=listdeficit_diff[count]
                
# 1. f strings used to hold a variable 
# 2. braces {} are used for the function as the value
# of the function is to be extracted, and not the name itself 
# below statement will be printed as output. it is printed as many times for each deficit
                print(f"[CASH DEFICIT] DAY: {float(d_day)}, AMOUNT: USD{d_dif}")
                     
        #if theres no deficit days in the list, it'll commit the code below
        #if the above if conditional statement is not met, this will be executed
        else:
            #prints this statement when theres no cash deficit days
            print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
 

        
        

        