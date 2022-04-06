import os.path
import sys


# Checks wether file provided by the user exists in local system
# Reads file, checks if IPs in file exist and extracts IPs
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
    ip_file_reader.seek(0) # start from beginning of file
    ip_list = ip_file_reader.readlines()
    ip_file_reader.close()

    return ip_list

#ip_file_valid()