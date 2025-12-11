# Aufgabe 1)
# a) Erstelle eine Liste die den Text "Python" in getrennen Buchstaben enthält (Ein Buchstabe als String je Eintrag)
myList = list("Python")
print(myList)
# b) Führe die Buchstaben der Liste innerhalb von einer Codezeile zu dem Wort Python als String zusammen (Tipp: via join())
myString = "".join(myList)
print(myString)

# Aufgabe 2)
# a) Erstelle eine String Liste mit 6 Hauptstädten
cities = ["Nuuk", "Wien", "Bern", "Doha", "Lima", "Oslo"]
print(cities)
# b) Füge programmatisch eine Stadt an den Anfang der Liste, ohne Werte aus der Liste zu löschen/zu überschreiben
cities.insert(0, "Rom")
print(cities)
# c) Füge programmatisch eine Stadt an das Ende der Liste, ohne Werte aus der Liste zu löschen/zu überschreiben
cities.append("Madrid")
print(cities)
# d) Füge programmatisch eine Stadt bei Index 3 ein  ohne Werte aus der Liste zu löschen/zu überschreiben
cities.insert(3, "Paris")
print(cities)
# e) Ersetze programmatisch, die Stadt bei Index 5 durch eine andere statt (überschreiben)
cities[5] = "Berlin"
print(cities)
# f) Lösche programmatisch die letzten beiden städte aus der liste
del cities[-2:]
print(cities)
# g) Vertausche programmatisch die Position der letzten und ersten Hauptstadt in der Liste
cities[0], cities[-1] = cities[-1], cities[0]
print(cities)
# h) Gebe programmatisch innerhalb von einer Expression die ersten drei Hauptstädte aus der Liste in der Konsole aus
print(cities[:3])
# i) Führe die Städte der Liste innerhalb von einer Codezeile programmatisch zu einem Text zusammen und speichere das Ergebnis in der Variable cityText.
# j) Passe die Logik aus i) so an , dass die Städte in cityText durch ", " getrent sind. (Komma und Leerzeichen)
cityText = ", ".join(cities)
print(cityText)
# k) Lösche programmatisch die Variable der Liste mit den Hauptstädten aus der Memory (so als hätte sie nie existiert# 
del cities

# Aufgabe 3:
# a) Erstelle eine String Liste mit Zahlen von 1 bis 8
numbers = list(range(1, 9))
print(numbers)
# b) Erstelle eine Kopie dieser Liste und kehre in der selben Codezeile die Reihenfolge der Listeinträge für die neue Liste um.
numbersCopy= numbers[::-1]
print(numbersCopy)
# c) Kehre nun die Reihenfolge der neuen Liste noch einmal um, aber benutze diesmal ein anderes Verfahren als in b).
numbersCopy.reverse()
print(numbersCopy)
# d) Gebe innerhalb von einer Codezeile nur die geraden Zahlen der Liste in der Konsole aus, ohne die Liste (Cache) selbst zu manipulieren.
print(numbers[1::2])
# e) Gebe innerhalb von einer Codezeile nur die ungeraden Zahlen der Liste in der Konsole aus, ohne die Liste (Cache) selbst zu manipulieren.
print(numbers[::2])
# f) Leere die Liste inenrhalb von einer Codezeile
del numbers[:]
print(numbers)
# g) Füge der leeren Liste den Wert 10 und 11 hinzu.
numbers += [10, 11]
print(numbers)
# h) Ersetze den Wert 11 innerhalb von einer Codezeile durch den Wert 101
#numbers[-1] = 101
numbers[numbers.index(11)] = 101
print(numbers)
# i) Lösche die gesamte Liste aus dem Cache
del numbers
# j) VERSUCHE die gelöschte Liste in der Konsole auszugeben, ohne das der Code crasht.
# k) Wenn der Code crasht, soll der Error in der Konsole ausgeben werden.
try:
    print(numbers)
except Exception as e:
    print(e)

# Aufgabe 4)
# a) Erstelle einen While Loop und beende die Iteration Kopfgesteuert bei der 20ten Iteration.
count = 0

while count < 20:
    count += 1

print(count)
# b) Erstelle einen While Loop mit der Bedingung True, und beende die Iteration Fußgesteuert bei der 20ten Iteration.
count = 0

while True:
    count += 1

# c) Erweitere den Loop aus b) so, dass nur gerade Zahlen ausgegeben werden.
    if count % 2 == 0:
        print(count)

    if count == 20:
        break

print(count)



# Aufgabe 5)
# a) Erstelle innerhalb von einer Code Zeile eine Liste aus Zahlen von 1 bis 100.000 ohne eckige Klammern zu verwenden (Tipp: Nutze range() innerhalb von list()) und gebe die Länge der Liste in der Konsole aus
myList = list(range(1, 100_001))
print(len(myList))
# b) Mache Aufgabe a) aber verwende dieses Mal eckige Klammern und nicht list(), und gebe die Länge der Liste in der Konsole aus
myList = [i for i in range(1, 100_001)]
print(len(myList))
# c) Erstelle innerhalb von einer Codezeile eine Liste aus 25 Strings mit dem Wert "Hallo" (eckige klammern verwenden ist ok) und gebe die Länge der Liste in der Konsole aus
myList = ["Hallo" for _ in range(1, 26)]
print(myList)
print(len(myList))

# Aufgabe 6)
# a) Erstelle eine Liste namens 'numList' aus Zahlen 1 bis 6
numList = [1, 2, 3, 4, 5, 6]
# b) Erstelle eine weitere Liste und füge in diese Liste versch. Daten ein: 12, "Hallo", 3.4, True, und die erstellte numList
myList = [12, "Hallo", 3.4, True, numList]
# c) Erstelle einen For Loop um die Werte aus der Liste iterativ in der Konsole auszugeben
for i in myList:
# d) Neste innerhalb des Loops ein if Statement und prüfe darin ob die jew. Schleifenvariable vom Datentyp 'list' ist (um die numList zu finden)
    if type(i) == list:
# e) Wenn die Bedingung in diesem If True ergibt, dann neste in dem if Block einen weiteren For Loop, um die einzelnen Werte der numList auch iterativ in der Konsole auszugeben
        for j in i:
            print(j)
    else: print(i)
