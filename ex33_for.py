# rewriting 33 to use a for loop

def for_to_print(how_many, steps):
    i = 0
    numbers = []

    for x in range(i, how_many):
        if i == how_many:
            break

        #print("At the top i is %d" % i)
        numbers.append(i)

        i = i + steps
        print("Numbers now: ", numbers)
        #print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)

for_to_print(12, 3)
