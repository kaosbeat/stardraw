import pickle

# Open the Pickle file in binary mode (rb)
with open('GentFirstNames.pickle', 'rb') as f:
    # Load the data from the Pickle file
    firstnames = pickle.load(f)

# print(loaded_values)  # prints the list of strings



char_count = sum(len(s) for s in firstnames)
plusspaces = char_count + len(firstnames)

print("total charcount: " ,char_count)  # prints 7
print("tatal length + spaces: " , plusspaces)
print("average name length: " ,char_count/len(firstnames))



