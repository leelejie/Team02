#to import the independant functions into this main function
import cash_on_hand,overheads, profit_loss

#to call the different functions into the main function 
def main():

    cash_on_hand.coh_function()
    overheads.overhead_function()
    profit_loss.profitloss_function()

    return 

output = main()  
from pathlib import Path

#This Function identifies as an iterator for all searhces of the files and folders in the directory 
#consisting of cash on hand, overheads and profit loss. 

# create a path object for contacts.txt
file_path = Path.cwd/"summary_report.txt"

#allows it to write the function output into a text file
with file_path.open(mode = "w") as file:
    file.write(output)

