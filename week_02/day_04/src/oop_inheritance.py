class Tier:

    def schlafen(self):
        print("zzz...")


class Hund(Tier):
    pass


class Katze(Tier):
    pass


h1 = Hund().schlafen()
k1 = Katze().schlafen()
