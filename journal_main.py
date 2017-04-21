#! python3

"""Program for logging simple journal entries"""
import sys
import datetime_information
from journal_file_handling import (Directory, JsonData)

class Entry:
    """Constructs a formatted text body and file name that details various
    datetime information, along with the current entry number"""
    
    def __init__(self, entry):
        self.file_data = JsonData().data
        self.entry     = "{} {}".format("", entry)
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
                 "Log#: {}\n\n".format(self.file_data["entry_count"]+1),
                 "Entry:{}".format(self.entry)]
     
    
    def format_filename(self):
        """Returns filename formatted with datetime information, and entry number
        
        Example:
        
        Entry #1 -- Jan-1-1970
        
        """        
        
        return "Entry #{} -- {}.txt".format(
                            self.filedata["entry_count"]+1,
                            self.datetime["date"])


def confirm_entry(selection):
    """Function will return True or False based on selection argument
    
    Arguments:
    selection  -- string value that dictates which function is passed control
       "-qc" Exits the program; no file is written to or modified
        "-s" Returns True, resulting in main() passing control to journal_file_handling.save_entry()
        "-e" Returns False, resulting in main() allowing user to re-enter entry   
            
    """
        
def get_entry(count):
    """Return is based on input stored in selection variable:       
            '-qc'-- Program exits and no data written to any file
            '-s' -- Entry object is constructed with user_input and is written
                    to .txt file.  file_information.json["entry_coount"] will be
                    incremented by 1 as well.
            '-e' -- get_entry() is called again, no data written to any file. This
                    allows user to change entry before comitting to file.
               
        Arguments:
            count -- contains current entry count, incremented by 1 for display
                     purposes
    """
    
    user_input = input("Entry #{}: ".format(count)) 
    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    #simple error checking process to verify journal entry creation
    selection_list = ["-s", "-e", "-qc"]    
    while selection not in selection_list:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
        
    if selection == "-qc":
        sys.exit("Entry Cancelled")   
    elif selection == "-s":
        return user_input
    elif selection == "-e":
        return False
        

def main():
    """Main flow control for program"""    
    
    count = JsonData().data["entry_count"]+1
    print("** Begin log for {} **\n".format(
                           count, datetime_information.get_datetime()["date"]))    
    
    #Allows user to re-enter entry as many time as desired, or quit at any time
    while not get_entry(count):
        get_entry(count)
    
    #journal_file_handling.save_entry(Entry())
    
    return Entry()

if __name__ == '__main__':
    main()


   