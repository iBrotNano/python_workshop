äpfel = 10
birnen = 20
kumquats = 30

text1 = "Du hast 10 äpfel und 20 birnen und 30 kumquats"
print("text1:", text1)

text2 = (
    "Du hast "
    + str(äpfel)
    + " äpfel und "
    + str(birnen)
    + " birnen und "
    + str(kumquats)
    + " kumquats"
)

print("text2:", text2)

text3 = f"Du hast {äpfel} äpfel und {birnen} birnen und {kumquats} kumquats"
print("text3:", text3)

text4 = f"Du hast {äpfel=} und {birnen=} und {kumquats=}"
print("text3:", text4)
print(f"{text4}")

userDb = {
    1: {"firstname": "Adrian", "lastname": "Ahnsdorf", "gender": "m"},
    2: {"firstname": "Beate", "lastname": "Bach", "gender": "f"},
    3: {"firstname": "Christian", "lastname": "Ceaser", "gender": "m"},
    4: {"firstname": "Doro", "lastname": "Dallmann", "gender": "d"},
    5: {"firstname": "Edeltraut", "lastname": "Ermke", "gender": "f"},
}

prefixMap = {"m": ["Lieber", "Herr"], "f": ["Liebe", "Frau"], "d": ["Hallo", ""]}

for key, value in userDb.items():
    isDiverse = value["gender"] == "d"
    prefixAndName = ""

    if isDiverse:
        prefixAndName = f"{value["firstname"]} {value["lastname"]}"
    else:
        prefixAndName = f"{prefixMap[value["gender"]][1]} {value['lastname']}"

    greeting = f"{prefixMap[value["gender"]][0]} {prefixAndName}"
    print(key, greeting)

pi = 3.14159
roundedFString = f"{pi:.2f}"  # Rounded
print(f"{roundedFString=}")

castedBackToFloat = float(roundedFString)
print(f"{castedBackToFloat=}")

castedBackToFloatAndCalc = castedBackToFloat + 1
print(f"{castedBackToFloatAndCalc=}")

name = "Maxi"
print(f"{name:>100}")
print(f"{name:<100}")
print(f"{name:^100}")

rate = 0.75
print(f"{rate:.0%}")

from datetime import datetime, timezone

now = datetime.now()
print(f"{now=}")
print(f"{now:%Y-%m-%d}")
print(f"{now:%H:%M:%S}")

weekday = datetime.isoweekday(now)
print(f"{weekday=}")

now_utc = datetime.utcnow()
print(f"{now_utc=}")

now_utc = datetime.now(timezone.utc)
print(f"{now_utc=}")
print(now_utc)
