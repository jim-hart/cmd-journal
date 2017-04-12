"""Contains functions that construct a filename based on current date"""
import time

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
    

if __name__ == '__main__':
    #test case
    print(format_datetime())
