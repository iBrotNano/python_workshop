'''
count = 0

while True:
    count += 1
    print(count)
'''

'''
count = 0

while True:
    count += 1
    if count % 10000 == 0:
        print(count)
'''

while False:
    print("Hallo")

count = 0

while True:
    count += 1

    if count == 100:
        break

print(count)

count = 0

while count <= 100:
    count += 1

print(count)

count = 0
keepLoop = True

while count <= 100:
    count += 1

    if count == 50:
        keepLoop = False

    if not keepLoop:
        break

print(count)

simulation_success = 5
success = False

retry = 10

while retry >= 0:
    retry -= 1

    if retry == simulation_success:
        success = True
    
    if success:
        break
'''
count = 0

while True:
    count += 1
    print(count)
    continue

    if count == 10:
        break

print(count)
'''

count = 0
text = ""

while count <= 10:
    print(count)
    count += 1

    if count % 2 == 0:
        print("even")
        continue

    print("odd => concat x")
    text += "x"

print(text)

my2DList = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], [555, 2342, 6645, 32453]]

for innerList in my2DList:
    print(innerList[0])
    print(innerList[1])
    print(innerList[2])

for innerList in my2DList:
    for value in innerList:
        print(value)

my2DList = [ [1, 2, 3], [4, 5, 6], [7, 8, 9], "Hallo", 100, True, 42.0 ]

for currentObject in my2DList:
    # if type(currentObject) == list or type(currentObject) == str:
    if isinstance(currentObject, list):
        for val in currentObject:
            print(val)
    else: print(currentObject)

myList = [1, 2, 3, 4, 5]

for index, value in enumerate(myList):
    print("index =", index, "value =", value)



myList = [1, 2, 3, 4, 5]

for index, value in enumerate(myList):
    if index == len(myList) - 1:
        break
    
    myList[index + 1] = value

print(myList)