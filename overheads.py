from pathlib import Path
import csv
fp = Path.cwd()/"CSV_reports"/"Overheads.csv"
with fp.open(mode = "r",encoding = "UTF-8", newline="") as file:
    reader= csv.reader(file)
    #skip header
    next(reader)

    def overhead():
        """
        This function returns the highest overhead category. 
        """
        overhead_value=[]
        overhead_category=[]
        overhead_valueandcategory=[]
        for line in reader:
            overhead_valueandcategory.append(line)
            overhead_value.append(float(line[1]))
            overhead_category.append(line[0])
        largest_value=max(overhead_value)
        highest_overheadcategory=[]
        if largest_value==float(overhead_valueandcategory[0][1]):
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
        return f"[HIGHEST OVERHEADS] {highest_overheadcategory}:"
    print(overhead())   
file_path= Path(r"C:\PFB\summary_report.txt") 