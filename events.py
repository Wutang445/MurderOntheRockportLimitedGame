import random


# Dice d20 mechanic


def rollD20():
    return random.randint(1, 20)

# Battle Mechanics


def battle(enemyList):
    print('Roll for initiative!')
    battleOrder = {}
    order = []
    userRoll = rollD20()

    for enemies in enemyList:
        battleOrder[f'{enemies}'] = rollD20()
    battleOrder['user'] = userRoll
    battleOrder = sorted(
        battleOrder, key=battleOrder.__getitem__, reverse=True)

    print('The battle order is:\n')
    for i in range(len(battleOrder)):
        print(battleOrder[i])
        order.append(battleOrder[i])
        battleOrder[i] = {battleOrder[i]: 20}
    for j in range(len(order)):
        print(order[j] + ' gets to attack first!')
        if(order[j] == 'user'):
            print('Roll for attack!')


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
                'The second figure you recognize. It\'s the 7 ft tall hooded occupant of the wagon you rode into town. His hand is raised and colored red,\n',
                'the low hum is emanating from the spell he seems to be casting. Suddenly the human looks up, awake, with glowing, red eyes, and is enveloped by\n'
                'what seems to be his own blood, flooding out from him and consuming his entire body. You hear a loud shriek from him, and the hooded figure clutches\n'
                'his main hand and a loud *SPLORTCH* as the human is reduced to a small crimson ball, which then explodes outwards as it knocks the hooded figure back.\n'
                'You hide quickly behind a tree to avoid the effects of what you witnessed, but peer out afterwards to see the remains of the human\'s armor scattered all around\n'
                'along with the hooded figure laying on the swamp floor, unconscious.')

        else:
            print('Didn\'t pass the check, better luck next time...\n')

    else:
        print('You shudder as the landscape around you gives off the worst vibes. After walking for a few minutes, you hear a *SPLORTCH*, and then a shriek\n'
              'Quickly, you dart behind a larger tree and hunker down, petrified with fear. You wait for about 15-20 minutes before you determine the coast\n'
              'is clear. You carefully walk out from your hiding place and head in the direction of where the sounds came from, and find a tall figure\n'
              'slumped over on the swamp floor, along with scattered pieces of what looks like bloodstained armor plating laying everywhere.')

    print('As you recover from the incident, a cluster of long, wiry eye stalks seems to dart out of the tree where the armor pieces lay scattered. You warily walk closer to the tree, only to find that two gigantic leeches\n'
          'rear their heads out, and suddenly you\'re surrounded on two sides by these horrendous, slithering creatures. Get ready for battle!\n')

    battle(['leech1', 'leech2'])


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
