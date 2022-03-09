myfile = open("routers.txt", "r")
print(myfile.read())
myfile.seek(0)
print(myfile.read(5))

myfile.seek(0)
for line in myfile.readlines():
    if line.startswith("A"):
        print(line)


# Remember to escape all special characters in path of file for read
# Ex: C:\Users\test\new\test.txt => \U, \t, \n are all escape characters and this filepath will creat an error
# Fix: C:\\Users\\test\\new\\test.txt 
# Or: (r"C:\Users\test\new\test.txt", "r")


# newfile = open("newfile.txt", "w")
# newfile.writelines(["Cisco", "Juniper", "HP"])
# newfile.close()

# newfile = open("newfile.txt", "a")
# newfile.writelines(" Apending this string!")
# newfile.close()

# newfile = open("newfile.txt", "w+")
# newfile.writelines("more lines!")
# newfile.seek(0)
# print(newfile.read())
# newfile.close()


# with as syntax eliminates need for calling close() on file
with open("newfile.txt", "w") as f:
    f.write("Hello world!!!!!!!")