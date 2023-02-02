#to import the csv file into the file
from pathlib import Path
import csv

#creates a file path towards the csv file 

fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    #skip header
    next(reader)
    #function to calculate the difference in the cash deficit days 
    def coh_function():
        
        """
        This function identifies the days where the previous day is higher than the current day
        and computes the difference 
        No parameters is required
        """
        #creates empty lists for the variables below
        coh_list=[]
        day_list=[]
        coh_day_list=[]
        listdeficit_coh=[]
        listdeficit_day=[]
        listdeficit_diff=[]
        statement=[]
        
        #for loop to go through every data in the list
        for values in reader:
            #to append the the values from the csv files into the empty lists
            coh_list.append(values[1])
            day_list.append(values[0])
            coh_day_list.append(values)

        #to find how many days there are in the data and assign it to a variable
        length=len(day_list)
        
        #to loop through for the number of  and has a enumerate 
        for index, (day,coh) in enumerate(coh_day_list):
            #if statement so that if the index is more than 0 but less than the length of the list, itll commit the codes below
            if 0<index<length:
                #set a variable to the previous day's cash on hand 
                prev_coh=float(coh_list[index-1])
                #if statement so that if a previous day's cash is higher than the current day's, itll commit the code below
                if float(coh)<prev_coh:
                    #to append the days and the difference in the values of the days where the previous day's cash is higehr than the current day into empty lists
                    listdeficit_day.append(day)
                    listdeficit_coh.append(float(coh))
                    listdeficit_diff.append(float(prev_coh)-float(coh))

        #to find the number of values in the list
        lengthd=len(listdeficit_day)

        #if statement so if the list of the days where there's a cash deficit is not empty itll commit the code below
        if listdeficit_day!=[]:
            
            #loops through the every data and to iterate over the range of the number of deficit days  
            for count in range(lengthd):   

                #Assigns all the values in the lists into variables to display in the statement    
                d_day=listdeficit_day[count]
                d_dif=listdeficit_diff[count]
                print(f"[CASH DEFICIT] DAY: {float(d_day)}, AMOUNT: USD{d_dif}")
                     
        #if theres no deficit days in the list, itll commit the code below
        else:
            #prints this statement when theres no cash deficit days
            print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
 
    #to call the function
    coh_function()
        
        

        