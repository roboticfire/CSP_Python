from __future__ import print_function
import random
import os
import sys
import time

class GameStatus:
    """
    Determines initial stats for your character
    """
    def __init__(self):
        self.health = 100
        self.money = 600
        
    def reduce_health(self, healthlost):
        """Function for reducing health"""
        x = int(healthlost)
        self.health = self.health - x
        if self.health <= 0:
            self.health = 0
            print("Now, you have %s health left." % game_status.health)
            print("Game Over")
            sys.exit()
        else:
            print("You have lost %s health and now have %s health left. \n" 
            % (str(x), str(game_status.health)))
            
    def reduce_money(self, moneyspent):
        """Function for reducing the amount of money"""
        # import pdb;pdb.set_trace()
        x = int(moneyspent)
        if moneyspent < 0:
            print("Negative money ... you get beaten up")
            print("Game Over")
            sys.exit()
        else:
            self.money -= x
            if self.money == 0:
                self.money = 0
                print("""You are now out of money and are no longer able to 
                continue.""")
                print("Game Over")
                sys.exit()
            else:
                print("You now have %s dollars left." % game_status.money)
        
game_status = GameStatus()

print("-----Hiest----- \n")
time.sleep(1.5)
print("---User Stats---")
print("Health: %s" % game_status.health)
print("Money: %s \n" % game_status.money)
time.sleep(2)
print("Welcome To Flatiron Museum! Sorry but we are currently closed.")
print("You are desperate, as you are in desperate need of money")
print("Cautiously, you look around for a way of entering. \n")
time.sleep(2)
        
def choice1():
    """
    Packaged first choice
    First main choice you make, 2 options, either a or b, reruns function if
    answer is not a or b
    Uses raw_input for user interaction
    """
    print("Do you:")
    print("A) Break the window.")
    print("B) Look around the back.")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        """Determines which path you take based on your answer"""
        print("You sucessfully broke the window! \n")
        time.sleep(0.5)
        if random.randint(0,3) == 1:
            print("Unfortunately, you scratched your leg and started bleeding\n")
            time.sleep(1)
            game_status.reduce_health(20)
        choice2a()
    elif answer == "B" or answer == "b":
        print("You found a hidden key! You sneak in. \n")
        time.sleep(1)
        choice2b()
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice1()
        
def choice2a():
    """
    Packaged second(a) choice
    Second choice if answer to choice 1 was A, 3 options, either a, b, or c, 
    if not prints Invalid and reruns function until answer is a, b, or c
    Uses raw_input for user interaction
    """
    print("After breaking the window, you see a guard walking around")
    print("Do you:")
    print("A) Attack the guard.")
    print("B) Hide in a bush.")
    print("C) Try to bribe him.")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("The guard turned out to be John Cena and you get beaten up.")
        print("You barely escape out of his grasp.")
        game_status.reduce_health(30)
        time.sleep(1)
        choice2b()
    elif answer == "B" or answer == "b":
        print("You tripped a hidden laser and your foot gets burned off.")
        print("You lie on the floor in pain as you get rushed to the hospital.")
        time.sleep(1)
        game_status.reduce_health(100)
    elif answer == "C" or answer == "c":
        print("How much money do you give?")
        try:
            moneyspent = int(raw_input(">> "))
        except ValueError:
            print("You did not give him any money.")
            time.sleep(1)
            print("John Cena gets mad and attacks you for wasting his time")
            game_status.reduce_health(100)
        game_status.reduce_money(moneyspent)
        if moneyspent >= 200:
            print("""Since John Cena is poor after getting scammed on Roblox""", 
            """he decides to accepts your donation.""")
            time.sleep(1)
            choice3()
        else: 
            print("You did not provide enough money, John Cena beats you up.")
            time.sleep(1)
            game_status.reduce_health(100)
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice2a()
        
def choice2b():
    """
    Packaged second(b) choice
    Second choice if answer to choice 1 was B, 3 options, either a, b, or c, 
    if not prints Invalid and reruns function until answer is a, b, or c
    Uses raw_input for user interaction
    """
    
    print("After sneaking in, you spot security cameras peering around.")
    print("Do you:")
    print("A) Pose in front of it.")
    print("B) Wear a mask")
    print("C) Disgiuse yourself as a dinosaur.")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("Choose a pose from 1-3")
        pose = raw_input(">> ")
        if pose == "1" or pose == "2" or pose == "3":
            if pose == "1":
                print("You stand still and dab as the cameras pass over you.")
                print("You get detected and run, only to trip over some bones.")
                print("You barely escape.")
                game_status.reduce_health(30)
                time.sleep(1)
                choice3()
            elif pose == "2":
                print("The operator had a bad day and fights you.")
                print("You manage to knock him unconscious, but you got hurt.")
                game_status.reduce_health(40)
                time.sleep(1)
                choice3()
            elif pose == "3":
                print("The operator loves your pose and lets you pass. \n")
                time.sleep(1)
                choice3()
        else:
            print("Invalid, try again")
            choice2b()
    elif answer == "B" or answer == "b":
        print("You accidently grab the mask of a dead pharaoh and get cursed.")
        print("You die a painful death. \n")
        time.sleep(0.5)
        game_status.reduce_health(100)
    elif answer == "C" or answer == "c":
        print("You rush to a T-rex and grab its skull.")
        print("Being nervous, unfortunately you")
        print("cut yourself on a tooth and get injured.")
        time.sleep(3)
        game_status.reduce_health(20)
        if random.randint(1,2) == 1:
            print("""Luckily, you aren\'t detected and managed get pass the""", 
            """cameras. \n""")
            time.sleep(1)
            choice3()
        else:
            print("You return to your original hiding spot. \n")
            time.sleep(1)
            choice2b()
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice2b()
        
def choice3():
    """
    Packaged third choice
    Third function from both 2a and 2b, 3 options, a, b, or c, 
    reruns function if answer is not a, b, or c
    Uses raw_input for user interaction
    """
    
    print("The final guard, armed with a pistol, confronts you.")
    print("Do you:")
    print("A) Try to bribe him")
    print("B) Run away")
    print("C) Attack him")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("He asks for a donation of 300.")
        print("You are forced to hand over the money.")
        game_status.reduce_money(300)
        time.sleep(2)
        print("The guard backstabs you and chases after you.")
        print("However, you grab the gem and escape. \n")
        choice4()
    elif answer == "B" or answer == "b":
        print("You run away.")
        print("The guard finds you again and chases after you.")
        time.sleep(2)
        if random.randint(1,2) == 1:
            print("However, the guard slips on a banana peel and breaks his back")
            print("You grab the gem and run. \n")
            choice4()
        else:
            print("The guard attacks you.")
            print("You deperatly fight back with the nearest object,",
            "a mummy's arm, and repeatly bash his head until he falls onto the",
            "floor, unconscious. \n"
            )
            game_status.reduce_health(20)
            choice3()
    elif answer == "C" or answer == "c":
        print("You get shot, and get rushed to the hospital.")
        print("Unfortunately, you failed your mission. \n")
        time.sleep(2)
        game_status.reduce_health(100)
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice3()

def choice4():
    """
    Packaged fourth choice
    Fourth function from choice 3, 2 options (a or b) and 
    reruns function if answer is not a or b
    Uses raw_input for user interaction
    """
    print("The guard recovers and alerts the others about what happened")
    time.sleep(3)
    print("The alarm rings.")
    time.sleep(1)
    print("BEEEDOOOBEEEDOOOOBEEDOO")
    time.sleep(2)
    print("BEEEEDOOOBEEEDOOOOBEEDOOO")
    time.sleep(2)
    print("BEEEEDOOOBEEEDOOOOBEEDOOOBEEEEDOOOOB")
    time.sleep(2)
    print("Now on the run, hordes of cops chase after you. \n",
    "Slowly, but surely, your options are slowly shrinking \n",
    "Do you: \n",
    "A) Make a mad dash for the window \n",
    "B) Attack the horde")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("Dragged down by the weight of the gem, the guards quickly \n",
        "move in and close you off")
        choice5a()
    elif answer == "B" or answer == "b":
        print("You turn around, drop into a fighting stance, \n",
        "and stare at the approaching guards.")
        choice5b()
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice4()
        
def choice5a():
    """
    Packaged fifth(a) choice
    Fifth function from choice 4, 2 options (a or b) and 
    reruns function if answer is not a or b
    Uses raw_input for user interaction
    """
    print("Do you: \n",
    "A) Go right \n",
    "B) Go left")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("You juked the guards.")
        print("You charge for the exit.\n")
        time.sleep(1)
        victory()
    elif answer == "B" or answer == "b":
        print("The guards anticipate your move and you get trapped.")
        print("Although you put up a valiant fight, you get arrested.\n")
        time.sleep(1)
        print("Game Over")
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice5a()
    
        
def choice5b():
    """
    Packaged fifth(b) choice
    Fifth function from choice 4, 2 options (a or b) and 
    reruns function if answer is not a or b
    Uses raw_input for user interaction
    """
    print("The guards, unsure of what to do, approach you slowly.\n",
    "You look around for a weapon.\n"
    "Do you: \n",
    "A) Grab a antique knife \n",
    "B) Grab a painting")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("Bring a knife to a gun fight doesn\'t work out so well for you")
        time.sleep(2)
        print("You charge at them, but they gun you down at a distance.\n")
        game_status.reduce_health(100)
    elif answer == "B" or answer == "b":
        print("The guards cringe as you grab the mult-million dollar \n",
        "painting and charge at them. \n",
        "They offered a deal, give them the painting and they claim that they \n",
        "will not hurt you. \n",)
        choice6
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice5b()
        
def choice6():
    """
    Packaged sixth choice
    sixth function from choice 4, 2 options (a or b) and 
    reruns function if answer is not a or b
    Uses raw_input for user interaction
    """
    print("Do you:")
    print("A) Give them the painting")
    print("B) Run for the exit")
    answer = raw_input(">> ")
    if answer == "A" or answer == "a":
        print("The guards betray you and charge at you")
        print("Although you fought hard, you get overwhelmed.")
        time.sleep(1)
        print("Game Over")
    elif answer == "B" or answer == "b":
        print("The guards, caught by surprise, chase after you.")
        print("However, fueled by adrenaline, you manage to escape")
        print("their prying hands and as the door got closer and closer")
        victory()
    else:
        print("Invalid, try again \n")
        time.sleep(0.5)
        choice6()
        
def victory():
    """
    Packaged function for printings
    words when victory is achieved
    """
    print("Panting with the effort, you burst charge out of the museum \n and",
    "into the bright sunlight with the gem held proudly at your side.\n")
    print("Congratulations - You Win!")
    
choice1()