from tkinter import *
fields = ('Plain Text', 'Cipher Text')


def encryption(entries):

    p_text = entries['Plain Text'].get()
    c_text = ""
    for char in p_text:
        if(char.islower()):
            c_text = c_text + chr(122 - ord(char) + 97)
        elif(char.isupper()):
            c_text = c_text + chr(90 - ord(char) + 65)
        else:
            c_text = c_text + char

    result = c_text
    entries['Cipher Text'].delete(0, END)
    entries['Cipher Text'].insert(0, result)


def decryption(entries):

    c_text = entries['Cipher Text'].get()
    p_text = ""
    for char in c_text:
        if(char.islower()):
            p_text = p_text + chr(122 - ord(char) + 97)
        elif(char.isupper()):
            p_text = p_text + chr(90 - ord(char) + 65)
        else:
            p_text = p_text + char

    result = p_text
    entries['Plain Text'].delete(0, END)
    entries['Plain Text'].insert(0, result)


def makeform(root, fields):
    entries = {}

    for field in fields:
        row = Frame(root)
        lab = Label(row, width=30, text=field + ": ", anchor='w')
        ent = Entry(row, highlightcolor="blue")
        #ent.insert(0, "0")
        row.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=LEFT, expand=YES, fill=BOTH)
        entries[field] = ent
    return entries


if __name__ == '__main__':
    root = Tk()
    root.title("PA:0")
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='Encrypt', fg="green",
                command=(lambda e=ents: encryption(e)))
    b1.pack(side=LEFT, padx=5, pady=5)

    b2 = Button(root, text='Decrypt', fg="red",
                command=(lambda e=ents: decryption(e)))
    b2.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()