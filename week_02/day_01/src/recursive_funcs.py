counter = 0

def myFunc():
    global counter
    counter += 1
    print(counter)
    myFunc()

try: myFunc() # Runs 999 times. This is the maximum recursion depth in Python.
except Exception as e: print(type(e), e)

def myFunc(p):
    print("p", p)

    if p <= 998:
        myFunc(p + 1)

    return p

result = myFunc(1)
print(result) # 1

def myFunc(p):
    print("p", p)

    if p <= 998:
        p = myFunc(p + 1)

    return p

result = myFunc(1)
print(result) # 999

def myFunc(p):
    if p <= 998:
        p = myFunc(p + 1)
        print(p)

result = myFunc(1)
print(result)