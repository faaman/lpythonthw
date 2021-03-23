from sys import exit
from random import randint


class Scene(object):

    def enter(self):
        print("This scene is not yet configured. Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n- - - - - - - - ")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Adventure(Scene):
    quips = [
        "Sound the Octo-Alert!",
        "Octonauts, let's do this!",
        "Octonauts, we've got an emergency rescue, first aid, lost sardine situation.",
        "Go ahead, Shellyfish... I mean Jellington... I mean Shellington!"
    ]

    def enter(self):
        print(Adventure.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class HQ(Scene):

    def enter(self):
        print("Barnacles is the brave polar bear captain of the Octonauts.")
        print("He knows how to drive any vehicle and is strong enough to lift a giant clam.")
        print("Kwazii is a daredevil cat with a mysterious pirate past.")
        print("He believes in many sea monsters ")
        print(" and likes to drive fast in the Gup-B. ")
        print("\n")
        print("Peso is a penguin and the medic of the Octonauts")
        print("He is not fond of scary situations, ")
        print("but if someone is hurt or .")
        print("in trouble he can be the bravest Octonaut of all")
        print("\n")
        print("Now choose an episode: shark, storm, urchin")

        action = input("> ")

        if action == "shark":
            print("When Dashi is swallowed by a whale shark ")
            print("she thought was a cave, ")
            print("the Octonauts venture inside it to rescue her.")
            return 'adventure'

        elif action == "storm":
            print("An undersea storm is approaching ")
            print("so Kwazii helps some creatures on a coral reef reach safety, ")
            print("but then he crashes the Gup-B while trying to race back to the Octopod. ")
            print("When the GUP-C's tow-rope snaps while rescuing him, ")
            print("some reef lobsters Kwazii helped earlier lend a hand ")
            print("by holding the broken rope ends together with their strong claws.")
            return 'adventure'

        elif action == "urchin":
            print("Barnacles and Kwazii investigate ")
            print("a disruption on a nearby reef; ")
            print("A carrier crab, and the urchin it keeps on top of its shell as a defence against predators ")
            print("have a falling out and just can't seem to get along.")
            return 'library'

        else:
            print("DOES NOT COMPUTE!")
            return 'head_quarters'


class Library(Scene):

    def enter(self):
        print("A school of flying fish accidentally ")
        print("make off with Professor Inkling's rare book ")
        print("and the Octonauts rig up the GUP-B to get it back. ")
        print("You find the school and need to say a code ")
        print("for the flying fish to return the rare book. ")
        print("If you get the code wrong 10 times then the ")
        print("fish fly away and you can't get the book. The code is 3 digits.")
        code = "%d%d%d" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 9:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print("The flying fish give you the book. ")
            print("You grab the rare book and run as fast as you can to the ")
            print("chute where you must drop it to slide down.")
            return 'the_chute'

        else:
            print("The flying fish fly away ")
            print("with the rare book.")
            return 'adventure'


class TheChute(Scene):

    def enter(self):
        print("You burst onto the Bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 Gothons who are trying to")
        print("take control of the ship. Each of them has an even uglier")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of Gothons")
            print("and make a leap for the door. Right as you drop it a")
            print("Gothon shoots you right in the back killing you.")
            return 'adventure'

        elif action == "slowly place the bomb":
            print("You point your blaster at the bomb under your arm")
            print("and the Gothons put their hands up and start to sweat.")
            return 'launch_bay'

        else:
            print("DOES NOT COMPUTE!")
            return "the_chute"


class LaunchBay(Scene):

    def enter(self):
        print("You rush through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes. It seems like")
        print("but you don't have time to look. There's 5 pods, which one")
        print("do you take?")

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of spac")
            return 'adventure'
        else:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod easily slides out into space heading to")
            print("time. You won!")
            return 'finished'


class Map(object):
    scenes = {
        'head_quarters': HQ(),
        'library': Library(),
        'the_chute': TheChute(),
        'launch_bay': LaunchBay(),
        'adventure': Adventure()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('head_quarters')
a_game = Engine(a_map)
a_game.play()
"""
b_map = Map('library')
b_game = Engine(a_map)
b_game.play()
"""
c_map = Map('the_chute')
c_game = Engine(a_map)
c_game.play()
"""
d_map = Map('launch_bay')
d_game = Engine(a_map)
d_game.play()
"""
