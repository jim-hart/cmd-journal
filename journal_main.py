#! python3

"""Program for logging simple journal entries"""
import sys
import journal_file_handling
import datetime_information


def get_user_entry():
    """Gets user's journal input and passes it to confirm_entry() based on
    selection input request after initial entry process"""

    print("** Begin log for {} **\n".format(
                                datetime_information.get_datetime()["date"]))
    
    user_initial = input("Entry #{}: ".format(
                    journal_file_handling.process_json()["entry_count"]+1))
    user_final = "{} {}".format("", user_initial)
    selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
    
    #simple error checking process to make sure selector properly chosen
    selection_list = ["-s", "-e", "-qc"]    
    while selection not in selection_list:
        print("Error: Invalid Selection")
        selection = input("-s: save entry, -e: edit entry, -qc: quit & cancel: ")
        
    if selection == "-qc":
        sys.exit("Entry Cancelled")
    else:
        confirm_entry(selection, user_final)


def confirm_entry(selection, user_entry):
    """Processes user selection in get_user_entry() function
    
    Arguments:
    selection  -- string value that dictates which function is passed control
        "-s" selector saves the journal entry
        "-e" selector calls get_user_entry() so user can re-input entry        
    user_entry -- string that contains users journal entry
    
    """
       
    if selection == "-s":
        journal_file_handling.save_entry(user_entry)
    elif selection == "-e":
        get_user_entry()


if __name__ == '__main__':
    get_user_entry()



   