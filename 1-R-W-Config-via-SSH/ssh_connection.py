import cmd
import paramiko
import os.path
import time
import sys
import re


# Performs several tasks:
# Checks if credentials and command files are valid
# Uses credentials to open SSH to target device
# Creates a thread to each device and handles ssh data transfer



def file_does_not_exist(file_name):
    print("\n File {} does not exist. Please try again.\n".format(file_name))

def file_valid():
    print("\n File is valid.\n")

# Validate credential file
user_file = input("\n# enter Credential file path and name:")

if os.path.isfile(user_file) == True:
    file_valid()
else:
    file_does_not_exist(user_file)
    sys.exit()

# Validate commands file
cmd_file = input("\n# enter commands file path and name:")

if os.path.isfile(cmd_file) == True:
    file_valid()
else:
    file_does_not_exist(cmd_file)
    sys.exit()

def ssh_connection(ip):
    global user_file
    global cmd_file

    try:
        selected_user_file = open(user_file, 'r')
        selected_user_file.seek(0)
        username = selected_user_file.readlines()[0].split(',')[0].rstrip("\n")
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1].rstrip("\n")
        
        
        session = paramiko.SSHClient()
        # CAUTION: allow/deny host keys from unknown servers - in prod env, only accept keys from known hosts
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Connect with username and password
        session.connect(ip.rstrip("\n"), username=username, password=password)
        
        # open shell on target device
        connection = session.invoke_shell()

        # 
        connection.send("enable\n")
        connection.send("terminal length 0\n")
        time.sleep(1)

        # Enter global config mode
        connection.send("\n")
        connection.send("configure terminal\n")
        time.sleep(1)

        # Open cmd_file
        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)

        for command in selected_cmd_file.readlines():
            connection.send(command + '\n')
            time.sleep(2)

        selected_cmd_file.close()
        selected_user_file.close()

        # Show  65535 bytes of connection output
        router_output = connection.recv(65535)

        if re.search(b"% Invalid input", router_output):
            print("There was invalid input on device: {}\n".format(ip))
        else:
            print("Commands complete on {}\n".format(ip))

        # print(str(router_output))

        session.close()

    except paramiko.AuthenticationException:
        print("Invalid username or password.")
