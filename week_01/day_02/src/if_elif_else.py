my_var = 7

if my_var < 0:
    print("if was triggered")
elif my_var > 5:
    print("2nd elif was triggered")
elif my_var > 0:
    print("1st elif was triggered")
elif my_var >= 0:
    print("3rd elif was triggered")
else:
    print("none of the concrete conditions were met")

my_val = 10.0

if type(my_val) == int:
    print("value is of type integer")
elif type(my_val) == float:
    print("value is of type float")
elif type(my_val) == str:
    print("value is of type string")
elif type(my_val) == NoneType:
    print("value is of type NoneType")
elif type(my_val) == bool:
    print("value is of type boolean")
else:
    print("value is of some other type")

my_text = "Hallo Welt"

if my_text == "Hallo Welt":
    print("text is Hallo Welt")
else:
    print("text ist nicht Hallo Welt")