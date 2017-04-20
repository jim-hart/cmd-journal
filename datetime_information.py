import time

def get_datetime():
    """Returns a formatted dictionary of current date, time, and day of week
    based on eastern standard time.
    
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
    
    days_dictionary =   {0 : "Monday",
                         1 : "Tuesday",
                         2 : "Wednesday",
                         3 : "Thursday",
                         4 : "Friday",
                         5 : "Saturday",
                         6 : "Sunday"}

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

if __name__ == '__main__':
    print(get_datetime())
    