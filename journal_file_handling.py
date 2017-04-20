#! python3

"""Functions for writing user input to files, and updating entry_count data"""

import json
import sys, os
import datetime_information

class Directory():
    """Holds directory information for files used in program"""
        
    JSON    = "Q:\\Git_Repos\\#Projects#\\cmd-journal\\json_data\\file_information.json"
    ENTRIES = "Q:\\GDrive\\Books & Notes\\Entries"


def process_json(update_count=False):
    """Returns, or writes data to file based on arguments passed to function
    
    Arguments:
    file_type   -- Used as variable to pull file path, which is located in
                   Directory class
    update_count-- if True, increments file_information.json["entry_count"] by 1
    
    """    
    
    #If only passed file_type, data is only returned
    with open(Directory.JSON) as f_obj:
        if not update_count:
            return json.load(f_obj)
        else:
            file_data = json.load(f_obj)
    
    #data write process
    with open(Directory.JSON, 'w') as f_obj:
        file_data["entry_count"] += 1
        json.dump((file_data), f_obj, indent=4, sort_keys=True)



def save_entry(entry):
    """Writes user's journal entry and datetime information to a .txt file and
    iterates file_information.json by 1
    
    Arguments:
    entry -- string containing user's journal entry
        
    .txt header format example:
    
    Date: Jan-1-1970
    Day : Thursday    
    Time: 04:00:00
    Log#: 1
            
    Entry: <user's text here>       
    
    """
    
    process_json(update_count=True)
    count = process_json()["entry_count"]    
    #datetime_information() stored in variable so it's only called once to avoid
    #possible time conflicts from three separate calls in a list literal
    date_information = datetime_information.get_datetime()
    file_information = ["Date: {}\n".format(date_information["date"]),
                        "Day : {}\n".format(date_information["day"]),
                        "Time: {}\n".format(date_information["time"]),
                        "Log#: {}\n\n".format(count),
                        "Entry:{}".format(entry)]
     
    directory = Directory.ENTRIES
    filename = "{}\\Entry #{} -- {}.txt".format(
                                    directory, count, date_information["date"])

    with open(filename, "w") as f_obj:
        f_obj.writelines(file_information)
    
if __name__ == '__main__':
    #test case
    print()
    
  
