# Übungen
#
# ---
## Aufgabe 1)
# a) Importiere die code bibliothek 'time'
import time

# b) Darunter: Füge folgende zeile ein: start = int(time.time() * 1000)
start = int(time.time() * 1000)
print(start)
# b) Erstelle eine Liste namens 'users' aus 10 leeren dictionaries
users = [{} for _ in range(1, 11)]
# c) Erstelle einen loop über die 'users' liste, sodass du den index (i) in der schleife verfügbar hast
for idx, val in enumerate(users):
    # d) Füge dem jeweiligen dictionary in dem jeweiligen schleifenschritt den key "user_id" mit dem wert i zu
    dict = users[idx]
    dict["user_id"] = idx
    dict["firstname"] = ""
    dict["lastname"] = ""
    dict["city"] = ""
    dict["signup_at"] = int(time.time() * 1000)
# e) Füge in jedem schleifenschritt dem jeweiligen dictionary auch folgende key-value-pairs hinzu:
# => "firstname": "", "lastname": "", "city": "", "signup_at": int(time.time() * 1000)

# f) füge am ende jedes schleifenschrittes folgende zeile hinzu: time.sleep(1)
# time.sleep(1)
# g) Wenn die Schleife fertig ist, printe das 'users' dictionary in die konsole
print(users)
end = int(time.time() * 1000)
# h) Darunter schreibe folgende zeile: end = int(time.time() * 1000)
# i) Darunter schreibe: print("duration: ", end - start, "milliseonds")
print("duration: ", end - start, "milliseconds")
#
# ---
#
## Aufgabe 2)
# a) Erzeuge innerhalb von eine code zeile ein dictionary mit integer keys von 0 bis 100 und weise den keys dabei jeweils werte von 100 bis 0 zu
#  => also {0: 100, 1: 99, 2: 98 ... 98: 2, 99: 1, 100: 0}
dict = {idx: val for idx, val in enumerate([i for i in range(0, 101)][::-1])}
print(dict)
# b) Lösche programmatisch den key 99
del dict[99]
print(dict)
# c) Lösche den Key der den Wert 50 hat indem du diesen wert programmatisch findest
del dict[list(dict.values()).index(50)]
print(dict)
# d) Lösche den letzten key programmatisch
dict.popitem()
print(dict)
# e) Überscheibe programmatisch den wert von key 1 mit mit dem Wert 1000
dict[1] = 1000
print(dict)
# f) Füge dem dictionary programmatisch einen neuen key 101 mit dem Wert 2000 hinzu
dict[101] = 2000
print(dict)
# g) Erstelle ein Tuple namens 'keys', dass nur die keys des dictionaries enthält
keys = tuple(dict.keys())
print(keys)
# h) Erstelle eine Liste names 'vals', die nur die values des dictionaries enthält
vals = list(dict.values())
print(vals)
# i) Merge 'keys'und 'vals zu einem neuen dictionary namens 'swapDict', sodass die 'vals' die keys und die 'keys' die values des 'swapDict' werden
swapDict = {v: k for k, v in dict.items()}
print("dict:", dict)
print("swapDict", swapDict)
# j) Loope über 'swapDict', um jeden wert des dictionaries einmal iterativ zu inkrementieren
for i, v in swapDict.items():
    swapDict[i] = v + 1

print(swapDict)
# k) Loope über das 'swapDict' um in jedem schleifenschritt den jeweiligen key zu löschen

for key in list(swapDict.keys()):
    del swapDict[key]

print(swapDict)
# l) Lösche alle keys des anderen dictionaries innerhalb von einer code zeile
dict.clear()
print(dict)
# m) Lösche 'swapDict' vollständig aus dem zwischenspeuicher so als hätte es nie existiert
del swapDict
#
# ---
#
## Aufgabe 3)
# a) Ertslle ein leeres dictionary namens 'myDict'
myDict = {}
# b) Erstelle innerhalb von einer code zeile eine liste namens 'myNums' mit Integers von 100 bis 150
myNums = [i for i in range(100, 151)]

# c) Loope über diese Liste und sorge dafür dass Du in jedem Schleifenschritt den jeweiligen wert (v) und index (i) aus der liste verfügbar hast
for i, v in enumerate(myNums):
    # d) In der Schleife: Füge dem 'myDict' einen neuen key mit wert hinzu. i soll als key und v soll als wert verwendet werden.
    myDict[i] = v
# e) Gebe nach der Schleife das geanze 'myDict' in der konsole aus

print(myDict)
# f) Erstelle ein neues leeres dictionary namens 'swappedDict'
swappedDict = {}
# g) Loope über das 'myDict', sodass du in jedem Schleifenschritt, um immer das ganze jeweilige item als Tuple verfügbar zu haben
for i in myDict.items():
    # h) Entpacke das jeweilige Tuple in der Schleife innerhalb von einer Zeile
    i, v = i
    # i) Weise in jedem Schleifenschritt dem 'swappedDict' den jeweiligen value des 'myDict' als key und den jeweiligen key des 'myDict' als value zu
    swappedDict[v] = i

print(f"{swappedDict=}")
# j) Erstelle einen variable namens 'pointerDict' die lediglich auf das 'myDict' pointed (Referenz)
pointerDict = myDict
# l) Erstelle eine variable namens 'shallowDict' die eine Shallow Copy des 'myDict' erzeugt
shallowDict = myDict.copy()
# m) Erstelle eine variable namens 'deepcopyDict' die eine vollstände Tiefenkopie Copy des 'myDict' erzeugt
import copy

deepcopyDict = copy.deepcopy(myDict)
# n) Erstelle darunter eine neue Schleife über das 'myDict' in dem du ohne ein Tuple entpacken zu müssen sowohl key als auch value in der schleife verfügbar hast
# o) In der Schleife: Weise jedem key einen neuen wert zu: und zwar eine liste welche die zahlenreihe von 0 bis wert des aktuellen value aus 'myDict' enthält
# p) Nach der Schleife: Gebe dir 'pointerDict' und  'shallowDict' und 'deepcopyDict' in der konsole aus und vergleiche die werte
# q) Darunter: Überschreibe 'shallowDict' mit einer neuen Shallow Copy des aktuellen 'myDict'
# r) Darunter: Überschreibe 'deepcopyDict' mit einer neuen deepcopy des aktuellen 'myDict'
# s) Darunter: Weise dem ersten key in 'pointerDict' folgenden String Wert zu: "Hallo"
# t) Darunter: Gebe dir 'pointerDict' und  'shallowDict' und 'deepcopyDict' in der konsole aus und vergleiche die werte
# u) Darunter: Schreibe eine Funktion namens: 'write_or_read_file()'
# v) Die funktion 'write_or_read_file()' soll 3 parameter haben: path, modus, obj
# w1) In der funktion, prüfe ob modus == "w" und ob obj Truthy ist, wenn ja baue in dem if block eine logik die eine json datei schreibt
# w2) Für den Schreibprozess soll 'path' parameter als filename, der 'modus' parameter als mode und der 'obj' parameter als datei inhalt dienen.
# x1) Darunter. In der funktion, prüfe ob modus == "r" ist, wenn ja baue in diesem if block eine logik die eine json datei liest
# x2) Für den Leseprozess soll 'path' parameter als filename, der 'modus' parameter als mode dienen.
# x3) Speichere den gelesenen inhalt in eine variable namens 'data'
# z1) Ummantele den gesamten funktionsinhalt mit einem try/except
# z2) Wenn es sich bei einem Funktionsaufruf um eine Schreibabsicht handelte, returne True
# z3) Wenn es sich bei einem Funktionsaufruf um eine Leseabsicht handelte, returne den wertd er 'data' variable
# z4) Sofern ein Error in der funktion stattfindet, returne None
# z5) Rufe die 'write_or_read_file()' einmal auf 'myDict' als json zu schreiben und danach noch einmal um 'myDict' zu lesen und zu printen
# z6) Darunter: Rufe die 'write_or_read_file()' 3 mal auf falsche Art und weise auf um Errors zu provozieren
# z7) Mache Dir Gedanken welche Aspekte man noch in die 'write_or_read_file()' bauen könnte, um sie weniger feheleranfällig zu machen
