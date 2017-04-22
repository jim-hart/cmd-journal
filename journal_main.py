#! python3

"""Program for logging simple journal entries"""

import sys
import datetime_information
import journal_data


class Entry:
    """Constructs a formatted text header and file name that details various
    datetime information, along with the current entry number"""

    def __init__(self, entry):
        self.log_number  = journal_data.JsonData().get_data()['entry_count'] + 1
        self.datetime    = datetime_information.get_datetime()
        self.header      = self.format_header()
        self.body        = self.format_body(entry)
        self.filename    = self.format_filename()

    def format_header(self):
        """Returns list containing formatted header information.  Also formats
        text header as well.
       
        Formatted header example:
                
        Date: Jan-1-1970
        Day : Thursday    
        Time: 04:00:00
        Log#: 1               
      
        
        """

        return ["Date: {}\n".format(self.datetime['date']),
                "Day : {}\n".format(self.datetime['day']),
                "Time: {}\n".format(self.datetime['time']),
                "Log#: {}\n\n".format(self.log_number)]

    def format_filename(self):
        """Returns filename formatted with datetime information, and entry number
        
        Example:
        
        Entry #1 -- Jan-1-1970
        
        """

        return "Entry #{} -- {}.txt".format(self.log_number,
                                            self.datetime['date'])

    @staticmethod
    def format_body(entry):
        """Returns list containing user's entry strings, along with descriptive
        start and end tags to be displayed in .txt file"""

        entry.insert(0, "---BEGIN LOG---\n\n")
        entry.append("----END LOG----")
        return entry


def get_entry():
    """Return is based on input provided to selection variable:       
        '-qc'-- Program exits and no data is written to any file
        
        '-s' -- List containing entry strings is returned.  This list is then
                formatted with Entry class, and is then pushed to
                journal_data.save_entry()
                
        '-e' -- get_entry() is called again, no data written to any file. This
                allows user to change entry before committing to file.
                     
    """
    count = journal_data.JsonData().get_data()['entry_count'] + 1
    user_entry = input("Entry #{} (enter '\end' to end input):\n".format(count))

    entries = []
    while user_entry.lower().strip() != '/end':
        # Allows enter key to be used in cmd prompt as a line break
        entries.append("{}\n\n".format(user_entry))
        user_entry = input()

    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    while selection not in ["-s", "-e", "-qc"]:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")

    if selection == "-qc":
        sys.exit("Entry Cancelled")
    elif selection == "-s":
        return entries
    elif selection == "-e":
        return False
   

def main():
    """Main flow control for program"""

    print("*** Begin log for {} ***\n".format(
                                datetime_information.get_datetime()['date']))

    # Allows user to re-enter text as many time as desired, or quit at any time
    user_entry = get_entry()
    while not user_entry:
        user_entry = get_entry()

    journal_data.save_entry(Entry(user_entry))

if __name__ == '__main__':
    main()
