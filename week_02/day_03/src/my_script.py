# import json  # Uses my own script json.py. The build in module is not accessible anymore.
#
# print(json.myVar)
# test = json.dump()

import my_module

x = my_module.myVar
print("x:", x)

y = my_module.myFunction(10, 20)
print("y:", y)

import my_module as mm  # With a name

x = mm.myVar
print("x with mm:", x)

y = mm.myFunction(10, 20)
print("y with mm:", y)

from my_module import *  # Imports all from module directly into this script. Module name must not be used anymore.

x = myVar
print("x directly form my_module", x)

y = myFunction(10, 20)
print("y directly form my_module", y)

from my_module import myVar, myFunction  # Imports explicitly.

x = myVar
print("x explicitly imported:", x)
y = myFunction(10, 20)
print("y explicitly imported:", y)

from my_module import myVar as mv, myFunction as mf  # Imports explicitly with alias.

x = mv
print("x explicitly imported with name:", x)
y = mf(10, 20)
print("y explicitly imported with name:", y)

# Alternative
# from my_module import (
#     myVar as mv,
#     myFunction as mf
# )

import modules.my_module2 as mm2


x = mm2.myVar
print("x with mm2:", x)

y = mm2.myFunction(10, 20)
print("y with mm2:", y)
