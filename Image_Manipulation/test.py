from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw 
from PIL import ImageOps, ImageDraw
import numpy as np
import pdb

# def test(original_image, percent_of_side=.3, position="TL", picture="football"):
    
#     width, height = original_image.size

#     rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
#     drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
#     drawing_layer.polygon([(0,0),(width,0),
#                             (0,height),(width,height)],
#                             fill=(127,0,127,120))
                         
#     # Uncomment the following line to show the mask
#     plt.imshow(rounded_mask)
    
#     result = PIL.Image.new('RGBA', original_image.size, (0,120,120,5))
#     result.paste(original_image, (0,0), mask=rounded_mask)

#     rounded_mask.save("test.png")                                           


def makeBorderOne(originalImage, border=50, color1="red", color2= "blue", color3="orange"):
    original_image = PIL.Image.open(originalImage)
    widthOriginal, heightOriginal = original_image.size
    width, height = widthOriginal+border*2, heightOriginal+border*2

    
    #start with transparent mask
    img = PIL.Image.new('RGB', (width, height))
    pattern = np.array(img)
    for row in range(len(pattern)):
        for column in range(len(pattern[0])):
            if not(row>border and row<(width-border-10) and column>border and column<(height-border+8)):
                if (row+column)/8 % 2 == 0:
                    
                
                # if width%2 == 0:
                    #(r+c)/w says how many stripes above/below line y=x
                    # The % 2 says whether it is an even or odd stripe
                    
                    # pdb.set_trace()
                    
                    # Even stripe
                    
                    #PIL.ImageColor.getrgb()
                    pattern[row][column] = PIL.ImageColor.getrgb(color1) 
                    
                elif (row+column)/8 % 3 == 0:
                    pattern[row][column] = PIL.ImageColor.getrgb(color2)
                else:
                    # Odd stripe
                    pattern[row][column] = PIL.ImageColor.getrgb(color3)
            else:
                pattern[row][column] = [0, 0, 0]
    # pdb.set_trace()
    frame = PIL.Image.fromarray(pattern)
    frame.save("frametest.png")
    
    # rounded_mask = PIL.Image.new('RGBA', (int(width*0.8), int(height*0.8)), (0,0,0,255))
    # frame = pattern2.paste(rounded_mask, (int(width*0.1), int(height*0.1)), mask=rounded_mask)
    """
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    
    # https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new
    
    # Overwrite the RGBA values with A=255.
    # The 127 for RGB values was used merely for visualizing the mask
    
    # Draw two rectangles to fill interior with opaqueness
    rounded_mask = PIL.Image.new('RGBA', (width, height), (127,0,127,0))
    drawing_layer = PIL.ImageDraw.Draw(rounded_mask)
    drawing_layer.polygon([(0,0),(width,0),
                            (0,height),(width,height)],
                            fill=(127,0,127,120))
    """
                         
    # Uncomment the following line to show the mask
    # plt.imshow(rounded_mask)
    
    # Make the new image, starting with all transparent
    original_image.save("imagetest.png")

    # pdb.set_trace()
    frame.paste(original_image, (int(border), int(border)), mask=original_image)
    
    frame.save("result.png")
    
def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

# def client2(directory=None):
#     """ Saves a modfied version of each image in directory.
    
#     Uses current directory if no directory is specified. 
#     Places images in subdirectory 'modified', creating it if it does not exist.
#     New image files are of type PNG and have transparent rounded corners.
#     """
    
#     if directory == None:
#         directory = os.getcwd() # Use working directory if unspecified
        
#     # Create a new directory 'modified'
#     new_directory = os.path.join(directory, 'modified')
#     try:
#         os.mkdir(new_directory)
#     except OSError:
#         pass # if the directory already exists, proceed  
    
#     # Load all the images
#     image_list, file_list = get_images(directory)  

#     # Go through the images and save modified versions
#     for n in range(len(image_list)):
#         # Parse the filename
#         print(n)
#         filename, filetype = os.path.splitext(file_list[n])
        
#         # Round the corners with default percent of radius
#         curr_image = image_list[n]
#         new_image = makeBorder(curr_image) 
        
#         # Save the altered image, suing PNG to retain transparency
#         new_image_filename = os.path.join(new_directory, filename + '.png')
#         new_image.save(new_image_filename)    


def Bordertest(original_image, border=50, color1="red", color2= "orange", color3="orange",SqColor="blue", borderChoice="b"):
    """
    Makes a border with 3 seperate colors in a striped pattern from top right to
    bottom left. The color alternate from color 1, color 2, color 1, color 3. 
    Leaves a empty section in the middle that is the same width and height as
    the given image. The default arguements for colors are translated to RGB and
    then used to create an numpy array. The resulting numpy array is then 
    returned as an PIL image with RBG.
    """
    
    original_image = PIL.Image.open(original_image)

    # dimensions of given image
    widthOriginal, heightOriginal = original_image.size
    
    # dimensions of image with border
    width, height = widthOriginal+border*2, heightOriginal+border*2

    # Creates a new image with the size of the original image with a border
    img = PIL.Image.new('RGB', (width, height))
    pattern = np.array(img)
    SqColor = PIL.ImageColor.getrgb(SqColor)

    # Generates a striped pattern
    
    if borderChoice == "a":
        for row in range(len(pattern)):
            for column in range(len(pattern[0])):
                
                # Condition that stops the pattern from generating in the image space

                if (row+column)/8 % 2 == 0:
                    # Even Stripe
                    pattern[row][column] = PIL.ImageColor.getrgb(color1) 
                    
                elif (row+column)/8 % 3 == 0:
                    # Odd stripe #1
                    pattern[row][column] = PIL.ImageColor.getrgb(color2)
                    
                else:
                    # Odd stripe #2
                    pattern[row][column] = PIL.ImageColor.getrgb(color3)
                    
    elif borderChoice == "b":
         for row in range(len(pattern)):
            for column in range(len(pattern[0])):
                if (row>border) and (row<(width-border)):
                    if row % 10 == 0:
                        pattern[row][column] = PIL.ImageColor.getrgb(color1)
                        pattern[row+1][column] = PIL.ImageColor.getrgb(color1)
                        pattern[row+2][column] = PIL.ImageColor.getrgb(color1) 
                        pattern[row+3][column] = PIL.ImageColor.getrgb(color1) 
                        pattern[row+4][column] = PIL.ImageColor.getrgb(color1)
                else:
                    if column % 10 == 0:
                        pattern[row][column] =  PIL.ImageColor.getrgb(color1)
                        pattern[row][column+1] = PIL.ImageColor.getrgb(color1)
                        pattern[row][column+2] = PIL.ImageColor.getrgb(color1)
                        pattern[row][column+3] = PIL.ImageColor.getrgb(color1)
                        pattern[row][column+4] = PIL.ImageColor.getrgb(color1)
                        
                if pattern[row][column][0] == 0 and pattern[row][column][1] == 0 and pattern[row][column][2] == 0:
                    pattern[row][column] =  PIL.ImageColor.getrgb(color2)
    
    # Turns the numpy array into an image
    frame = PIL.Image.fromarray(pattern)
    
    draw = ImageDraw.Draw(frame)
    
    draw.rectangle([(0,0),(border,border)], fill=SqColor, outline=None)
    draw.rectangle([(0,height-border),(border,height)], fill=SqColor, outline=None)
    draw.rectangle([(width-border,0),(width,border)], fill=SqColor, outline=None)
    draw.rectangle([(width-border,height-border),(width,height)], fill=SqColor, outline=None)

    frame.save("ImageDraw.png")