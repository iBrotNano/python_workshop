myList = []
print(myList)

myList = [1, 2, 3, 4, 5]
print(myList)
print(type(myList))

myListOfStrings = ["a", "b", "c", "d", "e"]
print(myListOfStrings)

myListOfIntAndStrings = [1, 2, "a", "b", 3, "c"]
print(myListOfIntAndStrings)

myListOfWhatNot = [1, "a", True, 2.5, None, [], [1, 2, 3], [[[]]], [[1, 2], [3, 4]], {}, ()]
print(myListOfWhatNot)

myListOfLogics = [str(1), 2 * 2, 5 + 5, 0 < 1, print("hallo"), print, type(myListOfWhatNot), myListOfWhatNot]
print(myListOfLogics)

myList =    [  1,  2,  3,  4,  5]
# Index        0   1   2   3   4
# Rev-Index   -5  -4  -3  -2  -1

myList = ["apple", "banana", "cherry", "kiwi", "elderberry"]
'''
INDEX   WERT            Nth value
0       "apple"         1st
1       "banana"        2nd
2       "cherry"        3rd
3       "kiwi"          4th
4       "elderberry"    5th 
'''

firstValue = myList[0]
secondValue = myList[1]
thirdValue = myList[2]
fourthValue = myList[3]
fifthValue = myList[4]

print(firstValue)
print(secondValue)
print(thirdValue)
print(fourthValue)
print(fifthValue)

lastValue = myList[-1]
print(lastValue)
secondLastValue = myList[-2]
print(secondLastValue)

# testForward = myList(10) # IndexError: list index out of range
# testBackward = myList(-6) # IndexError: list index out of range

lastViaLen = myList[len(myList)-1]
print(lastViaLen)

myList = ["apple", "banana", "cherry", "kiwi", "elderberry"]
newList = myList[0:2]
print(newList)

newList = myList[:2]
print(newList)

newList = myList[2:4]
print(newList)

newList = myList[2:]
print(newList)

newList = myList[2:-1]
print(newList)

copiedList = myList[:]
print(copiedList)

newList = myList[2:3]
print(newList)

newList = myList[2:2]
print(newList)

pointerList = myList
print(pointerList)

myList.append("mango")
print(myList)
print(pointerList)
print(copiedList)

myList.insert(0, "blueberry")
print(myList)

myList.insert(3, "raspberry")
print(myList)

myList.insert(100, "papaya")
print(myList)

myList.insert(-1, "pineapple")
print(myList)

poppedVal = myList.pop(9)
print(poppedVal)
print(myList)

poppedVal = myList.pop()
print(poppedVal)
print(myList)

del myList[1]
print(myList)

try:
    poppedVal = myList.pop(100)
    print(poppedVal)
    print(myList)
except IndexError as e:
    print("Error:", e)

try:
    del myList[100]
    print(myList)
except IndexError as e:
    print("Error:", e)

del myList[3:5]
print(myList)

myList[0] = "kiwi"
myList[1] = "banana"
print(myList)

myList[:2] = ["apple", "blueberry"]
print(myList)

addList = ["dragonfruit", "passionfruit"]
myList += addList
print(myList)

newMergedList = myList + copiedList + ["starfruit", "pitaya"]
print(newMergedList)

foundIndex = newMergedList.index("kiwi")
print(foundIndex)

del myList

try:
    print(myList)
except NameError as e:
    print("Error:", e)

my2DList = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(my2DList)
print(my2DList[0][0])
print(my2DList[1][2])
print(my2DList[0][-1])
print(my2DList[1][1])
print(my2DList[-2][-2])

myString = "Hello, World!"
myListFromString = list(myString)
print(myListFromString)

for char in myListFromString:
    print(char)

myString = ""

for char in myListFromString:
    print(myString)
    myString += char

print(myString)

separator = " "
mergedString = separator.join(myListFromString)
print(mergedString)

mergedString = "".join(myListFromString)
print(mergedString)

myList = [10, 20, 30, 40, 50]
total = 0

for value in myList:
    total += value

print("Total:", total)

for i in range(0, 10, 2):
    print(myListFromString[i])