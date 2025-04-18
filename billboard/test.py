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

i=0
while (i < 100):
    print(next(chars))
