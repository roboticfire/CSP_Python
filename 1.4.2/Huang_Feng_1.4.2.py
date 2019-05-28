""" Procedures """
# 1-3 N/A


""" Part I: Working with a Filesystem """
# 4 C:/Users/Studentlogin/Desktop/nice.jpg

# 5 ../Studentlogin/Desktop/nice.jpg

#6 This is an absolute filepath as it include all points because it starts with 
#  a C:/. You have to be in a certain directory because if you didn't, it would
#  interpret the answer as a relative, rather than absolute filepath. Cloud9 is
#  different as it starts with u, which means that it is stored in a cloud
#  rather than locally.


""" Part II: Rendering an Image on Screen: """
#7 The first code does not work.

#  The second code works.

"""
The differences in the code are that when importing other libraries, the second 
program imported mathplotlib first as well as the module "use()" with the 
parameter og 'Agg'. Additionally, the other program only showed the picture, 
but the second one saved the image to a new file.
"""
#  code.py #1

#  code.py #2


#7a The woman's nose is at (272, 412).

#7b The cat's nose is at (60,40).

""" Part III: Objects and Methods """
#8a fig is an instance of the class Figure.
#   ax is an instance of the class AxesSubplot.

#8b Similarly, in line 25, the method savefig is being called on the object 
#   fig. That method is being given 1 argument. That method is a method of the 
#   class Figure.

#8c The method savefig is being called on object fig and saved as "fig_plot"

#9a The method imshow is being called on the object ax[0]

#9b I: code.py #4

#9b II: code.py #5

""" Part V: Keyword = Value Pairs """
#10 code.py #6

#11a code.py #7

#11b code.py #8

#12 One method of AxesSubplot is normed. The default is true.

#13  code.py #9

""" Conclusion Questions """

#1 An absolute filename would be the path starting from the very first directory
#  to whichever file you wanted to get to. A relative filename, on the other 
#  hand, is the relative path to the file that is determined by a directory you 
#  are currently in, which is also not the root directory.


#2 An object could be an instance of a class, a variable, or anything that 
#  contains data in python.


#3 Properties are the values that are stored in objects, such as instances and
#  variables, which are assigned things like age, cost, color, etc. A method is 
#  a function of the class that can be used on instances in order to alter their
#  properties.

    
#4 When a method is called on an object, based on the arguments given and/or 
#  initialized values, the object’s values that are stored in it changes based 
#  on the code. Then, python updates the object with new values provided by the
#  method and returns it back to the program.

 