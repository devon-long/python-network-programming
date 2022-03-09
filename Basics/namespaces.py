# What is a namespace?
#     A space holding some variables, functions, classes that are created
# Built in namespace = built in python functios and classes
# Global namespace = all variables you define or import into program
# Local namespace = variables defined inside functions

# print, list, range belong to built in namespace
#print(list(range(10)))

# my_var is in global namespace and can be accessed anywhere in this .py file
my_var = 10
print(my_var)


def my_var_func():
    # my_var is in the Local namespace. Cannot be called outside of my_var_func()
    my_var = 10
    print(my_var)

my_global_var = 5
def new_var_func():
   # global my_global_var
    print(my_global_var)

new_var_func()

