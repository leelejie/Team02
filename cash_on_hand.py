from pathlib import Path
import csv


fp = Path.cwd()/"CSV_reports"/"Cash on Hand.csv"
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    def coh_function():
        
        """
        This function...
        """
        coh_list=[]
        day_list=[]
        coh_day_list=[]
        listdeficit_coh=[]
        listdeficit_day=[]
        listdeficit_diff=[]
        statement=[]
        for values in reader:
            coh_list.append(values[1])
            day_list.append(values[0])
            coh_day_list.append(values)
        length=len(day_list)
        for index, (day,coh) in enumerate(coh_day_list):
            if 0<index<length:
                prev_coh=float(coh_list[index-1])
                if float(coh)<prev_coh:
                    listdeficit_day.append(day)
                    listdeficit_coh.append(float(coh))
                    listdeficit_diff.append(float(prev_coh)-float(coh))
        lengthd=len(listdeficit_day)
        if listdeficit_day!=[]:

            for count in range(lengthd):            
                d_day=listdeficit_day[count]
                d_dif=listdeficit_diff[count]
                print(f"[CASH DEFICIT] DAY: {float(d_day)}, AMOUNT: USD{d_dif}")
                     

        else:
            print(f"[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    coh_function()
        
        

        