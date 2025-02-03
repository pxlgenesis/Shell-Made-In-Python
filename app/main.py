import sys
import os 
import shutil #shell utilities.
import shlex #Simple lexical analysis.
from prompt_toolkit import prompt #toolkit used to autocomplete words.
from prompt_toolkit.completion import WordCompleter

def main():
        #REPL
    completer = WordCompleter(builtin,ignore_case=True)
    while True:

        # "$" initiation
        #Takes in an input
        command = prompt("$ ",completer=completer) 
        sys.stdout.flush()

        #Recognises status 0 on "exit 0"
        if command == "": #Blank input resets.
            main()
        elif  command.startswith("exit"):
            handle_exit(command)

        elif command.startswith("pwd"):
            handle_pwd(command)

        elif command.startswith("cd"):
            handle_cd(command)

        elif command.startswith("echo"):
            handle_echo(command)
        
        elif command.startswith("type"):
            handle_typecmd(command)
        
        elif handle_systemcommand(command):
            os.system(command) #Automatically prints output but print(os.system(command)) causes it to return code 0.
        else:
            #f"{}" stands for formmated string
            print_cmd_error(command)
    
def debug():
    print("works!")

def handle_systemcommand(message):
    message = shlex.split(message)
    if shutil.which(message[0]):
        return True
    return False

#Prints error message
def print_cmd_error(message):
    print(f"{message}: command not found")
    sys.stdout.flush()
    
#ECHO command to print out the message    
def handle_echo(message): #Searches for "<" anad ">" in echo command and redirects to os shell.
    if "<" in message  or ">" in message:
        os.system(message)
        return
    elif message.startswith("echo "): 
        message=message[5:].strip() 
        message=shlex.split(message)
        print(" ".join(message))
    elif message == "echo":
        print("")
    else:
        print_cmd_error(message)

#EXIT command to exit the program
def handle_exit(message):        
    if len(message)<5:
        print_cmd_error(message)
        return

    message=message.split(maxsplit=1)
    if len(message)==2 and message[1] =="0":    
        #Exiting with system(0)
        sys.exit(0)
    else:
        print_cmd_error(message[1])

#All commands in shell
builtin={"echo","exit","type","pwd","cd"}

#finding inbuilt commands and searches for given path and command in envior path.
def handle_typecmd(message):
    #splits message into "type" & follow up "command"
    message = message.split(maxsplit=1)
    
    #Checks if it split into two
    if len(message)==2:
        
        #Checks for command in builtin commands
        if message[1] in builtin:
            print(f"{message[1]} is a shell builtin")
            return
        
        #Retrive and Split current path, pathsep auto detects win or linux sepration
        path_dictry = os.environ.get("PATH","").split(os.pathsep)
        

        #Process and match the path
        for directory in path_dictry:
            Potential_path=os.path.join(directory,message[1])

            #Is file gives boolean if the path exists
            #Access does the same but for if the user can has exucatable access
            if os.path.isfile(Potential_path) and os.access(Potential_path,os.X_OK): #Is there a file and can we access it.
                print(f"{message[1]} is {Potential_path}")
                return
             
        print(f"{message[1]}: not found")
    else:
        print_cmd_error(message[0])

#shows current directory
def handle_pwd(message):
    message = message.split(maxsplit=1)
    if len(message) > 1:
        print_cmd_error(message[0])
        return
    elif message[0] == "pwd":
        #used to check current directory
        print(os.getcwd())  
        return
    else:
        print_cmd_error(message[0])

#handles cd commands for absoute, relative and HOME
def handle_cd(message):
    message = message.split(maxsplit=1)
    if (len(message) < 2):
        print_cmd_error(message[0])
        return
    if(len(message) == 2) and (message[1]=="~"):
        os.chdir(os.path.expanduser("~"))
        return

    if ((len(message) >= 2) and (os.path.isdir(message[1]) == True)):
        os.chdir(message[1])
        return
    else:
        print(f"cd: {message[1]}: No such file or directory")
        return

if __name__ == "__main__":
    main()
432