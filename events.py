# Dice d20 mechanic
import random


def rollD20():
    return random.randint(1, 20)

# Branching Paths


def swampBattle():
    print('After a short ride out with your horse, you finally reach the outskirts of town, in view of the swamp\n',
          'Something definitely feels amiss though. You feel like you\'re being watched.')

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
