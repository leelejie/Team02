

#to import the independent functions into this main function
import cash_on_hand,overheads, profit_loss

#to call the different functions into the main function 
def main():

        cash_on_hand.coh_function()
        overheads.overheads_function()
        profit_loss.profitloss_function()

output=main()
<<<<<<< HEAD
=======
        
from pathlib import Path
>>>>>>> b3bbd6c05d316a30b0cdd8b979b226d3e32e0c0e

#This Function identifies as an iterator for all searhces of the files and folders in the directory 
#consisting of cash on hand, overheads and profit loss. 

# create a path object for contacts.txt
from pathlib import Path
file_path= Path(r"C:\PFB\summary_report.txt")
#opening file with 'with' and 'open'
#w passed to the mode parameter so i can write a text file
#allows it to write the function output into a text file
with file_path.open(mode = "w") as file:
    #write() method to write data into plain text file
<<<<<<< HEAD
    file.write(f"{output}")
=======
        file.write(f"{output}")
file.close(file_path)

>>>>>>> b3bbd6c05d316a30b0cdd8b979b226d3e32e0c0e
