from __future__ import print_function

'''Procedures'''
#1-4 N/A

'''Questions'''
#5 The type int, float, and long can represents 6 million

#6 There is an error for type('tr' + 5) because 'tr' is a string while 5 is an 
#  'int'. type('tr' + "y this") works because both of the types are strings.

#7 The way strings are counted is by numbering the sequence of characters in the
#  string. For example, 0 is assigned to M, 1 to y, 3 to space, 4 to s, etc. f
#  from left to right. Negative numbers will go from right to left, so t will be
#  -1, s will be -2, e will be -3, etc.

#8 Slicing, slogan[17:21]
#9 slogan[:13] + 'simply amazing!'

#10a It returns 7 because the value its assigned to, 'theater', is 7 characters.
#10b It returns theater without the last character, which is 'theate' because it
#  will become 7-1, activity[0:6]

#11 '' in '' tests if the 2nd string contains the 1st string somewhere in it.

#12 
def how_eligible(essay):
    '''Checks if a string of characters contain ? , " or ! and if so, adds 1 
    to a score and returns it'''
    score = 0
    for char in ["?","\"",",","!"]:
        if char in essay:
            score += 1
    
    return score
    
#1.3.5 Function Test
print(how_eligible('This? "Yes." No, not really!'))
print(how_eligible('Really, not a compound sentence.'))

# I got 4 and 1. I believe I did this assignment correctly.