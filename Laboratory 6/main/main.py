"""Module which creates the game."""
from player import army, player
from army import soldiers


def init():
    """Creates the game."""

    """create armies"""
    red_army = army.Army("Red Army", [])
    black_army = army.Army("Black Army", [])

    """create players"""
    harry_nerd = player.Player(100, red_army)
    starwars_nerd = player.Player(100, black_army)

    """create red army soldiers"""
    harry = soldiers.Swordsman("Sword of Gryffindor")
    bellatrix = soldiers.Bowman("Unyielding Wand of Bellatrix LeStrange")
    hermione = soldiers.Swordsman("Chants")
    ron = soldiers.Scouter("Magical Dumbness")

    harry.join(harry_nerd, red_army)
    bellatrix.join(harry_nerd, red_army)
    hermione.join(harry_nerd, red_army)
    ron.join(harry_nerd, red_army)

    """create black army soldiers"""
    vader = soldiers.Swordsman("Red Lightsaber")
    leia = soldiers.Swordsman("Blue Lightsaber")
    r2d2 = soldiers.Scouter("Cuteness")
    luke = soldiers.Bowman("Magical Dumbness")

    vader.join(starwars_nerd, black_army)
    leia.join(starwars_nerd, black_army)
    r2d2.join(starwars_nerd, black_army)
    luke.join(starwars_nerd, black_army)

    """printing the armies"""
    army.print_army(red_army)
    say_hurray(red_army)

    army.print_army(black_army)
    say_hurray(black_army)

    print("\n")
    """scout informs"""
    ron.inform_army()

    """FIGHT!"""
    black_army.fight(red_army)


def say_hurray(team):
    """Prints the hurrays."""

    for fighter in team.fighters:
        fighter.say_hurray()


init()
