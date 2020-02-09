import random


# Dice d20 mechanic


def rollD20():
    return random.randint(1, 20)

# Branching Paths


def swampBattle():
    print('After a short ride out with your horse, you finally reach the outskirts of town, in view of the swamp',
          '\nSomething definitely feels amiss though. You feel like you\'re being watched. Do you want to make a perception check? (yes/no)')
    answer = input()

    if(answer == 'yes'):
        check = rollD20()
        print('You rolled a ' + str(check) + ' for perception')
        if(check > 8):
            print('Congrats, you passed the check!\n'
                  'You see a mass of twisted trees around without leaves, but also notice in the distance what looks to be',
                  'to be crashed pod. As you get closer\nto the site, you see a fallen branch atop a crushed, giant leech, along',
                  'with other, clearly dead giant leeches. Footprints seem to be scattered\nall around, but they head in the direction of the town.')

            print(
                '\nYou also hear what seems like the snap of small twigs, and the sound of a faint, low hum.\n'
                'As you creep up to the source of the sounds, you see 2 figures in the distance.\n'
                'The first figure is a human male wearing plated armor, strapped high to one of the trees in a crucifixion pose. His mouth is gagged with a black cloth\n'
                'The second figure you recognize. It\'s the 7 ft tall hooded occupant of the wagon you rode into town. His hand is raised and colored red,\nthe low hum is emanating from',
                'the spell he seems to be casting.')

        else:
            print('You didn\'t pass the check, better luck next time...\n'
                  'You shudder as the landscape around you gives off the worst vibes')


# Storyline functions


def introFunction(arg):
    while arg != 'yes':
        if arg == 'stop':
            print('No, you stop. Party pooper.')
        elif arg == 'dab':
            print('*dabs back*')
        else:
            print('Are you sure? It\'ll be a good one!')

        arg = input()
    print('\nGood! Let us begin then..... \n')


def wagonInteraction(arg):

    while arg != 'observe' or arg != 'speak' or arg != 'stay silent':

        if arg == 'observe' or 'speak' or 'stay silent':
            break
        arg = input()

    if arg == 'observe':

        print('\nYou look over each individual carefully, noting any specific details.\n'
              'The first person looks like a short, stout dwarven man who is heavily armored and sleeping soundly.\n'
              'The second is a hooded figure who is completely covered by a long cloak.',
              'All you can tell is that they must have a thin build, and at least 7 feet tall.\n'
              'The third figure is a bit of a mystery. She\'s dressed in long robes with strange markings all over them.',
              'Based on her features, she doesn\'t look human.\n')

    elif arg == 'speak':

        print('\nYou attempt to speak to all of them with a hearty, friendly hello!\n'
              'The dwarven man remains asleep. The hooded figure slowly turns to look at you, and seems to snarl\n'
              'The witch looks at you almost sternly, but softens to a smile\n'
              'Seems like they aren\'t the talking type...\n')

    print('After some time, you start to see the beginning gate for the town of Rockport')


def townPath(arg):

    while arg != 'head to bar' or arg != 'look for work' or arg != 'visit hotel':

        if arg == 'head to bar' or 'look for work' or 'visit hotel':
            break
        arg = input()

    if arg == 'head to bar':

        print('\nYou decide to visit the local watering hole, weirdly named Bodett\'s Bar\n'
              'Now that you look around, all the townspeople seem to look like beloved radio personality Tom Bodett\n'
              'That\'s weird\n'
              'Anyway, after grabbing a few drinks, you overhear of a bounty for the creatures that reside in the swamp outside of Rockport...\n')

        swampBattle()

    elif arg == 'look for work':

        print('\nAfter spending a couple hours asking every Tom Bodett about work, you find a job\n'
              'One of them tasks you with checking out his house, making sure his cousin, Ron Bodett, isn\'t stealing from him\n'
              'He tells you that his address is at 420 Daverly Place')

    elif arg == 'visit hotel':

        print('\nYou trudge to the Rockport hotel, exhausted from the long journey to town\n'
              'The lobby of the hotel is a luxurious, sprawling floor filled with velvet furniture and golden decorations\n'
              'You speak to the hotel staff and acquire a room on the 7th floor of the hotel')
