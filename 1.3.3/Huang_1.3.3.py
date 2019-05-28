from __future__ import print_function

'''Procedures'''
#1-5 N/A

'''Part 1: Conditionals'''

#6a Prediction: I think that the statement will return True, because 9 is >= 9 
#so the first statement will be True and the second statement will also be True  
#because not False = True.

#   My prediction was correct

#6b Prediction: I think the statement will True False because 5=5 is true and
#2 != 3, which is also true.

#   My prediction was correct

#7  Conditional (False)
x, y = (65, 40)
40<x and x<130 and 100<=y and y<=120

#8  Conditional (True)
x, y = (90, 115)
40<x and x<130 and 100<=y and y<=120

'''Part 2: if-else structure and the print() Function'''

#9    
def age_limit_output(age):
    '''Step 9b if-else, reports minimum age and inputed age relationship to 
    age limit'''
    AGE_LIMIT = 13          # convention: use CAPS for constants
    if age < AGE_LIMIT:
        print(age, 'is below the age limit.')
    else:
        print(age, 'is old enough.')
    print(' Minimum age is', AGE_LIMIT) 

#9a. Predictions:
#(10) it will return 10 is below the age limit then the minimum age
#It returned below age limit because 10 < 13, returning the if statement part
#(16) will return 16 is old enough then the minimum age
#it returned old enough because 16 != 13, thus returning the else part

#9b Grade Reporter

def report_grade(percent): 
    '''Step 9b if-else, reports 2 sentences based on the inputed percent grade
    and whether or not it indicates mastery'''
    if percent >= 80:
        print('A grade of ' + str(percent) + ' percent indicates mastery.')
        print(' Keep up the good work!')
    else:
        print('A grade of ' + str(percent) + ' percent does not indicate mastery.')
        print(' Seek extra practice or help.')

#10 
    #Out[]: True
    #as 3 is a value of [1,2,3]
    #Out[]: False 
    #as '3' is not a value of [1,2,3]
    
#11 Vowel Detector
def letter_in_word(guess, word):
    '''Determines if guess is in word, guess is = to 1 character'''
    if len(guess)==1:
        if guess in word:
            return True
        else:
            return False

#12 MasterMind
def hint(color, secret):
    '''Determines if color is in the list of colors in secret'''
    if color in secret:
        print('The color ' ,color, ' IS in the secret sequence of colors.')
    else:
        print('The color ' ,color, ' IS NOT in the secret sequence of colors.')
        
'''Conclusion'''

#1 For indents, the def should be the left most line, the next tab should be the 
#if, else, and elif statements, and the next tab should be their child functions.
#The child functions are ran if their parents, the if, else, or elif statements 
#are called by the arugments and parameters in the call and def line.

#2 Some ways to create Boolean statements are using math signs, such as ==, !=, 
# >=, etc. Other ways to return Boolean statements can be achieved by using 
#conditionals, such as if something in something: return True.

#3 Ira is right that the program will run the code twice, but it when she says 
# 'the program will run slower' isn't true because it will still be evaluated  
# the same amount of times because of the conditions for the if else statemtnts 
# path.

# Jayla is also correct, as the code will run no matter what because it is in
# both branches. Additionally, she is also correct that you would need to 
# 'change it in two places' as the print statement is repeated for both the if 
# and else statements.

# Kendra is right that the code will run no matter what because it is in
# both branches. Additonally, Kendra is also correct that it will take up a 
# little  less space in the python code, as it wont't have an extra line to run.

#1.3.3 Function Test
age_limit_output(10)
age_limit_output(16)
report_grade(79)
report_grade(85)
print(letter_in_word('t', 'secret hangman phrase'))
secret = ['red','red','yellow','yellow','black']
hint('red', secret)
hint('green', secret)