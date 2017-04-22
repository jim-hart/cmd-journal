#! python3

"""Functions for writing user input to files, and updating entry_count data"""

import json
import os

class Directory:
    """Holds directory information for files used in program"""
        
    JSON    = 'Q:\\Git_Repos\\#Projects#\\cmd-journal\\json_data\\file_information.json'
    ENTRIES = 'Q:\\GDrive\\Books & Notes\\Entries'


class JsonData:
    """Class for managing file_information.json"""    
    
    def __init__(self):
        self.path = Directory.JSON
        self.data = self.get_data()
      
      
    def get_data(self):
        """Returns dictionary containing keys:values in file_information.json"""
                     
        with open(self.path) as f_obj:
            return json.load(f_obj)
            

    def update_count(self):
        """Iterates entry_count value by 1 and writes new value to
        file_information.json """

        with open(self.path, 'w') as f_obj:
            self.data['entry_count'] += 1
            json.dump(self.data, f_obj, indent=4, sort_keys=True)


def save_entry(entry):
    """Writes user's journal entry and datetime information to a .txt file and
    iterates file_information.json['entry_count'] by 1
    
    Arguments:
        entry -- Object containing formatted text header and filename
        
    """
    
    entry.json_obj.update_count()   

    with open(os.path.join(Directory.ENTRIES, entry.filename), 'w') as f_obj:
        f_obj.writelines(entry.body)
        f_obj.writelines(entry.entry)
    
    print("Entry saved to {}".format(Directory.ENTRIES))
    
if __name__ == '__main__':
    #test case(s)
    file_data = JsonData()
    file_data.update_count()
    print(file_data.data)
    
  
