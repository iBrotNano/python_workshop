def myDecorator(func):
    def myWrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")

    return myWrapper


@myDecorator
def myTestFunction():
    print("This is a test function.")


@myDecorator
def myTestFunction2():
    print("This is a second test function.")


myTestFunction()
myTestFunction()
myTestFunction2()

import time


def performance(func):
    def wrapper():
        start_time = int(time.time() * 1000)
        func()
        end_time = int(time.time() * 1000)
        duration = end_time - start_time
        print(f"Function '{func.__name__}' executed in {duration} ms.")

    return wrapper


@performance
def myFunction1():
    myList = [i for i in range(1, 10_001)]


@performance
def myFunction2():
    myList = [i for i in range(1, 1_000_001)]


@performance
def myFunction3():
    myList = [i for i in range(1, 10_000_001)]


myFunction1()
myFunction2()
myFunction3()
