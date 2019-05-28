""" Procedures """
#1-4 N/A

#5)  The names of the functions are round_corners_of_all_images(), get image(),
#    and round_corners_one_image().

#6)  The function took all the images in 1.4.5_Images and modified it, then 
#    prints out all image number and saves it in a new file called modified.

#7a) It is defined here to take 2 arguments. It has to be a PIL image.
#    Argument 1: original_image
#    Argument 2: percent_of_side 
#    Return value: masked image


#7b) (127,0,127,0) produces a purple transparent background.

#7c) Object created in line 26: rounded_mask
#    Object created in line 27: drawing_layer

#7d) You would need to hae an alpha value of 0, which means that it has a 
#    tranparent background for the corners and a solid color for middle part.

#7e) 2 rectangles lines 33-38
#    4 circles in 41-48

#7f) The color is purple.

#7g) The color values are (0,127,127), or light blue.

#8a) get_images() can be passed either 0 or 1 arguments.

#8b) It returns a 2-tuple list with a PIL.Image object for each image file and 
#    a string filename.

#8c) 
#    os.getcwd() 

#    os.listdir() 

#    os.path.join()

#8d) Return a string representing the path to which the symbolic link points.

#8e) It's open as it iterates through all the images. Some advantages are the 
#    the UI is more clean, but some disadvantages are if the user did not expect
#    the error then debugging will be made a lot harder.

#8f) It's so that if an IOError appears, it passes and the user doesn't see it.

#9a) It uses a try-except structure because if the image isn't able to be used, 
#    such as if the format was a .gif or .png or .jpg, you would need to skip 
#    that picture and move on to the next one. 

#9b) That number means all the images in the folder it iterated through.

#9c) The role of n is to act as the current image its on in the for loop and 
#    then making modifications to it.

""" Conclusion Questions """
#1   The reason why the icons on a desktop is not visible is because of its transperency. Because of that, you can see through the desktop  behind their irregular edges.



#2  well, smaller codes are easier to maintain and change, its easier to understand what the code is doing, and its also easier to fix if their is a bug. It made code reuse easier by moving
#common operations  into a seperate function.


#3   Yes, All photos are manipulated, even though they may look highly realistic, they aren't in the end. So for the brain, you're actually having light particles go into the eyes, so you 
#aren't "seeing" it isn't  "real image." Everything you see can be counted as manipulated images.


#4    The image would need to be yours in the first place, taken by you, and distributed by you. If the image is a famous place, or just someone in general, you will need to credit them. If
#you have all of these steps down, then you can sell it, or distribute it. However you like. 


#5    still currently doing the project.