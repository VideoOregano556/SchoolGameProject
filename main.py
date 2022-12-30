import random
from worlds.grasslands import grasslands
from worlds.badlands import badlands
from worlds.swamps import swamps


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
        'Hint: if a statement ends in ":" that means you need to input a value it will usually say what the options are\nEnter the name you want:\n'))

    print("\nHello", name, "it is nice to meet you.")
    input(
        "Hint: If you are ever hovering in a spot and no text has spawned hit enter to continue to next text. This is to not bombard you with walls of text in one go for example\n")

    print(
        "You have the option of 3 starts: the badlands, grasslands, and swamps. Depending on where you start you'll have a different experience. You can make the decision yourself or let luck do it for you.")
    input()
    print(
        "Three doors drop in front of you the first a sand-colored door the second a pleasant green and the last a smudgy blue with splotches of green\n")

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

    input()
    print('It was nice talking to you', name, 'I pray thee be careful on your journey')

    world(start, name)


if __name__ == "__main__":
    main()
