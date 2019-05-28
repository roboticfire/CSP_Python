from __future__ import print_function
import random
import sys
import os

diamond = False

class GameStatus:
    def __init__(self):
        self.health = 100
        
    def reduce_health(self, healthlost):
        x = healthlost
        self.health = self.health - x
        if self.health <= 0:
            self.health = 0
            print("Game Over")
            sys.exit()
        
print("Hello, %s." % name)
print("What is your name?")
name = raw_input(">> ")
print("Hello, %s." % name)
print("Currently, you have %s health." % game_status.health)
print(".")
print('Welcome To Flatiron Museum! Sorry but we are currently closed.')
        
def choice1():
    print("Do you:")
    print("A) Break the window.")
    print("B) Look around the back.")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("You sucessfully broke the window!")
        if random.randint(1,3) == 1:
            print("Unfortunately, you scratched your leg and started bleeding")
            game_status.reduce_health(40)
            print("Currently, you have %s health left." % game_status.health)
        choice3()
    elif answer == "B" or answer == "b":
        print("You found a hidden key! You sneak in.")
        choice2()
    else:
        print("Invalid, try again")
        choice1()
        
def choice2():
    print(".")
    print("After sneaking in, you see a guard walking around")
    print("Do you:")
    print("A) Attack the guard.")
    print("B) Hide in a bush.")
    print("C) Try to bribe him.")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("The guard turned out to be John Cena and you get beaten up")
        print("You barely escape out of his grasp.")
        game_status.reduce_health(50)
        choice3()
    elif answer == "B" or answer == "b":
        print("You tripped a hidden laser and your foot gets burned off")
        print("You lie on the floor in pain")
    elif answer == "C" or answer == "c":
        print("")
    else:
        print("Invalid, try again")
        print(".")
        choice2()
        
def choice3():
    print(".")
    print("After sneaking in, you spot security cameras peering around.")
    print("Do you:")
    print("A) Attack the guard.")
    print("B) Hide in a bush.")
    print("C) Try to bribe him.")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        if random.randint(1,3):
            print()
    elif answer == "B" or answer == "b":
        print("")
    elif answer == "C" or answer == "c":
        print("")
    else:
        print("Invalid, try again")
        print(".")
        choice2()
        
choice1()
        
