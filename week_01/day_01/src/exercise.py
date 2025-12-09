# Aufgabe 1:
# a)

x = 10
y = 13
print(x + y)

# b)
v = 1
w = 2
x = 3
y = 4
z = 5
print(v, w, x, y, z)

# c)
print("''''''")

# Aufgabe 2:
# a)
try:
    print(int(input("Enter a number: ")) * 2)
except Exception as e:
    print("Error occurred: " + str(e))

# Aufgabe 3:
# a)
text_1 = "Katzen kratzen Kletterklötze klug und kräftig."
text_2 = "Flinke Fellpfoten fegen federleicht vorbei."
full_text = text_1 + " " + text_2
print(full_text)

# Aufgabe 4:
myVar1 = "Hallo"
myVar2 = 10
myVar3 = 3.7

# a)
print(myVar1 + str(myVar2))

# b)
print(type(myVar1), type(myVar2), type(myVar3))

# c)
print(myVar1 + str(myVar3))

# d)
print(str(myVar2) + " " + str(myVar3))

# e)
result = myVar2 / 2
print(result, type(result))

# f)
myResult = myVar2 / myVar3
print(myResult, type(myResult))

# g)
myResult2 = int(myResult)
print(myResult2, type(myResult2))

# h)
print((int(myResult * 100) / 100))

# i)
print(myVar1 * 10)

# j)
print(myVar2 * 10)

# k)
print(myVar3 * 10)

# Aufgabe 5:
# a)
try:
    result = x / 0
except Exception as e:
    print("Error occurred:")
# b)
    print(e)
# c)
    print(type(e))

# Aufgabe 6:
myFloat = 67.5
# a)
myType = type(myFloat)
print(myType)
# b)
print(type(myType))

# Aufgabe 7:
# a)
print("print")
# b)
print(print)
# c)
print(print())
# d)
try:
    print(myPrint)
except Exception as e:
    print("Error occurred:")
    print(e)
# e)
print(type)
# f)
print(type(print))
# g)
print(type(print()))
# h)
# a) gibt den String "print" aus
# b) gibt den Namen der Funktion print aus?
# c) gibt None aus, da print() nichts zurückgibt
# d) gibt eine Fehlermeldung aus, da myPrint nicht definiert ist
# e) gibt den Type von type aus
# f) gibt den Type der Funktion print aus
# g) gibt den NoneType aus, da print() nichts zurückgibt