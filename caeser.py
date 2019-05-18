from collections import defaultdict
import matplotlib.pyplot as plt

data = open("input_file.txt", "r")
text = data.readline().rstrip('\n')
print(text)
key = 4

def encrypt(text,key):
 result = ""
 for i in range(len(text)):
    char = text[i]
    if char == ' ':
        result += ' '
    elif char.isupper():
        result += chr((ord(char) + key-65) % 26 + 65)
    else:
        result += chr((ord(char) + key - 97) % 26 + 97)
 return result


def countletters(file):
    results = defaultdict(int)
    for line in file:
        for char in line:
            c = char.lower()
            if c!=' ': results[c] += 1
    return results

ex= open("output_file.txt","w")
ex.write(encrypt(text,key))
ex.close()
print(encrypt(text , key))
#####

filename = "output_file.txt"
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
