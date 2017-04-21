#! python3

"""Functions for writing user input to files, and updating entry_count data"""

import json
import datetime_information

class Directory:
    """Holds directory information for files used in program"""
        
    JSON    = "Q:\\Git_Repos\\#Projects#\\cmd-journal\\json_data\\file_information.json"
    ENTRIES = "Q:\\GDrive\\Books & Notes\\Entries"

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
            self.data["entry_count"] += 1
            json.dump(self.data, f_obj, indent=4, sort_keys=True)


def save_entry(entry, file_data):
    """Writes user's journal entry and datetime information to a .txt file and
    iterates file_information.json by 1
    
    Arguments:
    entry -- string containing user's journal entry
        
    .txt header format example:
    
    Date: Jan-1-1970
    Day : Thursday    
    Time: 04:00:00
    Log#: 1
            
    Entry: <user's text here>       
    
    """
    
    file_data.update_count()        
    #datetime_information() stored in variable so it's only called once to avoid
    #possible time conflicts from three separate calls in a list literal
    date_information = datetime_information.get_datetime()
    file_information = ["Date: {}\n".format(date_information["date"]),
                        "Day : {}\n".format(date_information["day"]),
                        "Time: {}\n".format(date_information["time"]),
                        "Log#: {}\n\n".format(file_data.data["entry_count"]),
                        "Entry:{}".format(entry)]
     
    directory = Directory.ENTRIES
    filename = "{}\\Entry #{} -- {}.txt".format(
                                    directory, count, date_information["date"])

    with open(filename, "w") as f_obj:
        f_obj.writelines(file_information)
    
if __name__ == '__main__':
    #test case
    file_data = JsonData()
    file_data.update_count()
    print(file_data.data)
    
  
