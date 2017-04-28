#! python3

"""Functions for writing user input to files, and updating entry_count data"""

import json
import os
import sys
import shutil


class Directory:
    """Handles retrieval and updating of file paths"""

    ENTRY_DEFAULT = os.path.abspath(os.path.join(
                                    os.path.dirname(sys.argv[0]), 'Entries'))

    @classmethod
    def get_path(cls, json_data=False, entry_files=False):
        """Returns path of folder holding json data for the program"""

        if json_data:
            return os.path.join(os.path.dirname(sys.argv[0]),
                                'json_data\\file_information.json')
        elif entry_files:
            return JsonData.get_data()['entry_path']

    @classmethod
    def check_entry_path(cls):
        """Returns true if entry path folder exists in file_information.json,
        otherwise, default path is set for user in working directory for
        program and method returns False"""

        if not os.path.exists(JsonData.get_data()['entry_path']):
            print(">>Entry folder location not detected | folder set to: {}"
                  .format(cls.ENTRY_DEFAULT))
            os.mkdir(cls.ENTRY_DEFAULT)
            JsonData.update_data(entry_path=True, new_path=cls.ENTRY_DEFAULT)
            return False
        else:
            return True

    @classmethod
    def set_entry_path(cls, user_path=None, reset_path=False):
        """Changes path to entry folder and copies all current entries to that
        new folder.  
        
        Args:
            user_path (str): contains path to new folder location
            reset_path (bool): if True, path is reset to default entry path
        
        """
        if reset_path:
            JsonData.update_data(entry_path=True, new_path=cls.ENTRY_DEFAULT)
            return print("Entry folder reset to: {}".format(cls.ENTRY_DEFAULT))

        if os.path.isdir(user_path) and not reset_path:
            shutil.copytree(Directory.get_path(entry_files=True), user_path)
            JsonData.update_data(entry_path=True, new_path=user_path)
            return print("Entry folder updated to: {}".format(user_path))


class JsonData:
    """Class for managing file_information.json"""
    
    @classmethod
    def check_json_path(cls):
        """Generates file_information.json if such file does not exist"""
        
        if not os.path.exists(Directory.get_path(json_data=True)):
            json_object = {"entry_count": -1, "entry_path": ""}
            print(">>Program data file not detected | generating new object now.")
            os.mkdir(os.path.dirname(Directory.get_path(json_data=True)))
            cls.update_data(entry_count=True, default_json=json_object)
    
    
    @classmethod
    def get_data(cls):
        """Returns dictionary containing keys:values in file_information.json"""

        with open(Directory.get_path(json_data=True)) as f_obj:
            return json.load(f_obj)

    @classmethod
    def update_data(cls, entry_count=False, entry_path=False, new_path=None, default_json=None):
        """Performs action based on passed entry_count or entry_path arguments 

        Args:            
            entry_count (bool): if True, entry_count is iterated by 1
            entry_path (bool):  if True, entry_path will be set to new_path parameter
            new_path (str):     contains string holding new path to entry folder
        
        """
        
        if not default_json:
            file_data = cls.get_data()
        else:
            file_data=default_json        
        
        with open(Directory.get_path(json_data=True), 'w') as f_obj:
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

    filename = os.path.join(Directory.get_path(entry_files=True), entry.filename)
    with open(filename, 'w') as f_obj:
        f_obj.writelines(entry.header)
        f_obj.writelines(entry.body)

    print("Entry saved to {}".format(Directory.get_path(entry_files=True)))


if __name__ == '__main__':
    # test case(s)
    print(os.path.abspath(Directory.ENTRY_DEFAULT))
    # Directory.check_entry_path()
    # print(Directory.get_path(json_data=True))
