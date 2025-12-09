a = True
b = False

if a == b:
    print("outer if was triggered")

    if a == False:
        print("inner if was triggered")
    elif b == False:
        print("inner elif was triggered")
    else:
        print("inner else was triggered")
else:
    print("outer else was triggered")

# Ad absurdum nested conditions example

a = 1
b = 2
c = 3
d = 4

if a >= 1:

    if b == 2:

        if c <= 3:
            print("1, 2, 3 conditions met")
        elif c == 4:
            print("1, 2, 4 conditions met")
        else:
            print("1, 2, other c condition met")

            if d < 4:
                print("1, 2, other c, d<4 conditions met")
            elif d == 4:
                print("1, 2, other c, d=4 conditions met")
            else:
                print("1, 2, other c, d>4 conditions met")
        