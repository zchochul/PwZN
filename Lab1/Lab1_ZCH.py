import string
from ascii_graph import Pyasciigraph
import rich
from rich.progress import track
import rich.traceback #do lapania wyjatkow
import sys
#n = int(sys.argv[1])
#print(n+1)

rich.traceback.install()
rich.get_console().clear()

path = "book.txt" 
number_of_visible_words = 4
limit_length = 4


if (len(sys.argv) >1) :
    rich.print('Otrzymano argumentow: \t', len(sys.argv))
    if (len(sys.argv) == 2):
        path = sys.argv[1]
    elif (len(sys.argv) == 3):
        path = sys.argv[1]
        number_of_visible_words = int(sys.argv[2])
    elif (len(sys.argv) == 4):
        path = sys.argv[1]
        number_of_visible_words = int(sys.argv[2])
        limit_length = int(sys.argv[3])
else:
    rich.print('W tym skrypcie można korzystać z argumentów. W takiej kolejności: sciezka do pliku, top ile wyrazow, limit dlugosci slow')

rich.get_console().rule('Lab1, czyli zobaczmy staty slow w ksiazce o weglu :blush:')
#from system arguments get...
rich.print('[bold]A to dopiero poczatek, popatrz na te ustawienia!!! :smiley:')
rich.print('Prawdziwe slowa zaczynaja sie od:', limit_length, 'literek')
rich.print('Chciales zobaczyc TOP ', number_of_visible_words, ' najczestszych slow!')
rich.print('Miejsce gdzie znajdziesz ten utwor -> ', path)
rich.get_console().rule('I ten wykres... Cos pieknego :heart:')


# Open the file in read mode
text = open(path, "r")

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
            if len(word) < limit_length:
                d[word] = 0
            else:
                d[word] = d[word] + 1
        else:
            # Add the word to dictionary with count 1
            d[word] = 1

# Print the contents of dictionary
#for key in list(d.keys()):
    #print(key, " ", d[key])

#sorting
sorted_dictionary = {k: v for k, v in sorted(d.items(), key=lambda item: item[1],  reverse=True)[:number_of_visible_words]}
#print(sorted_dictionary)

#histogram
graph = Pyasciigraph()
for line in  graph.graph('Ranking najczestszych slow', sorted_dictionary.items()):
    print(line)

