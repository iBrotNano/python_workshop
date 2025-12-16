myTuple = (1, 2, 3)
print(myTuple)

myTuple = 1, 2, 3
print(myTuple)
print(type(myTuple))

a, b, c = myTuple
print(a, b, c)

a, b, c = 1, 2, 3

myList = [1, 2, 3]
a, b, c = myList
print(a, b, c)

myTuple = tuple(myList)
print(type(myTuple))

myList = list(myTuple)
print(type(myList))

myTuple = 1,
print(type(myTuple), myTuple)
myInt = 1
print(type(myInt))
myFloat = 1.
print(type(myFloat))

myTuple = 1,2,3,4,5,6

firstVal = myTuple[0]
secondVal = myTuple[1]
lastVal = myTuple[-1]

firstToThirdVal = myTuple[:3]
print(type(firstToThirdVal), firstToThirdVal)

reverseTuple = myTuple[::-1]
print(type(reverseTuple), reverseTuple)

copyOfMyTuple = myTuple[:]
print(type(copyOfMyTuple))

myTuple = 1,2,3,4,5,6

try: myTuple[0] = 100
except Exception as e: print(e)

try: myTuple.append(100)
except Exception as e: print(e)

try: myTuple.sort(100)
except Exception as e: print(e)

try: myTuple.reverse(100)
except Exception as e: print(e)

try: myTuple.insert(100)
except Exception as e: print(e)

try: myTuple.pop()
except Exception as e: print(e)

try: del myTuple[5]
except Exception as e: print(e)

del myTuple

try: print(myTuple)
except Exception as e: print(e)

myTuple = 1,2,3,4,5,6