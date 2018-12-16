"""Module which holds the Soldier class."""


class Soldier:
    """Class which holds methods for creating soldiers."""

    def __init__(self, weapon, typee, cost, attack, defense, armored):
        """Initialises the soldiers attributes."""

        self.weapon = weapon
        self.type = typee
        self.attack = attack
        self.defense = defense
        self.armored = armored
        self.cost = cost
        self.army = None

    def __str__(self):
        """Contains the string representation of the class."""

        return str(self.__class__) + ": " + str(self.__dict__)

    def acknowledge(self):
        """Gains defense when acknowledged."""

        self.defense += 30

    def die(self):
        """Remove soldier from army soldier list."""

        self.army.fighters.remove(self)

    def join(self, player, army):
        """Soldier joins army if the player has enough money and isn't already in another army.
        That would be treason."""

        if player.get_amount() >= self.cost:
            if self.army != "None":

                player.set_amount(player.get_amount() - self.cost)
                army.fighters.append(self)
                self.army = army

                print("Soldier " + self.type + " joined the " + self.army.name +
                      ".\nThe player has " + str(player.amount) + " coins left.\n")

            else:
                print("The soldier is already in another army.")

        else:
            print("Not enough money to buy the soldier.")

    def fight(self, enemy):
        """Method which handles two soldiers fighting.
        If one soldier is armoured, he takes 1/3 of the attack as loss
        and loses its armour after one hit."""

        if enemy.armored:

            enemy.defense -= self.attack / 3
            enemy.armored = False

        else:

            enemy.defense -= self.attack

        if enemy.defense < 0:

            enemy.die()

    def say_hurray(self):
        """Says a hurray."""
        pass
