def myFunc1():
    print("Hallo Welt")

def myFunc2():
    myFunc1()

myFunc2()

def myFunc1():
    print("Hallo Welt")

def myFunc2():
    myFunc1()

    try: myFunc3()
    except Exception as e: print(type(e), e)

myFunc2()

def myFunc3():
    print("Yayyy")

def myOuterFunc():
    def myInnerFunc():
        print("Hallo Welt ...")
    
    myInnerFunc()

myOuterFunc()

param = 42

def myOuterFunc(param):
    def myInnerFunc(p):
        nonlocal param # nonlocal works like global in this function. Every scope can have a variable named 'param'.
        print(param) # Works because it is known in this scope.
        param += 1
        print(p)
    
    myInnerFunc(param)

myOuterFunc(10)

