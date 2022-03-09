import re

mystr = "You can learn any programming language, whether it is Python2, Python3, Perl, Java, javascript or PHP"

# re.match(pattern, string, optional flags)
a = re.match("You", mystr)
# returns match object
#print(a)

#print(a.group())
a = re.match("you", mystr, re.I)
#print(a.group())

a = re.search("you", mystr, re.I)
#print(a.group())

arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222        L"
# a = re.search(r"(.+?) +(\d) +(.+?)\s{2,}(\w)*", arp)
# print(a.group(0))
# print(a.group(1))
# print(a.group(2))
# print(a.group(3))
# print(a.group(4))
# print(a.groups())


# All different ways to represent 2 digits in a row:
# \d\d
# \d{2}
# [0-9][0-9]
a = re.findall(r"\d\d\.\d{2}\.[0-9][0-9]\.[0-9]{1,3}", arp)
# a is a list, can now use list methods
print(a)

# add perenthesis to turn each section of IP address into a 4 element tuple => tuple methods
a = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(a)


arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222    10.10.10.5    L"
b = re.findall(r"(\d\d)\.(\d{2})\.([0-9][0-9])\.([0-9]{1,3})", arp)
print(b)

arp = "22.22.22.1   0    b4:a9:5a:ff:c8:45 VLAN#222    10.10.10.5    L"
c = re.sub(r"\d", "7", arp)
print(type(c))