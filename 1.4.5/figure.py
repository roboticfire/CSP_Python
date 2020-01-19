import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'basketball.JPG')
filename2 = os.path.join(directory, 'basketball.png')
# Read the image data into an array
img = plt.imread(filename)
img2 = plt.imread(filename2)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[0].set_title("Original Image")
ax[1].imshow(img2, interpolation='none')
ax[1].set_title("Modified Image")
# Saves the figure
fig.savefig('basketball.join.png')