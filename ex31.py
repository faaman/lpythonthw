print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear says hi. Good job!")
    elif bear == "2":
        print("The bear says hola. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away." % bear)

elif door == "2":
    print("You stare into the endless abyss on the mesa.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Ye jo desh hai tera.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Swadesh hai tera. Good job!")
    else:
        print("Ye jo bandhan hai. Good job!")

else:
    print("Woh toot nahi sakta. Good job!")