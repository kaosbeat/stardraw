from PIL import Image
import xml.etree.ElementTree as ET
import pickle
from itertools import cycle

### prepare data


def split_strings(strings):
    result = []
    for s in strings:
        for c in s:  # iterate over each character in the string
            result.append(c)  # add it to the result list
        result.append(' ')  # insert a space between strings

    return result

# Open the Pickle file in binary mode (rb)
with open('GentFirstNames.pickle', 'rb') as f:
    # Load the data from the Pickle file
    firstnames = pickle.load(f)

chars = cycle(split_strings(firstnames))


# cutchars = chars[0:100]
# print(cutchars)

### reads image
# Open the PNG image
img = Image.open('eye2.png')

# Get the width and height of the image
width, height = img.size

## SVG gen part
# Define the SVG document structure
root = ET.Element('svg')

charspace = 29.042/4
w = width*charspace 
h = height*charspace
root.set('width', str(w))  # adjust this value as needed
root.set('height', str(h))

# Set the global font family and font size
font_family = "BPdotsUnicaseSquare"
font_weight = "bold"
fontsizebase = 47.92390823/4
font_size = str(fontsizebase)+"px"

# # Iterate over each image pixel (x, y)
# for x in range(int(width)):
#     if (0 <= x < 1):
#         for y in range(int(height)):
#             r, g, b, a = img.getpixel((x, y))
#             text_element = ET.SubElement(root, 'text')
#             text_element.set('x', str(x*charspace )) 
#             text_element.set('y', str(y*charspace)) 
#             text_element.text = cycle(chars)
#             text_element.set('font-family', font_family)
#             text_element.set('font-size', str(font_size))
#             text_element.set('font-weight', str(font_weight))
#             text_element.set('fill', f'#{r:02x}{g:02x}{b:02x}')


# create larger textblocks for better performace
for y in range(int(height)):
    prevr = 1000 # can never be larger than 255 when taken from image, so new element will bestarted on check
    for x in range(int(width)):
        r, g, b, a = img.getpixel((x, y))
        if (r == prevr):
            #append
            print("stuf")
            text_element.text += next(chars)
        else:
            #start new element
            text_element = ET.SubElement(root, 'text')
            text_element.set('x', str(x*charspace )) 
            text_element.set('y', str(y*charspace))
            text_element.text = ""
            # a = cycle(chars)
            text_element.text += next(chars)
            text_element.set('font-family', font_family)
            text_element.set('font-size', str(font_size))
            text_element.set('font-weight', str(font_weight))
            text_element.set('fill', f'#{r:02x}{g:02x}{b:02x}')



# Write the SVG file to disk
tree = ET.ElementTree(root)
tree.write("output_groupedchars_horizontal.svg")