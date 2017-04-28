# cmd-journal
A command line tool for writing simple, auto-cataloged text entries

## Installation

#### NOTE
While the program has consistently run locally without any issues, your experience may vary.  If you experience any problems, please submit it via the issue tracker so I can look into it.  

#### Requirements:
1) Python 3.5+ if you want to run the code directly using your local interpreter
2) Windows OS -- Debian-Linux coming soon

#### Instructions:
  - Option 1: If you have Python3.5+ on your computer, download/clone the repository and from your command line:

      ```
         >python "DirectoryPathToFile"\journal_main.py
      ```

- Option 2: Download the zip file [here](https://github.com/jim-hart/cmdjournal/raw/ca6413811e1deb9ffa8f1eaf6675b9a49b9fa871/journal_main.zip). You can then extract the file anywhere and run it from the folder. All your log-entries will be generated in whatever directory you run the program from by default. 

To get the most out of this utility, make a batch file that runs the executable, and add that batch file to a folder that's in your system path.  Using this method, you can enter the batch file's name via the run command (win+r) and the program will start.  

## Features

#### Automatic Formatting
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

#### Ease of Use
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

### *Progress*
- [x] Autoset directory information
- [ ] Let user choose new directory for entry files
- [ ] Basic file encryption to keep body text, filenames, or both private


<em>Application Icon Credit:</em> <a target="_blank" href="https://www.vexels.com/vectors/preview/128313/note-book-flat-icon"> link </a> |   Designed by Vexels.com
