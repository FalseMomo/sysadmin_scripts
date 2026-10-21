#!/usr/bin/env python3

import os
import pathlib
import subprocess

def create_symbolic_link():
    """ creates a symbolic link """

    # finds the user's home directory
    home = pathlib.Path.home()

    # prompts user to enter the file to link
    user = input("\033[36mEnter a filename to create a shortcut: \033[0m ").strip()

    # searches for matches
    try:
        matches = []
        for path in pathlib.Path("/").rglob('*'):
            try:
                if path.is_file() and user.lower() == path.name.lower():
                    matches.append(path)
            except Exception:
                continue
    except Exception:
        print("\033[31mThat file doesn't exist!\033[0m\n")
        return 

    if len(matches) == 0:
        print("\033[31mThat file doesn't exist!\033[0m")
        return

    # handle matching files
    if len(matches) == 1:
        file = matches[0]
    else:
        print("\033[36mThere is more than one file with that name: \033[0m\n")

        for i in range(len(matches)):
            print(i+1, ": ",  matches[i])
        print()

        try: 
            selection = int(input("\033[36mPlease select the file to create a shortcut for: \033[0m"))
            if (selection < 1) or (selection > len(matches)):
                print("\033[31mInvalid selection! Returning to menu...\033[0m\n")
                return

            file = matches[selection-1]
        except ValueError:
            print("\033[31mNon-numeric input! Returning to menu...\033[0m\n")
            return

    # creates the symbolic link in the home folder
    link = home/(file.name + "_link")

    if file.exists():
        choice = input(str(file) + "\033[36m was found. Would you like to create a shortcut? [Y/y]: \033[0m")
        if choice.lower() == "y": 
            try:
                os.symlink(file, link)
                print("\033[32mSymbolic link created:\033[0m ", file, "\n")
            except FileExistsError:
                print("\033[31mA file with that name already exists!\n\033[0m")
            except Exception as exception:
                print("\033[31mException: \033[0m ", exception, "\n")
        else:
            print("\033[31mYou did not confirm the shortcut creation. Returning to menu...\033[0m\n")
            return

def delete_symbolic_link():
    """ deletes a symbolic link """

    # finds the user's home directory
    home = pathlib.Path.home()

    # prompts the user to enter the link to delete
    link = input("\033[36mEnter the link name to delete: \033[0m").strip()

    # searches for the symbolic link in the home directory
    for item in home.iterdir():
        
        # checks if the item is a symbolic link and is what the user is looking for
        if item.is_symlink() and link in item.name.lower():

            # confirms deletion
            choice = input(str(link) + "\033[36m was found. Would you like to delete the shortcut? [Y/y]: \033[0m")
            if choice.lower() == "y":
                try:
                    item.unlink()
                    print("\033[32mDeleted symbolic link: \033[0m", item.name, "\n")
                except Exception as exception:
                    print("\033[31mException: \033[0m ", exception)
                return 
            else:
                print("\033[31mYou did not confirm the shortcut deletion. Returning to menu...\n\033[0m")
                return 

    # lets the user know the link was not found
    print(link, " \033[31m was not found as a symbolic link! \033[0m\n")

def generate_report():
    """ generates a report on all symbolic links """

    # finds the user's home directory
    home = pathlib.Path.home()

    # prints the symbolic report header
    print("\033[36m\nSymbolic Link Report\n\033[0m")
    print("\033[36mCurrent Working Directory: \033[0m ", os.getcwd(), "\n")
    
    count = 0

    for item in home.rglob('*'):
        if item.is_symlink():
            count+=1

    print("\033[36mLinks:\033[0m", count)
    for item in home.rglob('*'):
        if item.is_symlink():
            try: 
                print(item)
            except Exception as exception:
                print("\033[31m Exception: \033[0m", exception)
    
    print()

def main():

    # clear the terminal when run
    subprocess.call("clear", shell=True)

    while(True):

        # print welcome message
        print("\033[35mWelcome to the Shortcut Creator!\033[0m\n")

        # print current working directory
        print("\033[35mCurrent Working Directory:\033[0m ", os.getcwd(), "\n")

        # print menu
        print("\t[1] Create a symbolic link\n\t[2] Delete a symbolic link\n\t[3] Generate a symbolic link report\n\t[4] Quit\n")

        # take user input
        userInput = input("\033[35mPlease make a selection (1-4):\033[0m ") 
        
        # creates a symbolic link
        if userInput.strip() == "1":
            create_symbolic_link()

        # deletes a symbolic link
        elif userInput.strip() == "2":
            delete_symbolic_link()

        # generates a symbolic link report
        elif userInput.strip() == "3":
            generate_report()

        # quits the program gracefully
        elif userInput.strip() == "4":
            print("\033[32mThanks for choosing us!\033[0m")
            break
        
        # handles invalid input
        else:
            print("\033[31mYou entered an invalid option!\033[0m")
            continue

if __name__ == "__main__":
    main()
