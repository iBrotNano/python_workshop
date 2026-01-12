def function1(p):
    return p + 1


def function2(p):
    return p + 2


def function3(p):
    return p + 3


def function4(p):
    return p + 4


def fallback(p=None):
    print("trigger some alternative action")
    return None


p = 1

if p == 1:
    result = function1(p)
elif p == 2:
    result = function2(p)
elif p == 3:
    result = function3(p)
elif p == 4:
    result = function4(p)
else:
    result = fallback(p)

print(f"{result=}")


myFunctionMap = {
    1: function1,
    2: function2,
    3: function3,
    4: function4,
}

dynFunction = myFunctionMap.get(p, fallback)
resultB = dynFunction(p)
print(f"{dynFunction=}")
print(f"{resultB=}")

match p:
    case 1:
        resultC = function1(p)
    case 2:
        resultC = function2(p)
    case 3:
        resultC = function3(p)
    case 4:
        resultC = function4(p)
    case _:
        resultC = fallback(p)

print(f"{resultC=}")
