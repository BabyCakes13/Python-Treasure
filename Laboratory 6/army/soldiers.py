from army import soldier


class Bowman(soldier.Soldier):
    """Contains methods for bowman soldier."""

    def __init__(self, weapon):
        super().__init__(weapon, "Bowman", 30, 110, 30, False)

    def say_hurray(self):
        print("An archer cannot hit the bullseye if he doesn't know where the target is.")


class Swordsman(soldier.Soldier):

    def __init__(self, weapon):
        super().__init__(weapon, "Swordsman", 20, 100, 50, True)

    def say_hurray(self):
        print("When the sword is once drawn, the passions of men observe no bounds of moderation.")


class Scouter(soldier.Soldier):

    def __init__(self, weapon):
        super().__init__(weapon, "Scouter", 15, 50, 20, False)

    def say_hurray(self):
        print("I must not be too suspicious.")

    def inform_army(self):

        for people in self.army.fighters:
            people.acknowledge()
            print("I was informed by the Scouter.")
