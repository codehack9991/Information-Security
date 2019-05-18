from collections import defaultdict
import matplotlib.pyplot as plt

def countletters(file):
    results = defaultdict(int)
    for line in file:
        for char in line:
            c = char.lower()
            if c!=' ': results[c] += 1
    return results

ASC_A = ord('A')
TABLE_WIDTH = 26


def init_table():
    return [[chr((col + row) % TABLE_WIDTH + ASC_A) \
             for col in range(TABLE_WIDTH)] \
            for row in range(TABLE_WIDTH)]



def print_table(table):
    output = ''
    for row in range(0, len(table)):
        for col in range(0, len(table[row])):
            output = output + table[row][col] + ' '
        output = output + '\n'
    print(output)


def encrypt(table, key, words):
    cipher = ''
    count = 0
    key = key.upper()

    for ch in words.upper():
        if str.isalpha(str(ch)):
            key_shift = ord(key[count % len(key)]) - ASC_A
            word_shift = ord(ch) - ASC_A
            cipher += table[key_shift][word_shift];
            count += 1

    return cipher

def decrypt(table, key, words):
    text = ''
    count = 0
    key = key.upper()
    for ch in words.upper():
        shift = ord(ch) - ord(key[count % len(key)])
        text += chr((shift + TABLE_WIDTH) % TABLE_WIDTH + ASC_A)
        count += 1
    return text.lower()


secret = "computer";
data = open("input_file.txt", "r")
text = data.readline().rstrip('\n')

table = init_table()
print_table(table)

ciphertext = encrypt(table, secret, text)
ex= open("output_file.txt","w")
ex.write(ciphertext)
ex.close()
print("Simple Text : ", decrypt(table, secret, ciphertext))
print("Cipher Text : ",ciphertext)
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

