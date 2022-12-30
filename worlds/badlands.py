import random
from worlds.world import randomName


def badlands(name):
    sin = None

    def rob():
        print(
            'The problem is worn paths have lots of traffic to get in that state and being alone is asking to be considered vulnerable to anything \n suddenly your hairs stand and a chill goes up your spine \n "kekeke" \n "Look at this boys seems like we have some things for the picking" \n "Finally i was worried we risked staying out here for nothing" \n The three surround you a dagger in each of their hands')
        tempN = None
        th = None
        sub = None  # use this to skip the rest of rob if needed
        input()
        print('"So what is your name man"')
        re = str(input(
            'What do you say? \n Tell your name(TELL), give fake(FAKE), say nothing(press enter), ask why they stopped you(WHY):'))
        print()
        while (re != 'TELL' and re != '' and re != 'FAKE' and re != 'WHY'):
            re = str(input('The options are (TELL),(WHY),(<enter key>),(FAKE):'))
        if (re == 'TELL'):
            print('I am', name)
            th = 1
        elif (re == ''):
            print('......')
            th = 3
        elif (re == 'FAKE'):
            tempN = randomName()
            print('I am', tempN)
            th = 2
        elif (re == 'WHY'):
            print('Why are you stopping me?')
            th = 4

        if (th == 4):  # spent too much time on this part
            print(
                '"Are you a fool you idiot we are going to rob you that\'s what"\n"Calm down he is clearly trying to doop us"\n "Its just vexing we look like robbers we are talking like they would to"\n"when did you learn such smart words"')
            input()
            print('They keep arguing amongst each other and it just keeps going on and on')
            input()
            print(
                'Two of them forgit about the world around them and the third looks like he regrets ever speaking to you or his partners')
            morb = str(input(
                'You grow tiered of this you can clear your throat to get their attention(COUGH), or you can just walk away(WALK) or you can surprise attack one of them(KILL):'))
            print()
            while (morb != 'COUGH' and morb != 'WALK' and morb != 'KILL'):
                morb = str(input('The options are (COUGH),(WALK),(KILL):'))
            if (morb == 'WALK'):
                print('You decide to take the easy way out and just walk away')  # this ends rob and go to next
                sub = False
            elif (morb == 'COUGH'):
                print(
                    'You just want this interaction over with and get their attention "Can we just get this over with cut to the chase and tell me what you want"')
                input()
                print('"we want to rob you give us everything you have"')  # go to the next part
                sub = True
            elif (morb == 'KILL'):
                print(
                    'in a swift movement you stab one of the robbers arguing with the other in the back of the neck taking him out the other two are horrified some nobody just killed their pal')  # the illusion of choice they all end the robbery and go to next AHHAHAHAHAH
                input()
                print('"you killed', randomName(),
                      'we didnt even do anything to you we arnt barbaric we just asked your name we didnt even jump you or surprise attack you')
                input()
                print(
                    'The two leave and you have the feeling they were good people just forced to do some bad things did he deserve to die')
                input()
                input()
                input()
                print('You keep waking')
                sub = False

        elif (th == 2):
            print('"', tempN, 'is it? That\'s a wierd one boys"')
            lug = random.randint(1, 5)
            if (lug == 1):
                input()
                print('"I knew someone named', tempN,
                      ' a few years back looked kinda like you wait a second\n IS THAT YOU', tempN, '"')
                input()
                print(
                    'You laugh and say I couldn\'t tell it was you under that mask you have on. this, of course, is all a lie you dont even know anyone with the name',
                    tempN)
                input()
                print('you and him talk a bit about something that never happened and he seems to respect this',
                      tempN, 'person and he decides to let you go')  # this ends the robbery and goes to next
                sub = False
            else:
                input()
                print('"whatever', tempN, 'give us everything you have or we\'ll kill you')  # go to the next part
                sub = True
        elif (th == 3):
            input()
            print('"Oh so we got a tough guy dont we"')
            input()
            print('"give us all that you have"')
            sub = True
        elif (th == 1):
            print('"alright', name, 'give us every thing you have"')  # go to next part of rob
            sub = True

        if (sub is True):  # this makes you get robbed
            input()
            print('dont fight back you are 1 against 3 you stand no chance')  # ends here kek

        elif (sub is False):  # you ended the encounter
            input()
            print(
                'Sooner or later you stumble to a shack your memories tell you this is your home Lets end this here to save time')

    input()
    # start of normal badlands
    print(
        'in an instant your mind is filled with a life you never lived experiences you never had yet with your eyes open you see the last thing your memories showed you, ',
        name, ', walking a trail in the badlands')
    input()
    print(
        'You start walking along a small path that can only be differentiated by the worn ground if you compare it to the scraped ground near it')
    input()
    # sin=random.randint(1,3)#1 is robbery 2 is sandstorm 3 is monster
    sin = 1
    if (sin == 1):
        rob()

    # if(sin==2):
    # sand()
    # if(sin==3):
    # beast()
