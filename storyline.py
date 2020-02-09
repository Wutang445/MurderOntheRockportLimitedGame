from events import *

# Game Text

print('*' * 44)
print('*' * 13 + 'Murder at Rockport' + '*' * 13)
print("***Are you ready to begin your adventure?***")
print('*' * 44)
print('*' * 13 + 'yes' + '*' * 13 + 'no' + '*' * 13)

introFunction(input())

print("Our story begins as you ride into town, on a wagon with several other rough-looking individuals...")
print("You don't know any of their names, backgrounds, or where they came from. What do you do? \n")
print("observe || speak || stay silent\n")
response = input()

wagonInteraction(response)

print("All the occupants of the wagon stumble out through back, you follow")
print("You've made it into the town, what do you choose to do next?\n")
print("head to bar || look for work || visit hotel")
decision = input()

townPath(decision)