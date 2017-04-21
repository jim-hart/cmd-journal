#! python3

"""Program for logging simple journal entries"""
import sys
import datetime_information
from journal_file_handling import (Directory, JsonData)

class Entry:
    """Creates Entry object, which holds a formatted filename and text body"""
    
    def __init__(self, entry):
        self.file_data = JsonData().data
        self.entry     = entry
        self.datetime  = datetime_information.get_datetime()
        self.body      = format_body()
        self.filename  = format_filename()
        
        
    def format_body(self):
        """Returns list containing header information, and the users text entry
        
        Arguments:
        entry -- string containing user's journal entry
            
        .txt header format example:
        
        Date: Jan-1-1970
        Day : Thursday    
        Time: 04:00:00
        Log#: 1
                
        Entry: <user's text here>       
        
        """  
        
        return  ["Date: {}\n".format(self.datetime["date"]),
                 "Day : {}\n".format(self.datetime["day"]),
                 "Time: {}\n".format(self.datetime["time"]),
                 "Log#: {}\n\n".format(file_data.data["entry_count"]+1),
                 "Entry:{}".format(self.entry)]
     
    
    def format_filename(self):
        """Returns filename formatted with datetime information, and entry number
        
        Example:
        
        Entry #1 -- Jan-1-1970
        
        """

        return "{}\\Entry #{} -- {}.txt".format(
                                        Directory.ENTRIES,
                                        self.filedata["entry_count"]+1,
                                        self.datetime["date"])


def save_entry(entry, file_data):
    


def confirm_entry(selection):
    """Function will return True or False based on selection argument
    
    Arguments:
    selection  -- string value that dictates which function is passed control
       "-qc" Exits the program; no file is written to or modified
        "-s" Returns True, resulting in main() passing control to save_entry()
        "-e" Returns False, resulting in main() allowing user to re-enter entry   
            
    """
    
    if selection == "-qc":
        sys.exit("Entry Cancelled")   
    elif selection == "-s":
        return True
    elif selection == "-e":
        return False
    
def get_entry():
    user_initial = input("Entry #{}: ".format(file_data.data["entry_count"]+1))
    user_final = "{} {}".format("", user_initial)
    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    #simple error checking process to verify journal entry creation
    selection_list = ["-s", "-e", "-qc"]    
    while selection not in selection_list:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")


def main():
    """Gets user's journal input and passes it to confirm_entry() based on
    selection input request after initial entry process"""
    
    file_data = journal_file_handling.JsonData()
    
    print("** Begin log for {} **\n".format(
                                datetime_information.get_datetime()["date"]))
    
    
        
    while not confirm_entry(selection):
    
    
    journal_file_handling.save_entry(user_final, file_data)
    
   

if __name__ == '__main__':
    entry = Entry()
    print(entry.file_data)


   