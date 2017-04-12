#! python3

"""Program for logging simple journal entries"""
import sys
import journal_file_handling
import datetime_information


def get_entry():
    """Gets user's journal input and passes it to confirm_entry() based on
    selection input request after initial intry process"""

    print("** Begin log for {} **\n".format(
                                datetime_information.get_datetime()["date"]))
    
    user_entry = input("Entry #{}: ".format(
                                journal_file_handling.get_entry_count() + 1))
    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    #simple error checking process to make sure selector propperly chosen    
    selection_list = ["-s", "-e", "-qc"]    
    while selection not in selection_list:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
        
    if selection == "-qc":
        sys.exit("Entry Cancelled")
    else:
        confirm_entry(selection, user_entry)


def confirm_entry(selection, user_entry):
    """Processes user selection in get_entry() function
    
    Arguments:
    selection  -- string value that dictates which function is passed control
        "-s" selector saves the journal entry
        "-e" selector calls get_entry() so user can re-input entry        
    user_entry -- string that contains users journal entry
    
    """
       
    if selection == "-s":
        journal_file_handling.save_entry(user_entry)
    elif selection == "-e":
        get_entry()


if __name__ == '__main__':
    get_entry()



   