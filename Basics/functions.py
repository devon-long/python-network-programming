def my_function(name):
    "This is a function!"
    print("Hello " + name)


my_function("Devon")

def sum_function(x,y):
    sum = x + y
    return sum

z = sum_function(3,4)
print(z)



def sum_default(x, y = 6):
    return x + y
print(sum_default(1))
print(sum_default(3,7))


def tuple_function(x, *args):
    print(x)
    for argument in args:
        print(argument)


tuple_function("hello", 100, 200)
tuple_function(1,2,3,4)
