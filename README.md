# cmd-journal
Command line tool for writing simple text-log entries.

## Automatic Formatting
The program will automatically format the journal filename and text body.  Functionality includes:

1. Automatic Filename Format
   - Filenames are automatically formatted so they can be easily organized and tracked.  Filename information includes:
        - Entry Number
        - Date 
        
2. Automatic Header Information
   - Text header is automatically formatted with the following information:
        - Date
        - Weekday
        - Time
        - Log Number
        
3. Automatic Text Body Formatting
   - Text body is enclosed begin and end labels to clearly indicate where your message starts and stops.

## Ease of Use
The program will automatically save your entry to a pre-determined directory, and it will confirm your entry message.  Features include:

1. Automatic Saving
    -  Once the journal entry is complete, the file is written to a .txt document in a specified folder
    
2. Simple Command Switches
   - Simple command switches offer the following functions
      - Save Entry
      - End text entry
      - Restart Entry
      - Quit without saving
      
3. No-hassle Line Breaks
    - Because end-of-input is signaled by a switch, the enter key can be used for easy line breaks

### *In Progress*
- [ ] Additional format checks (periods, spacing, etc...)
- [ ] Basic file encryption to keep body text, filenames, or both private
