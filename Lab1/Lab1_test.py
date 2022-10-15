import string
  
# Open the file in read mode
text = open("book.txt", "r")
  
# Create an empty dictionary
d = dict()
  
# Loop through each line of the file
for line in text:
    # Remove the leading spaces and newline character
    line = line.strip()
  
    # Convert the characters in line to
    # lowercase to avoid case mismatch
    line = line.lower()
  
    # Remove the punctuation marks from the line
    line = line.translate(line.maketrans("", "", string.punctuation))
  
    # Split the line into words
    words = line.split(" ")
  
    # Iterate over each word in line
    for word in words:
        # Check if the word is already in dictionary
        if word in d:
            # Increment count of word by 1
            d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1
  
# Print the contents of dictionary
#for key in list(d.keys()):
    #print(key, " ", d[key])

#sorting
#print(sorted(d.values())[:5])
sorted_dictionary = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],  reverse=True)[:10]}
print(sorted_dictionary)
# Print the contents of dictionary
#for key in list(d.keys()):
#    print(key, ":", d[key])
#print(list(d.items())[:4])
