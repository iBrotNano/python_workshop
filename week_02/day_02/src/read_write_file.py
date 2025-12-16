user = {
    "firstname": "Max",
    "lastname": "Mustermann",
    "age": None,
    "country": "DE",
    "city": None,
    "zip": 12345,
    "hobbies": ["jogging", "trading", "mindset", "spammen", "ü"]
}

import json

filename = "..\\temp\\user.json"

def writeJson(obj, path):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(obj, file, indent=4, ensure_ascii=False)

writeJson(user, filename)

def readJson(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
    
data = readJson(filename)
print(data)

data["city"] = "Munich"
data["zip"] = 54321
data["hobbies"][0] = "hiking"
data["hobbies"].append("viking")
writeJson(data, filename)
print(readJson(filename))