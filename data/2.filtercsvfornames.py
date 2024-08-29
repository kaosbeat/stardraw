

import re
import pickle

def extract_values(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    results = []
    for line in lines:
        # print(line)
        parts = line.split(',')
        # print(parts)
        value = parts[2]
        results.append(value)

    return results

filename = "Gent.csv"  # replace with your file name
values = extract_values(filename)
print(values)  # prints a list of strings, each representing the extracted value




# Save values to pickle file
with open('GentFirstNames.pickle', 'wb') as f:
    pickle.dump(values, f)