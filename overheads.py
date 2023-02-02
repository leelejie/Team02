from pathlib import Path
import csv
#creating a file to csv file
fp = Path.cwd()/"CSV_reports"/"Overheads.csv"
#read csv file to append values/ access the data
with fp.open(mode = "r",encoding = "UTF-8", newline="") as file:
    reader= csv.reader(file)
    #skip header
    next(reader)
    #define function
    def overhead():
        #docstrings to describe function
        """
        - This function finds the highest overhead category and returns the category
        along with its percentage
        - There are no parameters required
        """
        #create empty lists to store items
        overhead_value=[]
        overhead_category=[]
        overhead_valueandcategory=[]

        #for loop to access each row in the file
        for line in reader:

            #append every row to overhead_valueandcategory
            #it will be a nested list storing sublists of each data row 
            overhead_valueandcategory.append(line)

            #append every overhead value to list
            overhead_value.append(float(line[1]))

            #append eveery overhead category to list
            overhead_category.append(line[0])

        #use max function to find maximum overhead value  
        #from the list of overhead values
        largest_value=max(overhead_value)

        #empty list to store overhead category
        highest_overheadcategory=[]

        #if and elif statements check the index of the  
        #largest overhead value which came from the nested list 
        #this allows me to identify the position of the overhead category in the nested list
        #so it can be printed
        if largest_value==float(overhead_valueandcategory[0][1]):
            #eg. if the above statement is true, the below statement is executed and 
            #highest_overheadcategory is assigned to the category identified in the nested list
            #float function is used to covert the values of the overheads from a string to float 
            #so that its value can be compared to the largest value(float)
            highest_overheadcategory=overhead_valueandcategory[0][0]
        elif largest_value==float(overhead_valueandcategory[1][1]):
            highest_overheadcategory=overhead_valueandcategory[1][0]
        elif largest_value==float(overhead_valueandcategory[2][1]):
            highest_overheadcategory=overhead_valueandcategory[2][0]
        elif largest_value==float(overhead_valueandcategory[3][1]):
            highest_overheadcategory=overhead_valueandcategory[3][0]
        elif largest_value==float(overhead_valueandcategory[4][1]):
           highest_overheadcategory=overhead_valueandcategory[4][0]
        elif largest_value==float(overhead_valueandcategory[5][1]):
           highest_overheadcategory=overhead_valueandcategory[5][0] 

        #use return to return statement 
        #fstring and braces{} used to get the data assigned to the variables 
        return f"[HIGHEST OVERHEADS] {highest_overheadcategory.upper()}: {largest_value}%"
    
