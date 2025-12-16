def myFunc():
    a = 1 # Variable is declared in the scope of this function.
    b = 2
    return a, b

myVar = myFunc()
print(type(myVar), myVar)

a, b = myVar # Return value is unpacked from in variable stored return value of the function.
print(a, b)

a, b = myFunc() # Return value is unpacked immediately.
print(a, b)

a = 10
b = 20
print(a, b) # 10, 20

def myFunc():
    a = 1
    b = 2
    return a, b

myFunc()
print(a, b) # 10, 20

def myFunc():
    locA = 1
    locB = 2
    return locA, locB

myFunc()

try: print(locA, locB)
except Exception as e: print(type(e), e)

a = 10
b = 20

def myFunc():
    a = 1
    b = 2
    return a,b

a, b = myFunc()
print(a, b)

a = 10
b = 20

def myFunc():
    global a
    global b
    a += 1
    b = 22
    return a, b

myFunc()
print(a, b)

a = 10
b = 20

def myFunc():
    print(a) # Shadow variables are global variables. They can be used in the scope of the function, but are not writeable.
    print(b)

myFunc()