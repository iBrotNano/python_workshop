# AUFGABE 1)

# a) Deklariere eine Liste mit dem Variablennamen myList und Werten von 0 bis 4
myList = [0, 1, 2, 3, 4]

# b) Gebe die Liste in der Konsole aus
print(myList)

# c) Füge mit der richtigen Methode an das Ende der Liste die Zahl 5 hinzu
myList.append(5)
print(myList)

# d) Entferne mit der richtigen Methode den Wert bei Index 0 aus der Liste
myList.pop(0)
print(myList)
# e) Programmiere eine Schleife, welche die Liste durchläuft, nenne die Schleifenvariable num, und gebe die Schleifenvariable in jedem Schleifenschritt in der Konsole aus.
for num in myList:
    print(num)
 
# AUFGABE 2) 
# a) Deklariere eine Liste mit dem Variablennamen myList und Werten von 1 bis 10
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b) Deklariere eine Variable namens summe und weise ihr den Wert 0 zu
summe = 0
# c) Programmiere eine Schleife, welche die Liste durchläuft, und addiere die Schleifenvariable in jedem Schleifenschritt auf die summe variable (kumulieren)
for num in myList:
    summe += num

print(summe)
# d) Erstelle eine Pseudo-Kopie (Pointer) von der myList und nenne sie aliasList
aliasList = myList
print(aliasList)
# e) Füge der Alias Liste bei Index 2 den Wert 100 hinzu (ohne Werte zu ersetzen)  
aliasList.insert(2, 100)
print(aliasList)
# f) Gebe die myList und die aliasList in der Konsole aus und schaue Dir die Ergebnisse an
print(myList)
print(aliasList)
# g) Erstelle eine echte Kopie der myList in einer neuen Liste namens newList
newList = myList[:]
print(newList)
# h) Ersetze in der newList den Wert bei Index 0 durch den Wert 1000
newList[0] = 100
print(newList)
# i) Gebe die myList und aliasList und newList in der Konsole aus und vergleiche die Ergebnisse
print(myList)
print(aliasList)
print(newList)
# j) Erstelle eine neue Liste namens partialList und weise ihr die ersten 3 Werte aus der myList zu.
partialList = myList[:3]
print(partialList)

# AUFGABE 3) 
# a) Deklariere eine Liste mit dem Variablennamen myList und den Werten: 0, 2, 4, 6, 8, 10
myList = [0, 2, 4, 6, 8, 10]
# b) Prüfe in jedem Schleifenschritt ob die Schleifenvariable größer als 4 ist. 
for num in myList:
    # b1) Ist dies der Fall, dann gebe die Schleifenvariable in der Konsole aus. 
    if num > 4:
        print(num)
    # b2) Ist dies nicht der Fall, dann gebe "value not greater 4" in der Konsole aus.
    else:
        print("value not greater 4")

# AUFGABE 4) 
# a) Lasse den User sein Geburtsjahr in der Konsole eingeben und speichere die Eingabe in einer Variable namens birthYear
# b) Wandele die Usereingabe in eine Zahl um
try:
    birthYear = int(input("Enter your birth year, please: "))
# c) Subtrahiere das Geburtsjahr des Users von dem laufenden Jahr 2025 und speichere das Ergebnis in einer Variablen namens caAge
    caAge = 2025 - birthYear
# d) Gebe den Text "Dein Alter ist ca." und die Variable caAge in der Konsole aus.
    print("Your age is " + str(caAge))
    
# f) Bonus: Versuche mit if und else eine Logik zu schreiben, die prüft ob das Alter des Users realistisch ist. Ist das Alter unrealistisch, dann gebe in der Konsole aus "Es ist unrealistisch, dass Du ca." caAge "Jahre alt bist". 
    if(caAge > 118):
        print("Congratulations! You are the oldest person in the world. (At least physically.)")
# e) Stelle sicher dass der Code nicht crasht, egal was der User eingibt
except Exception as e:
    print("Looks like a cat walked across the keyboard.")
    print(e)  