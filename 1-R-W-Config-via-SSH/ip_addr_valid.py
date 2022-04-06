import sys

# Checks if each IP is valid:
## Correct format
## Exists
## Not a reserved IP
def ip_addr_valid(ip_list):

    # turns each ip address into a list of 4 octets
    for ip in ip_list:
        ip = ip.rstrip("\n")
        octets = ip.split(".")

        # check if each ip is a reserved IP by inspecting each octet... Pull this into a separate validation class.
        if ((len(octets) == 4) and (1<= int(octets[0]) <= 223) and (int(octets[0]) != 127) and
        (int(octets[0]) != 169 or int(octets[1]) != 254) and (0 <= int(octets[1]) <= 225 and
        0 <= int(octets[2]) <= 225 and 0 <= int(octets[3]) <= 255)):
            continue
        else:
            print('\n* There was an invalid address in the file: {} :(\n'.format(ip))
            sys.exit()

ip_addr_valid(["10.10.10.2\n", "10.10.10.3\n"])