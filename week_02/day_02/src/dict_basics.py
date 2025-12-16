myDict = {} # Initializes a dictionary
print(type(myDict), myDict)

# Values
myDict = {"name": "Maxi"}
print(myDict)

# Read a value
name = myDict["name"]
print(name)

userData = {
    "vorname": "Maxi",
    "nachname": "Musterfrau",
    "anrede": "Frau",
    "alter": None,
    "beruf": "Programmiererin",
    "hobbies": ["schwimmen", "joggen", "katzen", "puzzlen"]
}

# Read values
prefix = userData["anrede"]
firstName = userData["vorname"]
lastName = userData["nachname"]
print(prefix, firstName, lastName)

# Set values
userData["alter"] = 30
print(userData["alter"])
userData["alter"] += 1
print(userData["alter"])

# Add new key value pairs
userData["city"] = "Melbourne"
userData["country"] = "Australia"
userData["languages"] = "en", "de"
print(userData)

# Loop through a dictionary
for key in userData:
    print(key, userData[key])

keys = userData.keys()
print(type(keys), keys)

try: keys[0] = "hallööö"
except Exception as e: print(type(e), e)

keys = list(keys)
print(type(keys), keys)

for key in userData.keys():
    print(userData[key])

for val in userData.values():
    print(val)

items = userData.items()
print(items)

for key, val in userData.items():
    print(key, val)

# Delete key-value pair
del userData["alter"]
print(userData)

try: print(userData["alter"])
except Exception as e: print(type(e), e)

# Alternative
userData.pop("city")

# Deletes last item
userData.popitem()
print(userData)