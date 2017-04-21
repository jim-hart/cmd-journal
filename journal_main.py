#! python3

"""Program for logging simple journal entries"""

import sys
import datetime_information
import journal_data


class Entry:
    """Constructs a formatted text body and file name that details various
    datetime information, along with the current entry number"""
    
    def __init__(self, entry):
        self.json_obj  = journal_data.JsonData()
        self.entry     = "{} {}".format("", entry)
        self.datetime  = datetime_information.get_datetime()
        self.body      = self.format_body()
        self.filename  = self.format_filename()
        
        
    def format_body(self):
        """Returns list containing header information and the user's text entry
        
        Arguments:
            entry -- string containing user's journal entry
            
        formatted header example:
                
        Date: Jan-1-1970
        Day : Thursday    
        Time: 04:00:00
        Log#: 1
                
        Entry: <user's text here>       
        
        """  
        
        return  ["Date: {}\n".format(self.datetime["date"]),
                 "Day : {}\n".format(self.datetime["day"]),
                 "Time: {}\n".format(self.datetime["time"]),
                 "Log#: {}\n\n".format(self.json_obj.data["entry_count"]+1),
                 "Entry:{}".format(self.entry)]
     
    
    def format_filename(self):
        """Returns filename formatted with datetime information, and entry number
        
        Example:
        
        Entry #1 -- Jan-1-1970
        
        """        
        
        return "Entry #{} -- {}.txt".format(self.json_obj.data["entry_count"]+1,
                                            self.datetime["date"])


def get_entry():
    """Return is based on input provided to selection variable:       
        '-qc'-- Program exits and no data is written to any file
        
        '-s' -- Entry object is constructed with user_input and is written
                to .txt file.  file_information.json["entry_count"] will be
                incremented by 1.
                
        '-e' -- get_entry() is called again, no data written to any file. This
                allows user to change entry before committing to file.
                     
    """    
    count = journal_data.JsonData().data["entry_count"] + 1
    
    user_input = input("Entry #{}: ".format(count)) 
    selection  = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    #simple error checking process to verify journal entry creation
    while selection not in ["-s", "-e", "-qc"]:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
        
    if selection == "-qc":
        sys.exit("Entry cancelled, closing program.")   
    elif selection == "-s":
        return user_input
    elif selection == "-e":
        return False
   

def main():
    """Main flow control for program"""    
    
    count = journal_data.JsonData().data["entry_count"] + 1
    print("** Begin log for {} **\n".format(
                            count, datetime_information.get_datetime()["date"]))    
    
    #Allows user to re-enter text as many time as desired, or quit at any time
    user_entry = get_entry()
    while not user_entry:
        user_entry = get_entry()    

    journal_data.save_entry(Entry(user_entry))

if __name__ == '__main__':
    main()


   