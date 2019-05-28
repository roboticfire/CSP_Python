#1
""" Woman Plot """

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
# Show the figure on the screen
# fig.show()
fig.savefig('women_plot')
"""

#2
""" cat1-a.gif Plot """

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
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat1-a.gif_plot')
"""

#3
""" Multiple Plots """
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
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('file_name')
"""

#4
""" Creates woman2plot 2 plots of woman.png"""

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
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('woman2plot')
"""

#5
""" Creates cat1-a.gif5plot 5 plots of cat1-a.gif"""
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
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('cat1-a.gif5plot')
"""

#6 
""" Leaf Earing """
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

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')
"""

#7
""" Expirements"""
"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np    

directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'cat1-a.gif')
filename2 = os.path.join(directory, 'mice.jpg')
img = plt.imread(filename)
img2 = plt.imread(filename2)

fig, ax = plt.subplots(1, 4)
ax[0].imshow(img2) 
ax[0].set_title("Test 1")

ax[1].imshow(img)
ax[1].set_ylim(120,80)
ax[1].axis("off")

ax[2].imshow(img)
ax[2].set_xlim(20,50)
ax[2].set_ylim(50,80)

ax[3].imshow(img2)
ax[3].set_xlim(50,100)
ax[3].set_xlim(100,50)
ax[3].set_title("Hellooooo")

fig.savefig('expirement.png')
"""

#8
""" 3 Close ups """

"""
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np    

directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'cat1-a.gif')
img = plt.imread(filename)

fig, ax = plt.subplots(1, 3)
ax[0].imshow(img, interpolation='none') 
ax[0].set_xlim(20,30)
ax[0].set_ylim(50,60)

ax[1].imshow(img, interpolation='none')
ax[1].set_xlim(30,40)
ax[1].set_ylim(50,60)

ax[2].imshow(img, interpolation='none')
ax[2].set_xlim(40,50)
ax[2].set_ylim(50,60)

fig.savefig('three_closeup.png')
"""

#9
""" Crazy Mice """

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
filename = os.path.join(directory, 'mice.jpg')
print "file:", filename 
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 1)
# Show the image data in a subplot
ax.imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
ax.plot(117, 43, 'ro')
ax.plot(139, 43, 'ro')
ax.plot(37, 48, 'ro')

fig.savefig('crazymice_plot')
"""


from __future__ import print_function
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

###
# Make a rectangle of pixels yellow
###

height = len(img)
width = len(img[0])
for row in range(420, 470):
    for column in range(135, 162):
        img[row][column] = [0, 255, 0] # red + green = yellow
    
