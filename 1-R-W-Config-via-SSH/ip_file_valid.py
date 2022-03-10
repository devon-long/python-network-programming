import os.path
import sys


def ip_file_valid():

    # Prompt user for a file
    ip_file = input("Please enter file path and name (e.g. D:\Home\someFile.txt):  ")

    #Check if user's file is valid
    if os.path.isfile(ip_file):
        print("\n* File is valid \n")
    else:
        print("\n* File is not valid \n")
        sys.exit()
    
    # Read contents of file and store in list
    ip_file_reader = open(ip_file, 'r')
    ip_file_reader.seek(0)
    ip_list = ip_file_reader.readlines()
    ip_file_reader.close()

    return ip_list

