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