from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import random


'''Procedures'''
#1-3 N/A

'''Part I: for loops, range(), and help()'''
#4 
def days():
    """ 
    For each letter in the string 'MTWRFSS' it prints the first letter with
    day appended at the end. The 2nd for loop prints 5, 6, and 7 as str(day)
    in the 'It is the ' + str(day) + 'th of September'
    """
    for day in 'MTWRFSS': 
        print(day + 'day')
    for day in range(5,8):
        print('It is the ' + str(day) + 'th of September')

#5
def picks():
    """
    Creates a random list of 1,3, or 10 and stores a chart of the data in 
    1.3.7/picks
    """
    a = [] # make an empty list
    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list]
    #    random.choice(   [brackets here to choose from a list])

    a += [random.choice([1, 3, 10])]
    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.savefig('1.3.7/picks')

#6 
#a)
def roll_hundred_pair():
    """
    Rolls 100 pairs of 1-6 dice and records the results in a chart
    """
    result = []
    for i in range(100):
        total = random.randint(1,6) + random.randint(1,6)
        result.append(total)
        
    plt.hist(result)
    plt.savefig('1.3.7/roll_hundred_pair')
        
#b)
def dice(n):
    total = 0
    for i in range(n):
        roll = random.randint(1,6)
        total += roll
        return total
        
    print("Roll was", total)
        
        
'''Part II: While loops'''
#7
def validate():
    guess = '1' # initialization with a bad guess
    answer = 'hangman word'
    while guess not in answer:
        guess = raw_input('Name a letter in \''+answer+'\': ')
    print('Thank you!')

# Line 2 is nessecary because you have to assign guess a a value before you can
# allow it to be called in a function

#8 
def guess_winner(players=('Amy', 'Bill', 'Cathy', 'Dale')):
    '''
    The 4 arguments in this function contain 4 different names that are called 
    in this function randomly chosen and asks the user for a guess. If the guess
    is correct it prints you guessed in x guesses.
    '''
    winner = random.choice(players) 

    ####
    # Loops through all the players and prints them out
    ####
    print('Guess which of these people won the lottery: ',end='')
    for p in players[:len(players)-1]: # Loops 0-3 (4 times) through the names
        print(p+', ', end='')
    print(players[len(players)-1]) # Prints out the names of the characters

    ####
    # Checks if what the user inputed is = to the random character
    ####
    guesses = 1 
    while raw_input() != winner:
        print('Guess again!')
        guesses += 1
    print('You guessed in', guesses, 'guesses!')
    return guesses    

#9 
def goguess():
    '''Chooses a random number and user inputs a guess and determines
    relationship between guess and random number'''
    attempt = 1
    win = False
    secret = random.randint(1,20)
    print('I have a number between 1 and 20 inclusive.')
    while win == False:
        guess = int(raw_input('Guess: '))
        if guess == secret:
            print('Right! My number is', secret,'. You guessed in', attempt, 'guesses!')
            win = True
        elif guess > secret:
            print(guess, 'is too high')
            attempt += 1
        else:
            print(guess, 'is too low')
            attempt += 1
            
#10 You will need 6000/(2^x) until its < 1 guesses because for every guess you 
#   are able to cut the number of possible answer in half, so therefore the number
#   of guesses would have to be 2^x number of times.


'''Part III: Practice'''
#11 
def matches(ticket, winners):
    '''
    Takes 2 lists and returns how many common values they share
    '''
    common = 0
    for value in ticket:
        for win in winners:
            if value == win:
                common += 1
    
    return common

# b)
def report(guess, secret):
    '''
    Reports how many colors in the guess are in the secret and also reports 
    whether the correct colors are in the correct place.
    '''
    number_right_place = 0
    number_wrong_place = 0
    
    unFoundSecret = []
    unFoundGuess = []
    
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            number_right_place += 1
        else:
            unFoundSecret.append(secret[i])
            unFoundGuess.append(guess[i])
            
    for found in unFoundGuess:
        for secret in unFoundSecret:
            if found == secret:
                number_wrong_place += 1
                break
    
    return [number_right_place, number_wrong_place]
    
    
'''Conclusion'''
#1 Doing so would make the code a lot less elagant and a lot harder to 
#  troubleshoot. Using unrolled loops during development is tedious, boring and 
#  just plain inefficient to change anything inside of it, such as if it was 
#  for i in range(1000)

#2 Both iteration and data analysis deals with large amounts of data. Iteration 
#  reads information about each item, where data analysis on the other hand
#  only reads information to get statistics.

#3 A while loop keeps running until the condition is true and stops running when
#  it is no longer true. A for loop runs through the code for all the values in
#  the second list and only stops when all values or range(x) is completed.

#4 My partner and I worked well together by brainstorming ideas together when we
#  were stuck and building off of one another's ideas in order to finally solve
#  the question. Some things that could be improved are perhaps staying more 
#  focused when we work instead of going on side tangents in order to become
#  more efficient.


'''Assignment Check'''
#1.3.7 Function Test
days()
dice(5)
roll_hundred_pair()
validate()
goguess()
guess_winner()

print(matches([11, 12, 13, 14, 15], [3, 8, 12, 13, 17]))

guess = ['red','red','red','green','yellow']
secret = ['red','red','yellow','yellow','black']
print(report(guess, secret))

# Yes.