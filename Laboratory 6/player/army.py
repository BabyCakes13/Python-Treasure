"""Module which holds the Army class."""
import random


class Army:
    """Class which holds Army methods."""

    def __init__(self, name, fighters):
        """Initialises the name and fighter list for the army."""

        self.name = name
        self.fighters = fighters

    def __str__(self):
        """Returns the string representation of the class."""

        return str(self.__class__) + ": " + str(self.__dict__)

    def fight(self, enemies):
        """Fights armies in turns as long as each one has at least one fighter."""

        while True:
            attack(self, enemies)
            attack(enemies, self)


def focus_target(army):
    """Focuses a random target from the army list."""

    try:
        position = random.randint(0, len(army) - 1)
        target = army[position]

        return target

    except (IndexError, ValueError):

        return None


def attack(army, enemies):
    """Two random targets attack each other till no one is found."""

    enemy_target = focus_target(enemies.fighters)
    army_target = focus_target(army.fighters)

    if enemy_target is None:
        print("\n" + army.name + " WINS!")
        exit(0)
    elif army_target is None:
        print("\n" + enemies.name + " WINS!")
        exit(0)
    else:
        army_target.fight(enemy_target)


def print_army(army):
    """Pretty prints the armies."""

    print("\n" + army.name)

    for soldiers in army.fighters:
        print(soldiers)

    print("\n")
