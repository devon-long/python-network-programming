# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import myRouter

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   router1 = myRouter.MyRouter("R1", "2600", "123456", "12.4")
   router1.print_router("20221010")

   router2 = myRouter.MyRouter("R2", "7200", "101010", "12.2")
   router2.print_router("20210929")
   print(getattr(router2, "ios"))
   print(hasattr(router2, "model"))
   print(isinstance(router2, myRouter.MyRouter))

