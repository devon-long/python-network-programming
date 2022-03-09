for i in range(5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print(e, " --> you can't divide by 0")
    finally:
        print("This is printed no matter what")