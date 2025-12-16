# Arguments are values passed into a function.
# Parameter are in the function header defined variables in the scope of the function.

def myFunc(a, b):
    a += 1
    b = 22
    return a, b

print(myFunc(10, 20))

def myFunc(a, b):
    a += 1
    b -= 1
    return a, b

a, b = myFunc(10, 20)
print(a, b)

try:
    myTuple = 1, 2, 3
    a. b = myTuple
except Exception as e:
    print(type(e), e)

def myFunc(a, b):
    print(a, b)

try: myFunc(1, 2, 3)
except Exception as e: print(type(e), e)

def myFunc(a, b, c = 30):
    print(a, b, c)

myFunc(10, 20)
myFunc(10, 20, 40)

# Default values must be placed at the end of the parameter list.
# def myFunc(a = 10, b, c = 20):
#     print(a, b, c)

# Keyword arguments

def myFunc(a, b, c):
    print(a, b, c)

myFunc(c = 10, b = 20, a = 30)

def myFunc(p1, p2, p3, dp1 = 10, dp2 = True):
    print(p1, p2, p3, dp1, dp2)

myFunc(13, 3, 42, dp2=False)

def myFunc(a, b, c):
    print(a, b, c)

myFunc(10, 20, c = 30)
myFunc(10, c = 30, b = 20)
# myFunc(10, c = 30, 20) # Positional args after keyword args are not allowed.

def myFunc(p1, p2, p3 = 30):
    print(p1, p2, p3)

try: myFunc(10, p3=30)
except Exception as e: print(type(e), e)

myFunc(10, 20, p3=30)
myFunc(10, p3=30, p2=20)
myFunc(10, p2=30, p3=20)
