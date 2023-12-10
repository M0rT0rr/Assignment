'''This is the Final assignment for python for networking security
    Created By Torrance Mooradian Student #000279721
    This was created using AI help and tutorials from class
    Date created: December 9th 2023'''

import os
# Import platform was found by asking chat GPT
import platform

operating_system = platform.system()


#Testing for file path
def OSdetail():
    if operating_system == "Windows":
        os.chdir("C:\\Windows\\System32\\drivers\\etc")
    elif operating_system == "Linux":
        os.chdir("/etc/")
    else:
        MyPath=input("Enter the absolute path of the directory containing your host file")
        try: 
            os.chdir(MyPath)
        except FileNotFoundError:
            print('''
                Please try the select the correct Operating System Distribution.
                If the -OS switch was used please use -OS linux''')

# This function is used to append and check for existing FQDN entry
# with open code found @https://pynative.com/python-delete-lines-from-file/


def fileappend(FQDN):
    Black="0.0.0.0       " + FQDN
    with open("hosts", "r") as fp:
        lines = fp.readlines()
        # This section removes white space from the hosts file 
        for line in lines:
            if not line.endswith("\n"):
                newline = line
                with open("hosts", "w") as fp:
                    for line in lines:
                        if line.strip("\n") != newline:
                            fp.write(line)
                    fp.write(line + "\n")
    for line in lines:
        if line.strip("\n") == Black:
            fileremove(FQDN)
            exit()
    files=open("hosts", mode="a")
    files.write(f"0.0.0.0       {FQDN}\n")
    files.close()

#This is the function made to remove a line from a file
#code was made with reference to https://pynative.com/python-delete-lines-from-file/
def fileremove(FQDN):
    White="0.0.0.0       " + FQDN
    with open("hosts", "r") as fp:
        lines = fp.readlines()
    
    for line in lines:
        if line.strip("\n") == White:
            removing=input(f"would you like to remove (yes/no) or modify {line} Enter only yes, no or modify:\n")
            if removing=="yes":
                with open("hosts", "w") as fp:
                    for line in lines:
                        if line.strip("\n") != White:
                                fp.write(line)
            elif removing =="modify":
                mod=input("Enter the modified FQDN\n")
                modified="0.0.0.0       " + mod
                with open("hosts", "w") as fp:
                    for line in lines:
                        if line.strip("\n") != White:
                                fp.write(line)
                    fp.write(modified)

def Readfile():
    with open("hosts", "r") as fp:
        lines = fp.readlines()
        for line in lines:
           print(line.strip('\n'))