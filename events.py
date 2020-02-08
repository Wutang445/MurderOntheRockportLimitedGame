def introFunction(arg):
    while(arg != 'yes'):
        if arg == 'stop':
            print('No, you stop. Party pooper.')
        elif arg == 'dab':
            print('*dabs back*')
        else:
            print('Are you sure? It\'ll be a good one!')
            
        arg = input()
    print('\nGood! Let us begin then..... \n');

def wagonInteraction(arg):
    if arg == 'observe':
        print('\nYou look over each individual carefully, noting any specific details\n')
        print('The first person looks like a short, stout dwarven man who is heavily armored and sleeping soundly.\n')
        print('The second is a hooded figure who is completely covered by a long cloak. All you can tell is that they must have a thin build, and at least 7 feet tall.\n')
        print('The third figure is a bit of a mystery. She\'s dressed in long robes with strange markings all over them. Based on her features, she doesn\'t look human.\n')

    elif arg == 'speak':
        print('You attempt to speak to all of them with a hearty, friendly hello!')
        print('The dwarven man remains asleep. The hooded figure slowly turns to look at you, and seems to snarl')
        print('The witch looks at you almost sternly, but softens to a smile\n')
        print('Seems like they aren\'t the talking type...\n')
    
    print('\nAfter some time, you start to see the beginning gate for the town of Rockport')

def townPath(arg):
    if arg == 'head to bar':
        print('\nYou decide to visit the local watering hole, weirdly named Bodett\'s Bar')
        print('Now that you look around, all the townspeople seem to look like beloved radio personality Tom Bodett')
        print('That\'s weird')
        print('Anyway, after grabbing a few drinks, you overhear of a bounty for the creatures that reside in the swamp outside of Rockport')
