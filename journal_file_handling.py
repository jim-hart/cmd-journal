#! python3

"""Functions for writing user input to files, and updating entry count data"""
import json
import os
import datetime_information

def get_entry_count(update_count=False):
    """Either returns current journal entry count, or sends that count to
    get_entry_county()

    Arguments:
    update_count -- if True, sends count to update_entry_count() to be updated

    """

    current_directory = os.getcwd()
    filename = "{}\\json_data\\entry_count.json".format(current_directory)    
    with open(filename) as f_obj:
        entry_count = json.load(f_obj)
        
    if update_count:
        update_entry_count(filename, entry_count)
    else:
        return entry_count

def update_entry_count(filename, entry_count):
    """Updates entry_count.json file"""

    with open(filename, 'w') as f_obj:
        json.dump(entry_count+1, f_obj)


def save_entry(entry):
    """Writes user's journal entry and datetime information to a .txt file and
    calls get_entry_count(update_count=True) to update entry count.
    
    Arguments:
    entry -- string containing user's journal entry
        
    File output format example:
    
    Date: Jan-1-1970
    Day : Thursday    
    Time: 04:00:00
    Log#: 1
            
    Entry: <users text here>       
    
    """
    
    
    count = get_entry_count() + 1
    
    #datetime_information() stored in variable so it's only called once to avoid
    #possible time conflicts from three separate calls in a list literal
    date_information = datetime_information.get_datetime()
    file_information = ["Date: {}\n".format(date_information["date"]),
                        "Day : {}\n".format(date_information["day"]),
                        "Time: {}\n".format(date_information["time"]),
                        "Log#: {}\n\n".format(count),
                        "Entry:{}".format(entry)]
     
    
    directory = "Q:\\GDrive\\Books & Notes\\Entries"
    filename = "{}\\Entry #{} -- {}.txt".format(
                                    directory, count, date_information["date"])

    with open(filename, 'w') as f_obj:
        f_obj.writelines(file_information)        
    
    get_entry_count(update_count=True)
    
if __name__ == '__main__':
    #test case
    print()
