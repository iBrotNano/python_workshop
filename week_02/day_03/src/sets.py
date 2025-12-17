mySet = {1, 2, 3}
print("mySet:", type(mySet), mySet)

mySet = {1, 2, 1, 3}
print("mySet:", type(mySet), mySet)  # Values are unique

myTuple = (1, 2, 1, 3, 1, 4, 2, 2, 5, 5, 8, 7, 8, 9, 9)
myTuple = tuple(set(myTuple))
print("myTuple:", myTuple)  # Works like a distinct. The order is not keep.

myList = [1, 2, 1, 3, 1, 4, 2, 2, 5, 5, 8, 7, 8, 9, 9]
myList = list(set(myList))
myList.sort()
print("myList:", myList)

mySet = {0, 1, 2, 3, 4, 5, 6}
mySet.discard(1)  # Throws no error when the element is not present.

try:
    mySet.remove(1)
except Exception as e:
    print(type(e), e)

print("mySet:", mySet)

set1a = {True, 1}
set1b = {1, True}
print("set1a:", set1a)
print("set1b", set1b)  # 1 and True is interpreted as the same in sets.

set1a = {False, 0}
set1b = {0, False}
print("set1a:", set1a)
print("set1b", set1b)

mySetOfWhatNot = {"Hallo", 4.7, "🐈", "Katze", "Cat", "😺", 5, 999, None, True, 0}
print("mySetOfWhatNot:", mySetOfWhatNot)
print("mySetOfWhatNot:", mySetOfWhatNot)
print(
    "mySetOfWhatNot:", mySetOfWhatNot
)  # Has the same order when run in the same execution. But has a different order next time the script runs.

mySetOfWhatNot.pop()  # No control what item is deleted.
print("mySetOfWhatNot:", mySetOfWhatNot)

try:
    valueAtIndex = mySetOfWhatNot[0]
except Exception as e:
    print(type(e), e)

if "😺" in mySetOfWhatNot:  # Faster than on lists and tuples.
    print("😺 is in set.")
else:
    print("😺 is not in set.")

print("SetLength:", len(mySetOfWhatNot))  # Faster than lists and tuples.

mySetOfWhatNot.clear()
print("mySetOfWhatNot:", mySetOfWhatNot)

myString = "Halllooooo Weeeellllltttt"
mySet = set(myString)
print("mySet:", mySet)

myHash = hash(myString)
print("myHash", myHash)
myHaxHash = hex(myHash)
print("myHaxHash:", myHaxHash)

myMemorySlotId = id(myString)
print("myMemorySlotId:", myMemorySlotId)
myHexId = hex(myMemorySlotId)
print("myHexId:", myHexId)

myFrozenSet = frozenset({"apples", "banana", "cherry"})
print("myFrozenSet:", type(myFrozenSet), myFrozenSet)

try:
    myFrozenSet.discard("apple")
except Exception as e:
    print(type(e), e)

try:
    myFrozenSet.add("strawberry")
except Exception as e:
    print(type(e), e)
