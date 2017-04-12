#! python3

"""Program for logging simple journal entries"""
import sys
import time
from journal_file_handling import (get_entry_count, save_entry)


def datetime_information():
    """Returns dictionary of current date, time, and day of week based on easten
    standard time
    
    return example:
    {
        "date": Jan-1-1970
        "time": 04:00:00
        "day" : Thursday
    }

    """

    current_datetime = time.localtime()

    months_dictionary = {1 : "Jan",
                         2 : "Feb",
                         3 : "Mar",
                         4 : "Apr",
                         5 : "May",
                         6 : "Jun",
                         7 : "Jul",
                         8 : "Aug",
                         9 : "Sep",
                         10: "Oct",
                         11: "Nov",
                         12: "Dec"}
    
    days_dictionary =   {1 : "Monday",
                         2 : "Tuesday",
                         3 : "Wednesday",
                         4 : "Thursday",
                         5 : "Friday",
                         6 : "Saturday",
                         7 : "Sunday"}

    #date information
    month   = months_dictionary[current_datetime.tm_mon]
    day     = current_datetime.tm_mday    
    year    = current_datetime.tm_year
    weekday = days_dictionary[current_datetime.tm_wday]
    
    if day < 10:
        day = "0{}".format(current_datetime.tm_mday)
    
    #time information
    hour    = current_datetime.tm_hour
    minute  = current_datetime.tm_min
    second  = current_datetime.tm_sec

    #formatted information
    return {"date": "{}-{}-{}".format(month, day, year),
            "time": "{}:{}:{}".format(hour, minute, second),
            "day" :  weekday}


def get_entry():

    print("** Begin log for {} **\n".format(datetime_information()["date"]))
    
    user_entry = input("Entry #{}: ".format(get_entry_count() + 1))
    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    selection_list = ["-s", "-e", "-qc"]    
    while selection not in selection_list:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
        
    if selection == "-qc":
        sys.exit("Entry Cancelled")
    else:
        confirm_entry(selection, user_entry)


def confirm_entry(selection, user_entry):
    """Processes user selection in get_entry() function
    
    Arguments:
    selection  -- string value that dictates how program proceded
        "-s" selector saves the journal entry
        "-e" selector calls get_entry() so user can re-input entry        
    user_entry -- string that contains users journal entry
    
    """
    
    date = datetime_information()["date"]
    
    if selection == "-s":
        save_entry(date, user_entry)
    elif selection == "-e":
        get_entry()


if __name__ == '__main__':
    #x = get_entry()
    #print(x)

    get_entry()



   