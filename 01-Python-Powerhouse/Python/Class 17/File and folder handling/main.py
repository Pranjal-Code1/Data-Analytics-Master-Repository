from pathlib import Path
import os
import shutil

def create_folder():
    try:
        name = input("please tell your input name: ")
        p = Path(name)
        p.mkdir()  # "make directory" and is used to create new folders directly from a command-line interface
        print("Folder created successfully")
    except Exception as err:
        print(f"Sorry an error occur as {err}")


def read_file_folder():
    p = Path("")
    items = list(p.rglob("*"))
    for i, v in enumerate(items):
        print(f"{i +1}: {v}")


def update_folder():
    try:
        read_file_folder()
        old_name = input("Tell which folder your want to update: ")
        p = Path(old_name)
        if p.exists() and p.is_dir():
            new_name = input("Please tell your new folder name: ")
            new_p = Path(new_name)
            p.rename(new_p)
            print("Your folder name updated successfully")
        else:
            print("Sorry no such folder exist")

    except Exception as err:
        print(f"An error occured as {err}")


def delete_folder():
    try:
        read_file_folder()
        name = input("Tell which folder your want to delete: ")
        p = Path(name)
        if p.exists() and p.is_dir():
            p.rmdir() # os.rmdir() only deletes completely empty folders to prevent accidental data loss. 
            #shutil.rmtree(p) acts like a "force delete", clearing out the folder, its subfolders, and all files inside them in one go.
            print("Your folder deleted successfully")
        else:
            print("Sorry no such folder exist")

    except Exception as err:
        print(f"An error Occured as {err}")


def create_file():
    try:
        read_file_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if not p.exists():
            with open (name,"w") as fs:
                data = input("Write what you want in this file: ")
                fs.write(data)
            print("Your file created successfully")
        else:
            print("This name file already exist")
    
    except Exception as err:
        print(f"An error occured as {err}")


def read_file():
    try:
        read_file_folder()
        name = input("Please tell your file name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(name,'r') as fs:
                content = fs.read()
            print("Your content is: ")
            print(content)
        else:
            print("Sorry no such file exist")

    except Exception as err:
        print(f"An error occured as {err}")


def update_file():
    try:
        read_file_folder()
        name = input("Please enter your file name which you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("options ")
            print("1. For renaming the file")
            print("2. For appending something in the file ")
            print("3. For overwriting the file content ")
            choice = int(input("tell your choice : "))

            if choice ==1:
                new_name = input("Enter your new file name with extension: ")
                new_p = Path(new_name)
                if not new_p.exists():
                    p.rename(new_p)
                    print("Your file name changed successfully")
                
                else:
                    print("Sorry this name is already exist")

            if choice == 2:
                with open(name,'a') as fs:
                    data = input("what you want to append : ")
                    fs.write(" "+ data)
                print("Data appended successfully ")

            if choice == 3:
                with open(name,'w') as fs:
                    data = input("what you want to overwrite : ")
                    fs.write(data)
                print("Data changed successfully ")

    except Exception as err:
        print(f"An error occured as {err}")


def delete_file():
    try:
        read_file_folder()
        name = input("Enter your file name with extension : ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("File Deleted successfully")
        else:
            print("Sorry no such file exist")
    
    except Exception as err:
        print(f"An error occured as {err}")


while True:
    print("Option: ")

    print("1. Create a folder ")
    print("2. Read file and folders ")
    print("3. Update the folder ")
    print("4. Delete the folder ")
    print("5. Create a file ")
    print("6. Read a file ")
    print("7. Update a file ")
    print("8. Delete a file ")
    print("0. Exit the program")


    choice = int(input("Please chose your option: "))

    if choice == 0:  # This completely breaks the loop and closes the script
        print("Exiting program. Goodbye!")
        break

    elif choice == 1:
        create_folder()

    elif choice == 2:
        read_file_folder()

    elif choice == 3:
        update_folder()

    elif choice == 4:
        delete_folder()

    elif choice == 5:
        create_file()

    elif choice == 6:
        read_file()

    elif choice == 7:
        update_file()

    elif choice == 8:
        delete_file()
