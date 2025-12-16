myList = [i for i in range(1, 11)]

myData = {
    "programmieren": 1,
    "mit": 2,
    "python": 3,
    "ist": 4,
    "straight": 5,
    "forward": 6
}

print(myData)

mySwappedData = {v: k for k, v in myData.items()}
print(mySwappedData)

myList1 = ["a", "b", "c", "d"]
myList2 = [1, 2, 3, 4]

test = list(enumerate(myList1))
print(type(test), test)
mappedListDict = { val: myList2[idx] for idx, val in enumerate(myList1)}
print(mappedListDict)

myList1 = ["a", "b", "c", "d", "e", "f"]
myList2 = [1, 2, 3, 4]

mergedDict = dict(zip(myList1, myList2))
print(mergedDict)

# List must have the same length.
mergedDict = dict(zip(myList1, myList2, strict=True))
print(mergedDict)

myList1 = ["a", "b", "c", "d"]
myList2 = [1, 2, 3, 4, 5, 6]