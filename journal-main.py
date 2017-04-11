"""Program for logging simple journal entries to .txt files via cmd line"""
import time


def format_datetime(current_datetime):
    """ Function for formatting current datetime to be later used as file name
    for journal entries """

    date_dictionary = {"Jan":1,
                       "Feb":2,
                       "Mar":3,
                       "Apr":4,
                       "May":5,
                       "Jun":6,
                       "Jul":7,
                       "Aug":8,
                       "Sep":9,
                       "Oct":10,
                       "Nov":11,
                       "Dec":12}

    split_time = current_datetime.split()
    



if __name__ == '__main__':
    format_datetime(time.ctime())
    print(split_time)

