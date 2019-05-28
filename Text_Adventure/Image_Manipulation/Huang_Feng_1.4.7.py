from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path  
import PIL
import PIL.ImageDraw 
from PIL import ImageOps, ImageFont, ImageDraw
import numpy as np
import pdb
import textwrap

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
    
    
def makeBorder(original_image, border=50, color1="red", color2= "blue", color3="orange", SqColor="blue",borderChoice="a"):
    """
    A function that creates a border around an image. A rectangle is drawn on 
    the 4 corners. If the borderChoice is a, it creates a vertical/horizontal 
    design for the frame. If borderChoice is b, it makes a border with 3 
    seperate colors in a striped pattern from top right to bottom left. The 
    color alternate in the pattern: color 1, color 2, color 1, color 3. The 
    given arguements for colors are translated to RGB and then used to create an
    numpyarray. The resulting numpy array is then converted and returned as an 
    PIL image.
    """
    # dimensions of given image
    widthOriginal, heightOriginal = original_image.size
    
    # dimensions of image with border
    width, height = widthOriginal+border*2, heightOriginal+border*2

    # Creates a new image with the size of the original image with a border
    img = PIL.Image.new('RGB', (width, height))
    pattern = np.array(img)
    
    # Generates a striped pattern (Horizontal and Vertical)
    
    if borderChoice == "a":
         for row in range(len(pattern)):
            for column in range(len(pattern[0])):
                if (column>border) and (column<(width-border)):
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
        
    # Generates a striped pattern (Diagonal)
    
    elif borderChoice == "b":
        
        # Iterates through all the pixels in the image
        
        for row in range(len(pattern)):
            for column in range(len(pattern[0])):

                if (row+column)/8 % 2 == 0:
                    # Even Stripe
                    pattern[row][column] = PIL.ImageColor.getrgb(color1) 
                    
                elif (row+column)/8 % 3 == 0:
                    # Odd stripe #1
                    pattern[row][column] = PIL.ImageColor.getrgb(color2)
                    
                else:
                    # Odd stripe #2
                    pattern[row][column] = PIL.ImageColor.getrgb(color3)
                    
    
    # Turns the numpy array into an image
    frame = PIL.Image.fromarray(pattern)
    
    SqColor = PIL.ImageColor.getrgb(SqColor)
    
    # Creates a ImageDraw instance of frame in order to use the draw module
    
    draw = ImageDraw.Draw(frame)
    
    # Draws 4 rectangles in the corner of the border
    
    draw.rectangle([(0,0),(border,border)], fill=SqColor, outline=None)
    draw.rectangle([(0,height-border),(border,height)], fill=SqColor, outline=None)
    draw.rectangle([(width-border,0),(width,border)], fill=SqColor, outline=None)
    draw.rectangle([(width-border,height-border),(width,height)], fill=SqColor, outline=None)

    return frame
    

def tintImage(original_image, r,g,b,a):
    """
    Takes a given image, as well as an r,g,b,a. Creates a new image with the rgb 
    values and changes the opacity based on the given alpha value. Then, it
    pasts the generated tint on top of the image and returns it.
    """
    
    # Creates tint with user inputed rgba
    
    tint = PIL.Image.new('RGBA', original_image.size, (r,g,b,a))
    
    # Pastes the tint on the image
    
    original_image.paste(tint,(0,0),tint)
    
    return original_image

def text_on_image(image, text, size, border, r,g,b):
    """
    Takes a given image and pastes text on it. It takes in rgb values to change
    the color of the text, as well as size. Writes the text in the middle of the 
    image (including borders) and pastes it 80% down the height of the image 
    (no border).
    """
    
    # Imports font file
    font = PIL.ImageFont.truetype("../text.ttf",size) 
    
    # Gets image and text values (size)
    width, height = image.size
    img = PIL.Image.new('RGBA', image.size, (0,0,0,0))
    write = PIL.ImageDraw.Draw(img)
    lines = textwrap.fill(text)
    w,h = font.getsize(lines)
    
    # Pastes the text and the image together
    write.text( ((width-w)/2, (height-((int(border))*3/2)) ),lines,(r,g,b),font=font)
    image.paste(img,(0,0),img)
    
    return image
    

def clientTwo(border, borderChoice,color1, color2, color3, tint, alphaImg, text, textColor, textSize, SqColor, directory=None):
    """
    Uses current directory if no directory is specified. Places images in 
    subdirectory 'modified', creating it if it does not exist. Takes in most 
    arguements from function user_input() and then inserts into other functions
    such as tintImage(), text_on_image(), and makeBorder(). Takes image and then
    runs through all the different functions, then pastes modified image in 
    border. Prints out image number when image processing is finished. Saves 
    image as a PNG in order to retain transparency.
    """
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    # Create a new directory 'modified'
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed  
    
    # Load all the images
    image_list, file_list = get_images(directory)  

    # Go through the images and save modified versions
    for n in range(len(image_list)):
        # Parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
        
        # dimensions of given image
        widthOriginal, heightOriginal = curr_image.size
    
        # dimensions of image with border
        width, height = widthOriginal+border*2, heightOriginal+border*2
        
        # Creates a path to American flag and reads it
        america_file = os.path.join(directory, "Test_Images/America.png")
        america_img = PIL.Image.open(america_file)
        
        # Resizes image based on the size of the image
        america_resize = america_img.resize((width*1/6, height*1/6))
        
        # Gets height and width of new resized image
        america_size = america_resize.size
        
        # Calls tint function to tint image
        r,g,b =  PIL.ImageColor.getrgb(tint)
        curr_image = tintImage(curr_image, r,g,b,alphaImg)
        
        # Calls text function to write text
        rText,gText,bText =  PIL.ImageColor.getrgb(textColor)
        curr_image = text_on_image(curr_image, text, textSize, border,rText,gText,bText)
        
        # Calls border function to create a border
        new_image = makeBorder(curr_image, border, color1, color2, color3, SqColor,borderChoice).convert("RGBA")
        new_image.paste(curr_image, (int(border), int(border)))
        
        # Pastes the American flag in top right corner
        new_image.paste(america_resize, ( ((new_image.size[0]-(america_size[0]+int(border)), (int(border))))), mask = america_resize)
         
        # Save the altered image, suing PNG to retain transparency
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
        # Print image number that it finished
        print(n+1)
        
    print("Images Finished")

    
def user_input():
    """
    Function that collects all the user inputs and enters them as parameters into
    the clientTwo() function. If there is a value error, it reruns that part of 
    the code until condition is satisfied that allows a proper value that can be
    entered into clientTwo()
    """
    condition = False
    
    print("\n===================== Border =====================")
    print("\nHow thick do you want your border to be?")
    print("Recommended: 50")
    try:
        border = int(raw_input("Border pixels >> "))
    except ValueError:
        print("Please enter an integer.")
        user_input()
    print("\nDo you want your border to be:")
    print("A) Vertical and Horizontal")
    print("B) Diagonal")
    print("Recommended: A\n")
    borderChoice = raw_input("Border Choice >> ").lower()
    if borderChoice == "a":
        print("\nWhat colors do you want you border to be? (2 for pattern + corner color)")
    elif borderChoice == "b":
        print("\nWhat colors do you want you border to be? (3 for pattern + corner color)")
    else:
        raise Exception("Border choice was not defined, please enter in a or b")
    print("Example: cyan")
    color1 = raw_input("Color 1 >> ")
    color2 = raw_input("Color 2 >> ")
    if borderChoice == "a":
        color3 = "black"
    if borderChoice == "b":
        color3 = raw_input("Color 3 >> ")
    SqColor = raw_input("Corner Color >> ")
    
    print("\n===================== Tint =====================")
    print("\nWhat do you want your opacity of the tint to be?")
    print("Please enter a number between 0 and 255")
    print("with 0 being no tint")
    print("And 255 being only able to see the tint.")
    print("Recommended: 75-100")
    while condition == False:
        try:
            alphaImg = int(raw_input("Alpha (transparent) Value >> "))
            if type(alphaImg) == int and alphaImg<=255 and alphaImg>=0:
                condition = True
            else:
                print("Please enter an integer between 0 and 255.")
        except ValueError:
            print("Please enter an integer between 0 and 255.")
    print("\nWhat color do you want your image to be tinted?")
    print("Example: cyan")
    tint = raw_input("Tint Color: ")
    
    print("\n===================== Text =====================")
    print("\nWhat do you want your text to say?")
    text = raw_input("Text >> ")
    print("\nWhat color do you want your text to be?")
    textColor = raw_input("Text Color >> ")
    print("\nHow large do you want your text to be?")
    print("Recommended: 40\n")
    textSize = int(raw_input("Text Size >> "))
    print("Creating Images...")
    
    # Calls clientTwo function with all of the user inputed choices
    clientTwo(border, borderChoice, color1, color2, color3, tint, alphaImg, text, textColor, textSize, SqColor)
    