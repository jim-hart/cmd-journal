#! python3

"""Functions for writing user input to files, and updating entry_count data"""

import json
import os
import sys
import shutil

class Directory:
    """Holds directory information for files used in program"""

    ENTRIES = 'Q:\\GDrive\\Books & Notes\\Entries'

    @classmethod
    def get_path(cls, json_data=False, entry_data=False):
        """Returns path of folder holding json data for the program"""

        if json_data:
            return os.path.join(os.path.dirname(sys.argv[0]),
                               'json_data\\file_information.json')
        elif entry_data:
            return JsonData.get_data()['entry_path']

    @classmethod
    def check_entry_path(cls):
        """Returns true if entry path folder exists in file_information.json,
        otherwise, default path is set for user in working directory for
        program"""

        if not os.path.exists(JsonData.get_data()['entry_path']):
            default_path = os.path.join(os.path.dirname(sys.argv[0]), 'Entries')
            print("Enter Folder Location not detected! Folder set to: {}"
                  .format(default_path))
            os.mkdir(default_path)

        else:
            return True

    @classmethod
    def set_entry_path(cls, path):
        """Changes path to entry folder and copies all current entries to that
        new folder
        
        Args:
            path (str): string that contains path to new folder location
        
        """  
        
        # current_path = cls.get_path()
        # shutil.copytree(
        # JsonData.update_data(entry_path=True, new_path=path)
        

class JsonData:
    """Class for managing file_information.json"""

    @classmethod
    def get_data(cls):
        """Returns dictionary containing keys:values in file_information.json"""

        with open(Directory.get_path()) as f_obj:
            return json.load(f_obj)

    @classmethod
    def update_data(cls, entry_count=False, entry_path=False, new_path=""):
        """Performs action based on passed entry_count or entry_path arguments 

        Args:            
            entry_count (bool): if True, entry_count is iterated by 1
            entry_path (bool):  if True, entry_path will be set to new_path parameter
            new_path (str):     contains string holding new path to entry folder
        
        """

        file_data = cls.get_data()
        with open(Directory.get_path(), 'w') as f_obj:
            if entry_count:
                file_data['entry_count'] += 1 
            elif entry_path:
                file_data['entry_path'] = new_path
                
            json.dump(file_data, f_obj, indent=4, sort_keys=True)
            

def save_entry(entry):
    """Writes user's journal entry and datetime information to a .txt file and
    calls update_data() from JsonData() to iterate entry count by 1
    
    Arguments:
        :param entry: Object containing formatted text header and filename
        
    """

    JsonData().update_data(entry_count=True)

    with open(os.path.join(Directory.ENTRIES, entry.filename), 'w') as f_obj:
        f_obj.writelines(entry.header)
        f_obj.writelines(entry.body)

    print("Entry saved to {}".format(Directory.ENTRIES))


if __name__ == '__main__':
    # test case(s)
    # Directory.check_entry_path()
    Directory.check_entry_path()
    # print(Directory.get_path())
