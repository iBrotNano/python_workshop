myList = [1,2,3,4]
myPointer = myList
myCopy = myList[:]

userData = {
    "vorname": "Maxi",
    "nachname": "Musterfrau",
    "anrede": "Frau",
    "alter": 29,
    "beruf": "Programmiererin",
    "hobbies": ["schwimmen", "joggen", "katzen", "puzzeln"],
    "bsp": {
        "key1": 1,
        "key2": 2,
        "key3": {
            "xkey1": 100,
            "xkey2": 200
        }
    }
}

dictPoint = userData
dictPoint["hallo"] = "ja, huhu was geht"
dictPoint["vorname"] = "Maxi"
print("dictPoint:", dictPoint)
print("userData:", userData) # Both are identical

shallowDict = userData.copy()
dictPoint["vorname"] = "Mini"
shallowDict["hi"] = "jo what's .pop('in')?"
shallowDict["hobbies"].append("klettern")
print("shallowDict:", shallowDict)
print("userData:", userData)

import copy

deepCopy = copy.deepcopy(userData)
deepCopy["hobbies"].append("essen")
print("deepCopy:", deepCopy)
print("userData:", userData)

# Recap
def myFunc(li):
    li.append(100)

myList = [1,2,3]
myFunc(myList) # Pointer
myFunc(myList[:]) # Copy
print(myList)

def myFunc(di):
    di["hobbies"].append("schach")

myFunc(userData)
print(userData)
myFunc(copy.deepcopy(userData))