""" Procedure """
#1-3 N/A

""" Part I: Using Arrays of Pixels """
#4 Arrays and lists are both used in Python to store data, such as numbers, 
# strings, etc), and they both can be indexed and iterated through. Howver, if 
# you try to divide an array by 3, and each number in the array will be divided
# by 3 and the result will be printed if you request it. If you try to divide a 
# list by 3, Python will return an error.

#5 the image height = the number of rows of pixels = 960
#  the image width = the number of columns = 584
#  green intensity at (5,9) = 94
#  the red intensity at (4,10) = 62
#  the red intensity of the 25th pixel in the 50th row = 71

""" Part II: Manipulating Pixels """
#6 code.py #3

#7a It runs through all the rows and all the columns in that row. Then, if the 
#   sum of the values are greater than 500, it replaces that pixel with magenta.

#7b code.py

#7c code.py

#8 code.py

#9 code.py


""" Conclusion questions """
#1 The data in in a digital image is made out of a list, containing RGB and an 
#  optional opacity value. Altered means that the values are changed, resulting 
#  in a new color being created.

#2 A digital camera takes in light and turns the information given into a list 
#  of tuples in order to save the image. The light sensitive film will respond 
#  to light, and where it hits, it will physically change the color of the film.
#  They are similar as they both record the colors given and can be accessed/
#  viewed in the future.

#3a Larger place values have a larger impact. Smaller values, such as 0-63, 
#   have a smaller impact. 
 
#3b In binary, there are 6 possible spots for either 0 or 1. Therefore, 2*6 
#   means that there are 64 possible combinations,  indexing from 0 to 63.

#3c The quality of the image will become lower when only using 2 pixels.


#4  The computer would take a look at the values of every pixel in an image that
#   it comes across when you use a algorithm. When there is a sudden change, in
#   pixels, it might use another algorithm to determine if it was part of the 
#   original object or a new one.
