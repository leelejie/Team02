import cash_on_hand,overheads, profit_loss

def main():

    cash_on_hand.cash_loss()
    overheads.__annotations__
    profit_loss.profit_loss()

    return 

output = main()  
from pathlib import Path

#This Function identifies as an iterator for all searhces of the files and folders in the directory 
#consisting of cash on hand, overheads and profit loss. 

# create a path object for contacts.txt
file_path = Path.cwd/"summary_report.txt"

with file_path.open(mode = "w") as file:
    file.write(output)

