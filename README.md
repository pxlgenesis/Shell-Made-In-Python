Shell building project using python.

NOTE TO SELF: 
1.PYTHON IS CASE SENSITIVE.
2.For some reason program doesnt terminate on sys.exit(0) or return 0 in the main() for some reason while using visual studio but works fine in the terminal.
3.Used def func for each command.
4.Split is is used to cut commands into multiple parts. and then dictionary can be used to match it out.
5.regex is the way to go but too complex.
6. os.path.isfile: to check if file is present. os.access(path,os.X_OK) to check that the user privilages are enough.
7.shutil is used for high level operations for the file.
8.os.[] has important file handing functions.
9.isdir checks for directory and isfile checks for a executable file.
10.Join is can be used to join variables in a list with desired separator.
11.prompttoolkit is useful during user input operations.

v[0.1]
Task-To-Implement:
1.REPL (READ-EVAL-PRINT-LOOP): executes command after command like a terminal does.
2.EXIT: Implemented status 0 on typin "exit 0". 
3.ECHO: 1. implemented to read echo and differentiate from illegal      words like "echo34" or "echo%" for now. and changed both of them to be executed as functions.(echo strips the first 5 words of each message)
        2.Rewored echo to recognizse seprators.
        3.Reworked echo to recognize Redirect stdout & stdin

4.TYPE: Shows if or not the command is present in the shell.
5.CUSTOM COMMANDS: 1. checks for command and command path in bin. if present executes the command. 
                   2. Reworked to distinguished quoted commands.
6.PWD: outputs current working directory from os. 
7.CD: 1.changes directory on absolute path, relative and ~ for home.
      2.Reworked cd to recognize seprators.
8.AUTOCOMPLETE: autocompletes all builting commands.
    