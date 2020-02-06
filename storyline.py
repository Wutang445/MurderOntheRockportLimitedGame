from introduction import introFunction
from wagon import *

# Game Text

print("********************************************");
print("***** Welcome to the Rockport Limited! *****");
print("***Are you ready to begin your adventure?***")
print("********************************************");

introFunction(input())

print("Our story begins as you ride into town, on a wagon with several other rough-looking individuals...")
print("You don't know any of their names, backgrounds, or where they came from. What do you do? \n")
print("observe || speak || stay silent\n")
response = input()

wagonInteraction(response)