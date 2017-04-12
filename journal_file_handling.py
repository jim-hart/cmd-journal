#! python3

"""Functions for writing user input to files, and updating entry count data"""
import json
import os


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


def save_entry(date, entry):

    directory = "Q:\\GDrive\\Books & Notes\\Entries"
    filename = "{}\\{}.txt".format(directory, date)

    with open(filename, 'w') as f_obj:
        f_obj.write(entry)        

if __name__ == '__main__':
    #test case
    print()
