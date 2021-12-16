import sys
import os
from PIL import Image

image_folder = sys.argv[1]
directory = sys.argv[2]

# use check if new exists, if not, create
if not os.path.exists(directory):
    os.makedirs(directory)

#loop through entire pokedex
for filename in os.listdir(image_folder): 
	img = Image.open(f'{image_folder}{filename}')
	clean_name = os.path.splitext(filename)[0]
	img.save(f'{directory}{clean_name}.png', 'png')
	print('all done!')


#convert to png

#save them to new folder 

