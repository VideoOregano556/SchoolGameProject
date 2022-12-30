from worlds.grasslands import grasslands
from worlds.badlands import badlands
from worlds.swamps import swamps

import random
from os import system, name
from time import sleep


def clear_text():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def world(start, name):
    if (start == 1):
        badlands(name)

    if (start == 2):
        grasslands()

    if (start == 3):
        swamps()


def main():
    print("What is your name?\n")
    name = str(input(
        'Hint: if a statement ends in ":" that means you need to input a value. It will usually say what the options are.\nEnter the name you want:\n'))
    clear_text()
    print("\nHello", name, "it is nice to meet you.")
    input("Press Enter to continue")
    clear_text()

    print(
        "You have the option of 3 starts: the badlands, grasslands, and swamps. Depending on where you start you'll have a different experience. You can make the decision yourself or let luck do it for you.")
    input("Press Enter to continue")
    print("Three doors drop in front of you the first a sand-colored door the second a pleasant green and the last a smudgy blue with splotches of green\n")

    print('well', name, 'what is your choice? (1, 2, 3 or RNG)')
    start = str(input('Let\'s go with:\n'))

    while (start.lower() != 'rng' and start != '1' and start != '2' and start != '3'):
        start = str(input('pleas enter a correct value, 1,2,3 or RNG:'))

    if (start.lower() == 'rng'):
        start = random.randint(1, 3)
    else:
        start = int(start)

    if (start == 1):
        print(
            '\nAh the badlands a place that is both empty and full at the same time isn\'t it strange how things like that can exist.')
    elif (start == 2):
        print('\nthe good old grass lands a beautiful place, but not without its flaws')
    else:
        print('\nSwamps is a hidden gem if you ask me there is nothing quite like it in terms of looks')

    input("Press Enter to continue")
    print('It was nice talking to you', name, 'I pray thee be careful on your journey')
    sleep(3)
    world(start, name)


if __name__ == "__main__":
    main()
