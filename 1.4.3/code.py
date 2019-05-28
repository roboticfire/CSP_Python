from __future__ import print_function

#1
""" Woman 2 """

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig('women2')

print(type(img))
print(img)
print(len(img))
print(len(img[0]))
print(img[5][9][1])
print(img[4][10][0])
print(img[49][24][0])
"""

#2
""" Yellow Rectangle """

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
height = len(img)
width = len(img[0])
for row in range(200, 220):
    for column in range(50, 100):
        img[row][column] = [255, 255, 0] # red + green = yellow
fig.savefig('women2')
"""

#3
""" Green Earing """

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
height = len(img)
width = len(img[0])
for row in range(420, 480):
    for column in range(130, 180):
        img[row][column] = [0, 255, 0] #green

fig.savefig('green_earing.png')
"""

#4
""" Magenta Sky"""

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
fig.savefig("women_sky_earing.png")
"""

#5
""" Sky Earning """

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

height = len(img)
width = len(img[0])
for row in range(415, 480):
    for column in range(120, 160):
        if sum(img[row][column])>500: # brightness R+G+B goes up to 3*255=765
            img[row][column]=[0,255,0] # Green

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Saves the figure
ax.axis("off")
fig.savefig("women_sky_earing")
"""

#6
""" Make Mask """

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL
import random

def make_mask(rows, columns, stripe_width):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (row+column)**2/stripe_width % random.randint(1,2)*2 == 0: 
                image[row][column] = [0, 255, 255, 255] 
                
            elif random.randint(0,2) == 1:
                image[row][column] = [0, 0, 0, 255]
                
            else:
                image[row][column] = [0, 255, 127, 150] # magenta, alpha=255
    return image
    
if __name__ == "__main__":
    image = make_mask(100,100,20)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    ax.axis("off")
    fig.savefig('mask')            
"""

#7

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np    

'''Read the image data'''
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, "women_sky_earing_axis.png")
filename2 = os.path.join(directory, "mask.png")
img = plt.imread(filename)
img2 = plt.imread(filename2)

fig, ax = plt.subplots(1, 2)
ax[0].imshow(img, interpolation='none')
ax[0].axis("off")
ax[1].imshow(img2, interpolation='none')
ax[1].axis("off")

fig.savefig("women_and_mask.png")
"""

import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'no_axis.png')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img)
# Show the figure on the screen
# fig.show()
fig.savefig('women_and_mask.png')