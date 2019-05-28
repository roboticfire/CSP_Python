""" Procedures """
#1-8  N/A (Part 1)

#9-12 N/A

#13a) matplotlib.pyplot is used to create interactive plots on pictures.+
  
#13b) numpy is used for large, multi-dimensional arrays and matrices along with
#     some high-level mathematical functions.

#13c) PIL is used for opening, manipulating, and saving many different image 
#     file formats.

#14)  %run 1.4.4/earthEyes.py

#15a) Line 19 calls the function subplots from the PLT library. The function is
#     being called with 2 argument(s): 1 and 2. The function returns 2 object(s)
#     which is/are being assigned to fig and ax.

#15b) Line 20 calls imshow() on ax[0]
#     Line 23 calls imshow() on ax[1]
#     Line 24 calls set_xticks() on ax[1]
#     Line 25 calls set_xlim() on ax[1]
#     Line 26 calls set_ylim() on ax[1]
#     Line 27 calls savefig() on fig

#15c) The upper left corner is (700,925). The upper right corner is (966,1253)
#     The lower left corner is (1059,1162). The lower right corner is (1059,1253) 

#16)  The coordinates are (700,925). The range is 970,1050 for the y-axis and
#     1170,1270 for the x-axis. The box is 80 px on the top and 100 px on the 
#     bottom.

#17a) Line 30 uses the join() method from the os.path module. It is being passed
#     2 arguments. The value it returns is being assigned to the variable 
#     earth_file.

#17b) In line 31 the open() function of the PIL.Image module returns a new 
#     PIL.Image object, which is being assigned to the variable earth_img.

#17c) There are 2 parenthesis because the first set takes in the arguments 
#     entered, and the second pair defines the arguments as a 2-tuple list

#17d) The purpose of (89,87) is to determine the bounding box of the figure.


#17e) Line 30 calls the method join() on the object earth_file with 2 argument(s): directory, "earth.png".
#     Line 31 calls the method open() on the object earth_img with 1 argument(s): earth_file.
#     Line 32 calls the method resize() on the object earth_small with 1 argument(s): (89, 87).
#     Line 33 calls the method subplots() on the object fig2, axes2 with 2 argument(s): 1, 2.
#     Line 34 calls the method imshow() on the object axes2[0] with 1 argument(s): earth_img.
#     Line 35 calls the method imshow() on the object axes2[1] with 1 argument(s): earth_small.
#     Line 36 calls the method savefig on the object fig2 with 1 argument(s): "resize_earth".

#17i) Another argument is reasample.

#17ii)The default value is "1" or "P".

#17iii)A value of 2 is recommended.

#17g) A 2 tuple of (width,height)

#17h) print(earth_img.size) prints the (height,width) of earth_img
#     print(earth_small.size)prints the (height,width) of earth_small
#     print(earth_img.size[1]) prints the width of earth_img

#17i) You can tell because the second picture has a lower resolution, meaning 
#     that it uses less pixels.

#18)  The algoritum resize() might be using is first dividing the picture into
#     x different sections based on the width and height. Then, it will take the
#     average of RGB of all the pixels around it and merge the RGB of the entire 
#     section into the new, average RGB.

#19a) student_img bytes = 479 x 475 x 3 = 682,575 bytes
#     earth_small bytes = 89 x 87 x 4 = 30,972 bytes

#19b) File explorer properties

#19c) student.jpg bytes = 2,192,468 bytes
#     smallEarth.png bytes = 18,725 bytes

#19d) The dicreptancies could be from additional data being stored with the 
#     image or other compression data.

#19e) Instead of an image, the source can be a integer or tuple containing pixel
#     values. The method then fills the region with the given color.

#19f) If the modes don’t match, the pasted image is converted to the mode of 
#     this image.

#19g) earth_small is the source image, (1162, 966) is the location of the top 
#     left corner, and mask is the optional mask image

#20) earthEyes.py


""" Conclusion Questions """
#1   In order to change images, we used the methods resize(), paste(), and open() 
#    from the PIL library. A couple of the attributes are region and images

#2   Instead of doing all the PIL resized the image of you, saving a lot of time    