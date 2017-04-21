#! python3

"""Program for logging simple journal entries"""
import sys
import journal_file_handling
import datetime_information


def confirm_entry(selection):
    """Function will return True or False based on selection argument
    
    Arguments:
    selection  -- string value that dictates which function is passed control
        "-s" Returns True, resulting in main() passing control to save_entry()
        "-e" Returns False, resulting in main() allowing user to re-enter entry   
            
    """
       
    if selection == "-s":
        return True
    elif selection == "-e":
        return False

def main():
    """Gets user's journal input and passes it to confirm_entry() based on
    selection input request after initial entry process"""
    
    file_data = journal_file_handling.JsonData()
    
    print("** Begin log for {} **\n".format(
                                datetime_information.get_datetime()["date"]))
    
    user_initial = input("Entry #{}: ".format(file_data.data["entry_count"]+1))
    user_final = "{} {}".format("", user_initial)
    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    #simple error checking process to verify journal entry creation
    selection_list = ["-s", "-e", "-qc"]    
    while selection not in selection_list:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
        
    if selection == "-qc":
        sys.exit("Entry Cancelled")
    
    if confirm_entry(selection):
        journal_file_handling.save_entry(user_final, file_data)
   

if __name__ == '__main__':
    main()



   