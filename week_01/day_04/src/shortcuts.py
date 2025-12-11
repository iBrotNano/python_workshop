myList = []

for i in range(0, 1000):
    myList.append(i)

print(len(myList))

myList = [i for i in range(0, 1000)]
print(len(myList))

myList = ["x" for _ in range(0, 1000)]
print(myList)

myList = [i * 10 for i in range(0, 1000)]
print(myList)
print(len(myList))

myList = [i for i in range(0, 100) if i % 2 == 0]
print(len(myList))
print(myList)

my2DList = [i for i in range(0, 3)]
print(my2DList)

my2DList = [[] for i in range(0, 3)]
print(my2DList)

my2DList = [[i for i in range(0, 3)] for _ in range(0, 3)]
print(my2DList)

listGeneratorA = [i for i in range(0, 3)]
listGeneratorB = [listGeneratorA for _ in range(0, 3)]
print(listGeneratorB)