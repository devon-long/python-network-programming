import sys
import subprocess

# Checks if IP address is reachable with a ping
def ip_reach(list):
    for ip in list:
        ip = ip.rstrip("\n")

        # send 2 packets to ip and supress errors and output
        ping_response = subprocess.call('ping %s -n 2' % (ip), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        if ping_response == 0:
            print("\n* {} is reachable :)\n".format(ip))
            continue
        else:
            print("\n* {} is not reachable :)\n".format(ip))
            sys.exit()
