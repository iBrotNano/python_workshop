# and

test = True and True
print(test)  # Expected output: True

test = True and False
print(test)  # Expected output: False

test = True and True and True and False
print(test)  # Expected output: False

test= 0 == 0 and 1 == 2
print(test)  # Expected output: False

# or

test = True or True
print(test)  # Expected output: True

test = True or False
print(test)  # Expected output: True

test = False or False or True or False
print(test)  # Expected output: True

test = False or False or False
print(test)  # Expected output: False

# ands first, then ors

test = True and False or True and False
print(test)  # Expected output: False

test = False or False or (False and True) or False or True
print(test)  # Expected output: True

test = (False or False or False) and (True or False or True)
print(test)  # Expected output: False

# Falsy values
# string ""
# Integert 0
# Float 0.0
# Boolean False
# None

a = ""

if a: print("a is truthy")
else: print("a is falsy")  # Expected output: a is falsy

a = 0

if a: print("a is truthy")
else: print("a is falsy")  # Expected output: a is falsy

a = 0.0

if a: print("a is truthy")
else: print("a is falsy")  # Expected output: a is falsy

a = False

if a: print("a is truthy")
else: print("a is falsy")  # Expected output: a is falsy

a = None

if a: print("a is truthy")
else: print("a is falsy")  # Expected output: a is falsy

test = "" and ""
print(test)  # Expected output: ""

test = "1" and "2"
print(test) # Expected output: "2"

test = "hallo" and "hallo" and "hallo" and ""
print(test)  # Expected output: ""

test = 1 and 2 and 0 and 3 and 4
print(test)  # Expected output: 0

if test: print("truthy")
else: print("falsy")  # Expected output: falsy

test = "" or ""
print(test)  # Expected output: ""

test = "1" or "2"
print(test)  # Expected output: "1"

test = "hello" or ""
print(test)  # Expected output: "hello"

test = "" or "hallo"
print(test)  # Expected output: "hallo"

test = "" or "" or "1" or "" or "2"
print(test)  # Expected output: "1"

try: test = "hallo" >= 0
except: print(test)

test = "aa" > "ab"
print(test)  # Expected output: False

test = 10 > 0.0
print(test)  # Expected output: True

test = 0 == 0.0
print(test)  # Expected output: True

test = True > 0
print(test)  # Expected output: True

test = True == 1
print(test)  # Expected output: True

test = False == 0.0
print(test)  # Expected output: True

test = "" != False
print(test)  # Expected output: True

test = not True
print(test)  # Expected output: False

test = not False
print(test)  # Expected output: True

test = not ""
print(test)  # Expected output: True

test = not "hallo"
print(test)  # Expected output: False

test = not 0
print(test)  # Expected output: True

test = not 42
print(test)  # Expected output: False

test = not None
print(test)  # Expected output: True

hobby = None

if not hobby:
    print("You need a hobby!")  # Expected output: You need a hobby!
else:
    print("Great hobby!")

response = None

if not response:
    print("some retry logik to ask OpenAI again x times ....")

if not response:
    response = "Default response because OpenAI did not respond in time."