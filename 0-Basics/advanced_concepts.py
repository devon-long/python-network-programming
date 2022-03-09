list1 = []
for i in range(10):
    result = i ** 2
    list1.append(result)

# List Comprehension version of the above for loop:
list2 = [x ** 2 for x in range(10)]

list3 = [x ** 2 for x in range(10) if x > 5]
#print(list3)

# Set Comprehension
set1 = {x ** 2 for x in range(10)}

# Dictionary Comprehension
dict1 = {x : x * 2 for x in range(10)}
#print(dict1.keys())

# Lambda functions
a = lambda x, y : x * y
# print(type(a))
# print(a(2, 10))
# print(a(7, 25))

def my_func(my_list):
    list_xy = []
    for x in range(10):
        for y in range(5):
            result = x * y
            list_xy.append(result)
    return list_xy + my_list

#print(my_func([100, 101, 102]))

# Replicate above function using Lambda + comprehension technique
b = lambda my_list: [x * y for x in range(10) for y in range(5)] + my_list
# print(b([100, 101, 102]))

# Map
def product10(a):
    return a * 10

r1 = range(10)

map(product10, r1)
# print(list(map(product10, r1)))
# print(list(map((lambda a: a * 10), r1)))

filter((lambda a: a > 5), r1)
# print(list(filter((lambda a: a > 5), r1)))

# ITERATORS
my_list = [1,2,3,4,5,6,7]
my_iter = iter(my_list)
# print(my_iter)
# print(next(my_iter))

# GENERATORS
# def my_gen(x,y):
#     for i in range(x):
#         print("i is %d" % i)
#         print("y is %d" % y)
#         yield i * y

# gen_object = my_gen(10, 5)
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))
# print(next(gen_object))

# GENERATOR EXPRESSION
gen_exp = (x for x in range(5))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))
# print(next(gen_exp))


# ITERTOOLS
from itertools import *

list4 = [1, 2, 3, "a", "b", "c"]
list5 = [101, 102, 103, "X", "Y"]

# chain(list4, list5)
# for i in chain(list4, list5):
    # print(i)

# OTHER ITERATORS
# count(start, step)
# cycle(range()) = repeatedly cycle through the range
# filterfalse(function, iterable sequence to filter) returns elements from sequence where function is false

# print(list(islice(range(10), 2, 9, 2)))

#DECORATORS
def my_decorator(target_function):
    def function_wrapper():
        return "Python is such a " + target_function() + " language!"
    return function_wrapper

@my_decorator
def target_function():
    return "cool"

print(target_function())

