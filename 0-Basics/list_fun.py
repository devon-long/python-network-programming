list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
print(list1)
print(len(list1))
print(list1[2])
print(list1[-2])
# Does not work anymore in v3
#print(min(list1))

list1.append(1000)
print(list1)
del list1[4]
print(list1)
print(list1.pop(0))
print(list1)
list1.remove(-11)
print(list1)
list1.insert(2, "Nortel")
print(list1)

list2 = [5,55,555]
list1.extend(list2)
print(list1)

list1.append(10)
print(list1.count(10))

list2.append(1)
list2.append(70)
print(list2)
list2.sort()
print(list2)
print("=====================")
sorted(list2)
print(list2)
list2.reverse()
print(list2)

# Slicing lists is same as strings
# ex: list2[:3] prints first elements of list up to but not including index 3