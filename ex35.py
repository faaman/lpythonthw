# I replaced sentences with PnP, but now the questions don't make much sense

from sys import exit


def gold_room():
    print("It is a truth universally acknowledged, ")

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Lady, learn to type a number.")

    if how_much < 50:
        print("that a single man in possession of a good fortune, ")
        exit(0)
    else:
        dead("must be in want of a wife. ")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take honey":
            dead("What is his name?")
        elif next == "taunt bear" and not bear_moved:
            print("Is he married or single?")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("How so? How can it affect them?")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print("I see no occasion for that.")


def cthulhu_room():
    print("They have none of them much to recommend them, ")
    print("they are all silly and ignorant like other girls; ")
    print("but Lizzy has something more of quickness than her sisters. ")

    next = input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Ah, you do not know what I suffer.")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Depend upon it, my dear, that when there are twenty, I will visit them all.")
    exit(0)


def start():
    print("If I were as rich as Mr. Darcy ")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You make me laugh, Charlotte; but it is not sound.")


start()
