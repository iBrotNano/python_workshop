class Tier:

    def sound(self):
        pass


class Katze(Tier):

    def __init__(self, amountColors=1, gender="f"):
        if amountColors > 3:
            raise Exception("Katzen haben maximal 3 Farben.")

        self.amountColors = amountColors

        if amountColors == 3:
            self.gender = "f"
        else:
            self.gender = gender

    def sound(self):
        print("Miau")


class Hund(Tier):
    def sound(self):
        print("Wuff")


class Vogel(Tier):
    def sound(self):
        print("Piep")


for tier in [Katze(), Hund(), Vogel()]:
    tier.sound()

katze = Katze(2, "m")
print(f"{katze.amountColors=}")
print(f"{katze.gender=}")

try:
    katze = Katze(4, "m")
except Exception as e:
    print(type(e), e)
