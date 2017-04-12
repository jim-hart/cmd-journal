#! python3

"""Contains functions that construct a filename based on current date"""
import time
import json
import os

def format_datetime():
    """Returns a string representative of the current date based on eastern
    standard time.  

    Returned string will have the following format: Jan-1-1970"""

    current_date = time.localtime()

    months_dictionary = {1:  "Jan",
                         2:  "Feb",
                         3:  "Mar",
                         4:  "Apr",
                         5:  "May",
                         6:  "Jun",
                         7:  "Jul",
                         8:  "Aug",
                         9:  "Sep",
                         10: "Oct",
                         11: "Nov",
                         12: "Dec"}
    
    month = months_dictionary[current_date.tm_mon]
    day = current_date.tm_mday
    year = current_date.tm_year

    return "{}-{}-{}".format(month, day, year)
    

def get_entry_count():
    """returns total count of journal entries from entry_count.json"""

    current_directory = os.getcwd()
    filename = "{}\\json_data\\entry_count.json".format(current_directory)
    with open(filename) as f_obj:
        return json.load(f_obj)

if __name__ == '__main__':
    #test case
    print(get_entry_count())
