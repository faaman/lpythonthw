def while_to_print(how_many, steps):
    i = 0
    numbers = []

    while i < how_many:
        print("At the top i is %d" % i)
        numbers.append(i)

        i = i + steps
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)


while_to_print(8, 2)
