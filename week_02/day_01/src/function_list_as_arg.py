myList = [1,2,3,4,5]

def myFunc(li):
    li.append(6)

myFunc(myList) # Pointer
print(myList)

myList = [1,2,3,4,5]

def myFunc(li):
    li.append(6)

myFunc(myList[:]) # Copy
print(myList)