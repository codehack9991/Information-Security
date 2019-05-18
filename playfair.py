import re
from collections import defaultdict
import matplotlib.pyplot as plt
import string
import itertools

def chunker(seq, size):
    it = iter(seq)
    while True:
       chunk = tuple(itertools.islice(it, size))
       if not chunk:
           return
       yield chunk



def prepare_input(dirty):
    """
    Prepare the plaintext by up-casing it
    and separating repeated letters with X's
    """
    
    dirty = ''.join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""
    
    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty)-1):
        clean += dirty[i]
        
        if dirty[i] == dirty[i+1]:
            clean += 'X'
    
    clean += dirty[-1]

    if len(clean) & 1:
        clean += 'X'

    return clean

def generate_table(key):

    # I and J are used interchangeably to allow
    # us to use a 5x5 table (25 letters)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # we're using a list instead of a '2d' array because it makes the math 
    # for setting up the table and doing the actual encoding/decoding simpler
    table = []

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table

def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    # https://en.wikipedia.org/wiki/Playfair_cipher#Description
    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1*5+(col1+1)%5]
            ciphertext += table[row2*5+(col2+1)%5]
        elif col1 == col2:
            ciphertext += table[((row1+1)%5)*5+col1]
            ciphertext += table[((row2+1)%5)*5+col2]
        else: # rectangle
            ciphertext += table[row1*5+col2]
            ciphertext += table[row2*5+col1]

    return ciphertext


def decode(ciphertext, key):
    table = generate_table(key)
    plaintext = ""

    # https://en.wikipedia.org/wiki/Playfair_cipher#Description
    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1*5+(col1-1)%5]
            plaintext += table[row2*5+(col2-1)%5]
        elif col1 == col2:
            plaintext += table[((row1-1)%5)*5+col1]
            plaintext += table[((row2-1)%5)*5+col2]
        else: # rectangle
            plaintext += table[row1*5+col2]
            plaintext += table[row2*5+col1]

    return plaintext

def countletters(file):
    results = defaultdict(int)
    for line in file:
        for char in line:
            c = char.lower()
            if c!=' ': results[c] += 1
    return results


data = open("input_file.txt", "r")
text = data.readline().rstrip('\n')
#text = "My name is j"
key = 'assignment playfair'
cipher_text = encode(text, key)
ex= open("output_file2.txt","w")
ex.write(cipher_text)
ex.close()
print("Simple Text : ", decode(cipher_text, key))
print("Cipher Text : ",cipher_text)

#####

filename = "output_file2.txt"
file = open(filename, encoding="utf8")
d=countletters(file)
key_max = max(d.keys(), key=(lambda k: d[k]))
d = {k: v / d[key_max] for k, v in d.items()}
plt.title("Alphabet Frequencies in " + filename)
plt.ylabel("Total Number of Occurrences")
plt.xlabel("Frequency ranked letters")
lists = sorted((value, key) for (key,value) in d.items())
lists =sorted(lists, reverse=True)
print(d)
y, x = zip(*lists) # unpack a list of pairs into two tuples

plt.plot(x, y)
plt.show()
