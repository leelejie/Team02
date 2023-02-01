from pathlib import Path
import csv
#crete file path to csv file 
fp = Path.cwd()/"CSV_reports"/"Overheads.csv"
#read csv file to append data from csv- overhead category and value
with fp.open(mode = "r",encoding = "UTF-8", newline="") as file:
    reader= csv.reader(file)
    #skip header
    next(reader)
    #define function
    def overhead():
        #docstrings to describe function
        """
        - This function calculates and returns the highest overhead 
        category and its percentage
        - There are no parameters required
        """
        #create empty lists and strings to store value later on
        overhead_value=[]
        overhead_category=[]
        overhead_valueandcategory=[]
        highestoverhead_category=""
        #create for loop to append overhead category and value to respective lists
        for line in reader:
            overhead_valueandcategory.append(line)
            overhead_value.append(float(line[1]))
            overhead_category.append(line[0])
        #use max function to find largest value in the list storing overhead values
        largest_value=max(overhead_value)
        #create for loop to access sublists in the nested list (overhead_valueandcategory)
        for sublist in overhead_valueandcategory:
            #create if statement to check if each overhead value from the sublist matches the 
            #max overhead value to find its respective category
            if float(sublist[1])==largest_value:
                highestoverhead_category=sublist[0]
                #statement returned as output
                return (f"[HIGHEST OVERHEADS] {highestoverhead_category.upper()}: {largest_value}%")
    print(overhead())

        
