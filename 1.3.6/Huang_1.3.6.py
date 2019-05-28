import random

'''Procedures'''
#1-3 N/A

'''Part I: Tuples, Syntax'''
#4 (2,30,3) is a tuple.

#5 You can't go beyond a certain point when typing, your have to use comments 
#  for your answers, and use MLA format when submitting. For Python variables 
#  fixed variables should be in all caps, while others are lowercase.

#6 I predict that it will return b. It returned b because when you number the 
#  tuple from 0-2, item number 1 will be 'b'.
#  I predict that it will print 'a', 'b', as [0:2] means it includes 0-(2-1), or
#  items 0 and 1.

#7 I predict that it will return true because b can't change which means that 
#  the second item in the tuple will also be 10. 
#  I predict that it will return 15 because you are assigning b to a new tuple 
#  with the updated value in which a is now 15.

'''Part II: Lists'''
#8 I predict that it will print from b to the end, as item [1] is b and : means 
#  to either the beginning or the end.

#9 It returned false because you assigned the value of '3', which is a string, 
#  to value[2]. As a result, a string is not == to an int, so thus it returned 
#  false.

#10a It added the values 4 and 5 to the end of the list.
#10b It added [6,7] to the list as there were parenthesis around the brackets.

#11 It doesn't work because you can only concatenate lists to lists.

#12 It returns 18 because it multiplies a by 3, then assigns a to the new value.

'''Part III: Lists and the random module'''

#13 import random

#14 
def roll_two_dice():
    '''Simulates rolling 2 dice and adding up the result'''
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1 + dice2
    
'''Conclusion'''
#1 a, b, and c are different because a is a string, b is a tuple, and c 
#  is a list. Additionally, b is non-mutable as it is a tuple and can only
#  concatenate lists, but lists are mutable and can be changed.

#2 There can't be only an integer because there are necessary uses for others, 
#  like string to print, floats for decimals, lists to store, etc.

#3 You can define functions by using def functionname(parameters): and then the
#  body below. Inside, you can return things for either the computer or the user
#  to see by using either print or return. Strings are defined by using '' and 
#  can be printed. Integers are numbers like 3, 5, or 7. Floats can contain
#  decimals, like 3.0, 4.5, etc. Lists are defined using [], and tuples are 
#  defined by using (). For loops are repeatly run for all the values in the 
#  list/string, and is useful when checking a list for a certain item/character.


#1.3.6 Function Test
print(roll_two_dice())
