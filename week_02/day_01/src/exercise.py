# Übungen
# 
# ---
# 
## Aufgabe 1)
# - k) Deklariere ganz obem in skript eine globale leere liste namens 'all_results'
all_results = []

# - a) Erstelle eine Funktion namens '_pow()'
# - b) Die Funktion soll zwei parameter haben: base, expo
def _pow(base, expo):
# - c) Die Funktion soll eine exponentialrechnung vornehmen: den parameter 'base' hoch den parameter 'expo' rechnen
# - d) Die Funktion soll das ergebnis aus der Exponentialrechnung zurückgeben
    return base ** expo
# - e) Erstelle eine globale Liste namens 'bases' mit Zahlen von 1 bis 100

bases = list(range(1, 101))
# - f) Erstelle eine globale Liste namens 'expos' mit Zahlen von 0 bis 20, aber in abständen von 0.5
expos = [i * 0.5 for i in range(0, 41)]
# - g) Erstelle einen loop der die liste 'bases' iteriert
for base in bases:
# - h) Neste innerhalb dieses loops einen weiteren loop der über die liste 'expos' iteriert
    for exp in expos:
# - i) Inenerhalb des inneren loops soll die _pow() funktion aufgereufen und für die jeweile iteration die aktuellen basis-werte und exponenten an die funktion übergeben
# - j) Nehme den returnwert der funktion auch entgegen und gebe ihn in der konsole aus
        result = _pow(base, exp)
        print("Pow of", base, "and", exp, result)
# - l) Sorge dafür dass innerhalb des loops auch jedes ergebnis der funktion in die 'all_results' liste geschrieben wird
        all_results.append(result)
# - m) Nachdem de loop fertig ist soll die summe aller werte der 'all_results' gebildet wund in der konsole ausgegeben werden
sum = 0
for i in all_results: sum += i
print("Summe:", sum)
# - n) Nachdem de loop fertig ist soll die anzahl der werte in 'all_results' in der konsoel ausgegebn werden
print("Anzahl:", len(all_results))
# 
# ---
# 
## Aufgabe 2)
# - a) Erstelle eine Funktion namens 'myFunc()'
# - b) Die funktion soll einen parameter namens 'obj' haben
# - i) Erstelle eine globale liste namens 'listOfWhatNot' mit werten zu allen klassen die wir kennengelernt haben
listOfWhatNot = ["Hallo", 1, 2.0, True, None, [1,2,3], (1,2,3)]

def myFunc(obj):
# - c) In der funktion soll geprüft werden welche klasse bzw datentyp der parameter hat
# - d) die klasse von 'obj' soll dann in der funktion geprintet werden
    print(type(obj))
# - e) Wenn es sich bei der klasse von 'obj' um eine iterierbare klassse (sequenz) handelt, dann soll in der funktion ein loop über obj ausgeführt werden
    if isinstance(obj, list) or isinstance(obj, tuple):
        for index, value in enumerate(obj):
            print(type(value))
# - f) in dem loop soll nur bei jeder zweiten iteration der wert der schleifenvariable ausgegeben werden
            if index % 2 != 0:
                print(value)
# - g) Wenn es sich bei 'obj' um eine sequenz handelt dann soll am ende der funktion die anzahl der items in obj zurückgeben werden
        print(len(obj))
# - h) wenn 'obj' keine sequenz ist dann soll die funktion None zurückgeben
    else: print(None)

myFunc([42, 13])
myFunc(list(range(42, 1013)))
myFunc("Hallo")   

sumOfIndicies = 0
# - j) Erstelle einen loop (außerhalb der funktion) der über 'listOfWhatNot' iteriert und im loop die 'myFunc()' aufruft und den wert der schleifenvariable an 'myFunc()' übergibt
# - k) in dem loop soll auch der index der aktuellen iteration in der konsole ausgeben
for index, value in enumerate(listOfWhatNot):
    print("Index:", index, "Value:", myFunc(i))
# - l) In dem loop soll auch die summe aus den indizies kumuliert werden
    sumOfIndicies += index
# - m) Nach dem loop soll diese summe in der konsole ausgegeben werden
print(sumOfIndicies)
# 
# ---
# 
## Aufgabe 3) 
# - a) Schreibe eine Funktion namens 'myFunction()' die 5 parameter entgehen nimmt
# - b) der vierte parameter soll den defaultwert 4 und der fünfte parameter den defaultwert 5 haben
def myFunction(p1, p2, p3, p4 = 4, p5 = 5):
# - c) In der funktion soll die summe aus allen parametern gebildet werden
# - k) stelle innerhalb der funktion sicher dass der code nicht crasht, egal welcher datentyp an die parameter übergeben wird
    try:
        sum = p1 + p2 + p3 + p4 + p5
# - d) In der funktion soll das produkt aus allen parametern gebildet werden
        product = p1 * p2 * p3 * p4 * p5
# - e) Die Funktion soll summe und produkt returnen
        return sum, product
    except Exception as e: print(type(e), e)
# - f) Rufe die Funktion mit nur 3 positional arguments auf
print(myFunction(1, 2, 3))
# - g) Darunter: Rufe die mit 4 positional arguments auf
print(myFunction(1, 2, 3, 5))
# - h) Darunter: Rufe die mit 5 positional arguments auf
print(myFunction(1, 2, 3, 5, 8))
# - i) Darunter: Rufe die mit 2 positional arguments und 3 keyword arguments auf
print(myFunction(1, 2, p3 = 3, p4 = 5, p5 = 8))
# - j) Nehme die Returnwerte bei jedem funktionsaufruf korrekt entgegen und gebe die werte einzeln mit einem print() in der konsole aus
sum, product = myFunction(1, 2, 3)
print("Summe:", sum) 
print("Product:", product)

sum, product = myFunction(1, 2, 3, 5)
print("Summe:", sum) 
print("Product:", product)

sum, product = myFunction(1, 2, 3, 5, 8)
print("Summe:", sum) 
print("Product:", product)

sum, product = myFunction(1, 2, p3 = 3, p4 = 5, p5 = 8)
print("Summe:", sum) 
print("Product:", product)
# - l) Teste ob es funktioniert, und gebe im falle eines errors, den error und den datentyp der errormeldung in der konsole aus
myFunction(1,2,"Ahh")
# 
# ---
# 
## Aufgabe 4) 
# - a) Packe ein Tuple namens 'myIntTuple' mit 5 Integerwerten
myIntTuple = (1,2,3,5,8)
# - b) Entpacke das Tuple korrekt und gebe die einzelnen Werte mit einem print() in der Konsole aus
a, b, c, d, e = myIntTuple
print(a,b,c,d,e)
# - c) Erstelle innerhalb von einer code zeile ein neues Tuple namens 'myStrTuple' mit String-Werten von 1 bis 1000 
myStrTuple = [str(i) for i in list(range(1, 1001))]
# - d) Loope über das 'myStrTuple' und gebe mit einem print() innerhalb des loops den jeweils aktuellen index und wert aus
sum = 0

for index, value in enumerate(myStrTuple):
    print("Index:", index, "Value:", value)
# - e) Kumuliere innerhalb des Loops iterativ die werte des 'myStrTuple' als Integer
    sum += int(value)
# - f) Gebe die das Ergebnis der Kumulierung in der Konsole aus sobald der Loop vorbei ist

print("Sum:", sum)
# - g) Erstelle darunter eine globale Variable namens 'average' und weise ihr die Berechnung des Mittelwertes aller Werte als Integer in dem 'myStrTuple' zu

average = sum / len(myStrTuple)
# - h) gebe den Wert von 'average' in der Konsole aus
print("Average:", average)
# 
# ---
# 
## Aufgabe 5) Bonus
# 
# - a) schreibe eine Funktion namens 'myDeco()'
# - b) diese funktion soll den parameter 'func' haben
def myDeco(func):
# - c) Neste eine weitere Funktion namens 'myWrapper()' innerhalb der 'myDeco()' function.
    def myWrapper():
# - d) Die 'myWrapper()' Funktion soll zuerst den text "before test function" printen
        print("before test function")
# - e) Darunter soll die funktion exakt folgende Zeile habe: func()
        func()
# - f) Darunter soll die funktion den text "after test function" printen
        print("after test function")
    return myWrapper
# - g) Schreibe außer halb von 'myDeco()' auf globaler ebene eine neue funktion namens 'myTest()'
# - i) schreibe exakte folgende zeile direkt eine zeile über den header von 'myTest()': @myDeco()
@myDeco
def myTest():
# - h) Die 'myTest()' soll den text "function test" printen
    print("function test")
# - j) Rufe ganz unten im skript die 'myTest()' auf und führe das Skript aus
myTest()
# - k) Wenn Du in der Konsole folgendes bekommst ist alles richtig:
# - before function
# - function test
# - after test function
# - m) Hat es geklappt ??? Wenn ja, dann kopiere den code in ChatGPT und frage was dieser Code macht, welches Konzept dahinter steht und wofür dich diesses Konzept noch eignet
# @myDeco ist ein Dekorator für myTest(). Wird myTest() aufgerufen, wird myDeco() mit myTest() als übergebener Funktion  ausgeführt. myDeco() gibt aber die innere Function zurück bzw. den Pointer auf die Function. 
# --- 