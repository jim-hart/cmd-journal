#! python3

"""Program for logging simple journal entries"""
import time
from journal_file_handling import (get_entry_count)


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

    return user_entry

if __name__ == '__main__':
    x = get_entry()
    print(x)



   