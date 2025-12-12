# Aufgabe 1 – Arithmetische Operatoren
# a) Erstelle zwei Variablen (a und b) mit Zahlen deiner Wahl und berechne:
a = 3
b = 5
# b) Ihr Ergebnis nach Addition
print(a + b)
# c) Ihr Ergebnis nach Subtraktion
print(a - b)
# d) Ihr Ergebnis nach Multiplikation
print(a * b)
# e) Ihr Ergebnis nach Division
print(a / b)
# f) Ihr Ergebnis nach Floor Division
print(a // b)
# g) Ihr Ergebnis nach Modulo
print(a % b)
# h) Ihr Ergebnis nach Exponentialrechnug
print(a ** b)
# i) Führe die vorherigen Schritte einmal so dass variable a links und variable b rechts vom Operator steht, und dann nochmal in umgekehrt
print(a, "+", b, "=", a + b, "|", b, "+", a, "=", b + a)
print(a, "-", b, "=", a - b, "|", b, "-", a, "=", b - a)
print(a, "*", b, "=", a * b, "|", b, "*", a, "=", b * a)
print(a, "/", b, "=", a / b, "|", b, "/", a, "=", b / a)
print(a, "//", b, "=", a // b, "|", b, "//", a, "=", b // a)
print(a, "%", b, "=", a % b, "|", b, "%", a, "=", b % a)
print(a, "**", b, "=", a ** b, "|", b, "**", a, "=", b ** a)

# j) Berechne die Wurzel aus 36
print(36 ** 0.5)
# k) Gebe alle Ergebnisse in der Konsole (Terminal) aus

# Aufgabe 2 – Zuweisungsoperatoren
# a) Erstelle eine Variable a = 10
a = 10
print(a)
# b) Addiere 5 auf a mit +=
a += 5
print(a)
# c) Multipliziere a mit 2 mit *=
a *= 2
print(a)
# d) Reduziere a mit -= um 4
a -= 4
print(a)
# e) Dividiere a durch 2 mit /= und gib a nach jedem Schritt aus
a /= 2
print(a)

# Aufgabe 3 – Vergleichsoperatoren und Logikoperatoren
# a) Gib jeweils True oder False aus bei folgenden Prüfungen (nutze Kontrollstrukturen):

if not 5 != 5:
    print(False)
    
if 8 >= 7:
    print(True)
    
if 2 <= 2:
    print(True)

# b) Kombiniere die drei Bedingungen mit dem 'and' Operator und füge ein Kommentar mit dem zu erwartenden Ergbnis hinzu. 
# Danach gebe die Ergbnisse in der Konsole aus
check = 5 != 5 and 8 >= 7 and 2 <= 2 # False
print(check)

# c) Kombiniere die drei Bedingungen Werte mit dem 'or' Operator und füge ein Kommentar mit dem zu erwartenden Ergbnis hinzu. 
# Danach gebe die Ergbnisse in der Konsole aus
check = 5 != 5 or 8 >= 7 or 2 <= 2 # True
print(check)

# d) Führe b) und c) nochmal aus aber negiere jede Bedingung
check = not 5 != 5 and not 8 >= 7 and not 2 <= 2 # False
print(check)
check = not 5 != 5 or not 8 >= 7 or not 2 <= 2 # True
print(check)

# e) Führe d) nochmal aus aber ummantele die gesamte Bedingungskette innerhaln runder Klammern und negiere dann vor der Klammer
check = not (not 5 != 5 and not 8 >= 7 and not 2 <= 2) # True
print(check)
check = not (not 5 != 5 or not 8 >= 7 or not 2 <= 2) # False
print(check)

# Aufgabe 4) – Listen und Loops
# a) Erstelle eine Liste namens 'numList' aus Zahlen 1 bis 6
numList = list(range(1, 7))
print(numList)
# b) Erstelle eine weitere Liste namens 'mixList' und füge in diese Liste versch. Datentypen ein: Int, String, Float, Bool, und die erstellte numList
mixList = [5, "hallo", 3.3, True, numList]
# c) Erstelle einen Loop um die Werte aus der mixList iterativ in der Konsole auszugeben
for i in mixList:
# d) Transfer: Neste innerhalb des Loops ein if Statement und prüfe darin ob Datentyp 'list' auftaucht (um die numList zu finden)
    if type(i) == list:
        # f) Bonus: Finde innerhalb des im If genesteten Code Blocks den Index der numLst programmatisch heraus und gebe ihn in der Konsole aus
        print(mixList.index(i))
        # e) Transfer: Wenn die Bedingung in diesem If, True ergibt dann neste in dem if Block einen weiteren Loop, um die einzelnen Werte der numList auch iterativ in der Konsole auszugeben
        for j in i:
            print(j)
    else:
        print(i)

# Aufgabe 5 – Loops
# a) Erstelle einen While Loop mit der Bedingung True, und beende die Iteration Fußgesteuert bei der 20ten Iteration
counter = 0
while True:
    counter += 1
    if(counter == 20): break 
# b) Erstelle innerhalb von einer Code Zeile programmatisch eine Liste namens largeList aus Zahlen von 1 bis 100.000
largeList = list(range(1, 100_001))
# c) Gebe die Länge der largeList in der Konsole aus
print(len(largeList))
# d) Iteriere über die largeList und gebe innerhalb der Schleife den Wert der Schleifenvariable in der Konsole aus sofern diese ohne Restwert durch 2500 teilbar ist.
# e) Erstelle über dem Schleifenheader eine Variable namens kumul und weise dieser variable den wert 0 zu
kumul = 0
for i in largeList:
    if(i % 2500 == 0):
        print(i)
    
    kumul += i
    
print(kumul)
# f) Baue in der Schleife eine Logik ein, welche in jedem Schleifenschritt den Wert der Schleifenvariable der variable kumul hinzuaddiert

# Aufgabe 6 – Sequenzen, Casting, Loops
# a) Generiere programmatisch eine Liste namens myNums aus Integer Zahlen von 1 bis 9, aber rückwärts.
myNums = list(range(9, 0, -1))
print(myNums)
# b) Lese in einer Code Zeile programmatisch die Reihenfolge der Zahlen in myNums rückwärts und schreibe das Ergebnis in eine variable namens myRevNums
myRevNums = myNums[::-1]
print(myRevNums)
# c) Wandele beide listen jeweils in eine String um, sodass alle zahlen der jeweiligen Liste in ihrer Reihenfolge zu einem Text werden.
myNumsText = "".join(str(i) for i in myNums)
myRevNumsText = "".join(str(i) for i in myRevNums)
print(myNumsText)
print(myRevNumsText)
# d) Caste die beiden erstellten Strings zu Integer und addiere sie dann.
result = int(myNumsText) + int(myRevNumsText)
print(result)
# e) Wandele aus dem Ergbnis in eine neue Liste um, in welcher jede Zahl ein Item ist
items = [i for i in str(result)]
print(items)
# f) Iteriere über diese neue Liste, und .appende() den Wert der jeweils aktuellen Schleifenvariable and das ende der liste
# for i in items:
#     items.append(i) # Endlosschleife

# Aufgabe 7 - Loops
my2DList = [ [1, 2, 3], [1, 2, 3], [1, 2, 3] ]
# a) Loope so über die my2DList, dass alle integerwerte einzeln in der Konsole ausgegeben werden
for i in my2DList:
    for j in i:
        print(j)
# b) Loope so über die my2DList, dass die inneren Listen untereinander in der Konsole als String ausgeben werden:
for i in my2DList:
    print("".join(str(j) for j in i))
# b) Deklariere eine leere Liste namens flatList
flatList = []
# c) Schreibe alle Integerwerte aus my2DList programmatisch in die flatList, sodass die flatList eine 1-dimensionale Liste wird, und keine Zahl verloren geht.
for i in my2DList:
    for j in i:
        flatList.append(j)
        
print(flatList)
# d) Sortiere die Werte in flatList nach aufsteigernder Wertigkeit
flatList.sort()
print(flatList)
# e) Ermittele programmatisch die Summe aller Zahlen in der flatList
cumulated = 0

for i in flatList:
    cumulated += i
    
print(cumulated)
# f) Nutze die flatList um programmatisch nur die ungeraden Werte in eine neue Liste namens oddsList zu schreiben.
oddsList = []

for i in flatList:
    if i % 2 != 0:
        oddsList.append(i)
        
print(oddsList)
# g) Nutze die flatList um programmatisch nur die geraden Werte in eine neue Liste namens evensList zu schreiben.
evensList = []

for i in flatList:
    if i % 2 == 0:
        evensList.append(i)
        
print(evensList)
# h) Entferne programmatisch die Mehrfachwerte aus der flatList, sodass jeder Wert nur einmal vorkommt (einzigartig) und schreibe das Ergbnis in eine neue Variable namens distinctList
distinctList = []
seen = []
for value in flatList:
    if value in seen:
        continue
    
    seen.append(value)
    distinctList.append(value)

print(distinctList)


# i) Nutze nur distinctList um programmatisch einen Loop zu bauen mit dem Du die my2DList rekonstruierst
counter = 0
new2DList = []

while counter < 3:
    new2DList.append(distinctList)
    counter += 1
    
print(new2DList)