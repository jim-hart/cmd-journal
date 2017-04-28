#! python3

"""Functions for writing user input to files, and updating entry_count data"""

import json
import os, sys


class Directory:
    """Holds directory information for files used in program"""
    
    #JSON    = 
    ENTRIES = 'Q:\\GDrive\\Books & Notes\\Entries'
    
    @classmethod
    def json_path(cls):
        return os.path.join(os.path.dirname(sys.argv[0]), 
                          'json_data\\file_information.json')

class JsonData:
    """Class for managing file_information.json"""        
    
    @classmethod
    def get_data(cls):
        """Returns dictionary containing keys:values in file_information.json"""
                     
        with open(Directory.json_path()) as f_obj:
            return json.load(f_obj)
            
    @classmethod
    def update_count(cls):
        """Iterates entry_count value by 1 and writes new value to
        file_information.json """
        
        file_data = cls.get_data()        
        with open(Directory.json_path(), 'w') as f_obj:
            file_data['entry_count'] += 1
            json.dump(file_data, f_obj, indent=4, sort_keys=True)


def save_entry(entry):
    """Writes user's journal entry and datetime information to a .txt file and
    calls update_count() from JsonData() to iterate entry count by 1
    
    Arguments:
        entry -- Object containing formatted text header and filename
        
    """
    
    JsonData().update_count()

    with open(os.path.join(Directory.ENTRIES, entry.filename), 'w') as f_obj:
        f_obj.writelines(entry.header)
        f_obj.writelines(entry.body)
    
    print("Entry saved to {}".format(Directory.ENTRIES))
    
    
if __name__ == '__main__':
    # test case(s)
    #JsonData().update_count()
    print(Directory.json_path())
