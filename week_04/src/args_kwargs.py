def myFunc1(*args):
    print(args)

    if args[0]:
        print(args[0])

    if args[1]:
        print(args[1])

    for arg in args:
        print(arg)


myFunc1(1, 2, 3)


def myFunc2(**kwargs):
    print(kwargs)

    if kwargs.get("pumpernickel"):
        print(kwargs["pumpernickel"])

    for key, val in kwargs.items():
        print(key, val)


myFunc2(a=1, b=2, c=3, pumpernickel="Brot")


def myFunc3(*args, **kwargs):
    print(type(args), args)
    print(type(kwargs), kwargs)


myFunc3(
    4,
    True,
    (1, 2, 3),
    {"firstname": "paul", "lastname": "Pokahontas"},
    food="kartoffel",
)
