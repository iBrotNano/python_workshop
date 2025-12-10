# AUFGABE 1) Wissensanwendung

myVar1 = -5
myVar2 = 0
myVar3 = 5.0

# a) Printe True, wenn die Summe aus allen drei Variablen größer ist als 0

print(myVar1 + myVar2 + myVar3 > 0) # False, da 0

# b) Printe True, wenn das Produkt aus allen drei Variablen kleiner ist als 0

print(myVar1 * myVar2 * myVar3 < 0) # False, da 0

# c) Printe True, wenn das Ergebnis aus myVar1 / myVar3 vom Typ Integer ist
print(type(myVar1 / myVar3) == int) # False, da float

# d) Printe False, wenn das Ergebnis aus myVar1 / myVar2 einen Error bewirkt
try:
    result = myVar1 / myVar2
except:
    print(False)  # Division durch Null bewirkt einen Fehler

# e) Printe True, wenn mindestens eine der drei variablen eine String ist
print(type(myVar1) == str or type(myVar2) == str or type(myVar3) == str) # False, da alle numerisch

# f) Printe True, wenn mindestens eine der drei variablen ein Float ist
print(type(myVar1) == float or type(myVar2) == float or type(myVar3) == float) # True, da myVar3 ein Float ist

# g) Printe True, wenn alle drei Variablen vom Typ Integer sind
print(type(myVar1) == int and type(myVar2) == int and type(myVar3) == int) # False, da myVar3 ein Float ist

# h1) Printe 1, wenn myVar1 kleiner ist als 0, ansonsten printe False
if myVar1 < 0:
    print(1)
else:
    print(False)

# h2) Nesting: Falls h1 Truthy, dann Printe 2, sofern myVar2 größer gleich -1 ist, ansonsten printe False
if myVar1 < 0:
    print(1)

    if myVar2 >= -1:
        print(2)
    else:
        print(False)
else:
    print(False)

# h3) Nesting: Falls h2 Truthy, dann Printe 3, sofern myVar3 größer ist als 5, ansonsten printe False
if myVar1 < 0:
    print(1)

    if myVar2 >= -1:
        print(2)

        if myVar3 > 5:
            print(3)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)

# AUFGABE 2) Wissenstransfer

# a) Lasse den User eine Eingabe machen, und sage dem Nutzer dabei "Guess the correct programing language"
# b) Speichere die Eingabe in der Variablen: userGuess
userGuess = input("Guess the correct programing language: ").lower().strip()

# g) Prüfe ob userGuess == "python" ist, wenn ja, printe: "YEAH, that's it you nailed it!"
if userGuess == "python":
    print("YEAH, that's it you nailed it!")
# c) Prüfe ob userGuess falsy ist, wenn ja dann printe: "please write something useful"
elif not userGuess:
    print("please write something useful")
# d) Prüfe ob userGuess mehr Zeichen hat als 6, wenn ja printe "target is shorter" (Tipp: len(userGuess) gibt anzahl zeichen)
elif len(userGuess) > 6:
    print("target is shorter")
# e) Prüfe ob userGuess weniger Zeichen hat als 6, wenn ja printe "target is longer"
elif len(userGuess) < 6:
    print("target is longer")
# f) Prüfe ob userGuess genau 6 Zeichen hat, wenn ja printe "not yet correct, but the number of chars is right tho :-)"
elif len(userGuess) == 6:
    print("not yet correct, but the number of chars is right tho :-)")
# h) Prüfe ob userGuess mit "p" beginnt, wenn ja printe "good start, but not yet right" (Tipp: userGuess.startswith("p") )
elif userGuess.startswith("p"):
    print("good start, but not yet right")
# i) Sorge dafür dass User nicht auf Groß-/Kleinschreibung achten muss (Tipp: userGuess.lower() wandelt string in kleinbuchstaben um)
# j) Sorge dafür, dass leerzeichen am anfang und ende entfernt werden (Tipp: userGuess.strip() entfernt äußere whitespaces)
# k) Arrangiere den Code so, dass die Zeichenverarbeitung nützlich greift und die Prüfungen eine sinnvolle Reihenfolge haben

# AUFGABE 3) Bonus 

# a) Lege eine Variable namens userBalance an und setze diese = 0
# b) Lasse den Nutzer eine Eingabe machen: Frage den Nutzer dabei "How long are you married?"
# c) Caste die Nutzereingabe als Integer
# d) Sorge dafür dass der Code nicht crasht egal was Nutzer eingibt
# e) Gebe im except bereich "invalid value" in Konsole aus
# f) Wenn Nutzer 0 eingibt, printe: "Enjoy Your Freedom 😎"
# g) Implementiere folgende Logik: Wenn nutzer verheiratet ist länger als:
#   - 0 Jahre, printe: "That's so lovely" 😻
#   - 10 Jahre, addiere 10 zur userBalance und printe: "Congratulations 🥰, you just won 10 free coins"
#   - 25 Jahre, addiere 25 zur userBalance und printe: "Wow 🥳🥰 Congratulations, you just won 50 free coins"
#   - 50 Jahre, addiere 50 zur userBalance und printe: "OMG!! 😻😻😻 Thats so beautiful, you just won 100 free coins"
# h) Wenn der Nutzer negative Zahl eingibt, triggere eine Error Meldung: raise Exception("Sorry, can't go back in time yet ^^")

# AUFGABE 4) Bonus 
# a) Lasse User eine Eingabe machen, und sage dem Nutzer dabei "Please type a base number you want to exponentiate"
# b) Speichere die Eingabe in die variable: baseNum
# c) Lasse User danach noch eine Eingabe machen, und sage dem Nutzer dabei "Please type an integer exponent number to calculate with"
# d) Speichere die Eingabe in die variable: expo
# e) Caste expo in integer
# f) Stelle sicher, dass expo > 1 ist, wenn nicht dann raise eine Exception mit der meldung "exponent must be > 1"
# g) Erstelle eine variable namens multiplier und konkateniere hierfür als strings den Multiplikationsoperator + baseNum
# h) Erstelle eine variable namens stringCalc: Konkateniere => baseNum + multiplier * (expo -1)
# i) Gebe stringCalc in Konsole aus
# j) Erstelle eine Variable namens: result => und weise folgendes zu: eval(stringCalc)
# k) Gebe result in der Konsole aus
# l) Gebe auch folgendes in Konsole aus: eval(baseNum + "**" + str(expo))
# m) Gebe auch folgendes in der Konsole aus: int(baseNum) ** expo
# n) Sorge dafür dass der code nicht crasht, und wenn ein error auftritt gebe diesen in der Konsole aus