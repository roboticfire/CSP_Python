from __future__ import print_function
import random

'''Procedures'''
#1-4 N/A

'''Part 1: Nested if structures and testing'''

#1
def food_id(food):
    ''' Returns categorization of food

    food is a string
    returns a string of categories
    '''
    # The data
    fruits = ['apple', 'banana', 'orange']
    citrus = ['orange']
    starchy = ['banana', 'potato']

    # Check the category and report
    if food in fruits:
        if food in citrus:
            return 'Citrus, Fruit'
        else:
            return 'NOT Citrus, Fruit'
    else:
        if food in starchy:
            return 'Starchy, NOT Fruit'
        else:
            return 'NOT Starchy, NOT Fruit'
            
#1a The return value resulted from line 17

#1b i.   'orange'
#   ii.  'apple'
#   iii. 'potato'
#   iv.  'broccoli'

#1c It will never occur because banana is counted as a fruit, so thus it will 
# never enter the else statement for starchy.

#2 Test Suite
def food_id_test():
    ''' Unit test for food_id
    returns True if good, returns False and prints error if not 
    good
    '''
    works = True
    if food_id('orange') != 'Citrus, Fruit':
        works = 'orange bug in food id()'
    if food_id('banana') != 'NOT Citrus, Fruit':
        works = 'banana bug in food_id()' 
    if food_id('apple') != 'NOT Citrus, Fruit':
        works = 'apple bug in food id()'
    if food_id('potato') != 'Starchy, NOT Fruit':
        works = 'potato bug in food id()'

    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
#3
def f(n):
    '''Returns if the number is even, odd, an integer, or a muliple of 6'''
    if int(n)==n:
        if n % 2 == 0:
            if n % 3 == 0:
                print('The number' ,str(n), 'is a multiple of 6.')
                return 'The number ' +str(n)+ ' is a multiple of 6.'
            else:
                print('The number' ,str(n), 'is an even number')
                return 'The number ' +str(n)+ ' is an even number.'
        else:
            print('The number' ,str(n), 'is an odd number.')
            return 'The number ' +str(n)+ ' is an odd number.'
    else:
        print(str(n), 'is not an integer.')
        return 'Is not an integer.'

#4 One possible test set is 0, 2, 3, 2.5, and 12.

#5 Test Suite
def f_test():
    '''Unit test for f(n)
    returns True if good, returns False and prints error if not 
    good'''
    works = True
    if f(1.5) != 'Is not an integer.':
        works = 'Integer bug in f()'
    if f(1) != 'The number 1 is an odd number.':
        works = 'Odd number bug in f()'
    if f(2) != 'The number 2 is an even number.':
        works = 'Even Number bug in f()'
    if f(6) != 'The number 6 is a multiple of 6.':
        works = 'Factor of 6 bug in f()'
        
    if works == True:
        print("All good!")
        return True
    else:
        print(works)
        return False
        
'''Part II: The raw_input() function, type casting, and print() from Python 3'''

#7 Concentrating using + just adds the second value as the least significant
# digits on the first variable. Using + as numeric addition means that you add
# the values of the 2 numbers together and it returns the value.

#8 
def guess_once():
    '''Chooses a random number and user inputs a guess and determines
    relationship between guess and random number'''
    secret = random.randint(1, 4)
    print('I have a number between 1 and 4 inclusive.')
    guess = int(raw_input('Guess: '))
    if guess == secret:
        print('Right on! I was number', secret, end='!\n')
    elif guess > secret:
        print('Too high, my number was', secret, end='!\n')
    else:
        print('Too low - my number was', secret, end='!\n')
        
#a Line 11 works by using 1 string, your variable, a keyword=value. The argument 
# end='!/n' adds a new string to the output of the function with an !.

#9
def quiz_decimal(low, high):
    '''Determines if a number is between or above/below the 2 given numbers'''
    print('Type a number between',low,'and',high)
    number = float(raw_input(''))
    if number > high:
        print('No',number,'is greater than',high)
    elif number < low:
        print('No',number,'is less than',low)
    else:
        print('Good!' ,low, '<' ,number, '<' ,high)
    
'''Conclusion'''
#1 The relationship between glass test structures and if statements are that 
# when you run a glass test, it uses if statements and checks all the results,
# and if any of the if statements were true, it would change the result and 
# return an error.

#2 Any number of code, from one to a million, could be ran depending on what 
# arugment the user entered into the function.

#3 Programmers may write test suites before acutally writing the code in case 
# they may want to check their code's flowchart while they are working to make 
# sure the the correct outputs are reached before expanding the code.

#4 Yes.
    
'''Challenge'''
def f_challenge(n):
    '''Returns if the number is even, odd, an integer, or a muliple of 6'''
    if int(n)!=n:
        print(str(n), 'is not an integer.')
    elif n % 6 == 0:
        print('The number' ,str(n), 'is a multiple of 6.')
    elif n % 2 ==0:
        print('The number' ,str(n), 'is an even number.')
    else:
        print('The number' ,str(n), 'is an odd number.')

#1.3.4 Function Test
print(food_id('apple'))
food_id_test()
f(1.1)
f(2)
f(3)
f(6)
f_test()
guess_once()
guess_once()
quiz_decimal(4, 4.1)
quiz_decimal(4, 4.1)
f_challenge(1.1)
f_challenge(2)
f_challenge(3)
f_challenge(6)