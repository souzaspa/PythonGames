# Word Jumble Game

# ---------------------------------------------------
# Packages
from tkinter import *
from random import choice
from random import shuffle


# ---------------------------------------------------
# Functions
def answer():
    if word == myEntry.get():
        answer.config(text='\nCorreto!')
    else:
        answer.config(text='\nIncorreto!')


def hint(count):
    global hintCounter
    hintCounter = count
    wordLength = len(word)
    if count < wordLength:
        hintLabel.config(text=f"{hintLabel['text']} {word [count]}")

    hintCounter += 1


def shuffler():
    # Deletes Labels
    myEntry.delete(0, END)
    answer.config(text='')
    hintLabel.config(text="")
    # Clear global variable
    global hintCounter
    hintCounter = 0
    # Words list
    city = ['porto alegre', 'santa maria', 'santa cruz', 'passo fundo', 'viamao', 'alvorada', 'erechim',
            'lajeado', 'guaiba', 'canoas', 'esteio', 'gravatai', 'cachoeirinha', 'gramado', 'canela',
            'tramandai', 'pelotas', 'bage', 'osorio', 'alegrete', 'uruguaiana', 'chui', 'irai', 'vacaria',
            'sapiranga', 'sapucaia do sul', 'sao leopoldo', 'novo hamburgo', 'santa rosa', 'bento gonçalves',
            'farroupilha', 'caxias do sul', 'santana do livramento', 'campo bom', 'montenegro', 'parobe',
            'capao da canoa', 'canguçu', 'estancia velha', 'marau', 'santiago', 'panambi', 'eldorado do sul',
            'charqueadas', 'torres', 'rio pardo', 'dom pedrito', 'portao', 'igrejinha', 'garibaldi', 'estrela',
            'teotonia', 'morro reuter', 'carlos barbosa', 'nova prata', 'taquari', 'ivoti', 'encantado',
            'piratini', 'cidreira', 'agudo', 'feliz', 'cacequi']
    # Global variable to choice a word
    global word
    word = choice(city)
    # Transform to list
    break_word = list(word)
    # Shuffle the word
    shuffle(break_word)
    # Turn shuffleled list into a word
    global shuffled_word
    shuffled_word = ''
    for letter in break_word:
        shuffled_word += letter
    # Print the shuffle word on the screen
    myLabel.config(text=shuffled_word)


# ---------------------------------------------------
# GUI
root = Tk()
root.title('Adivinhe a cidade do Rio Grande do Sul')
root.geometry('500x410')
root.config(background='lightgreen')
root.resizable(False, False)


# ---------------------------------------------------
# Variables
global hintCounter
hintCounter = 0


# ---------------------------------------------------
# Widgets
myLabel = Label(root, text="", font=('Helvetica', 40), background='lightgreen')
myEntry = Entry(root, font=('Helvetica', 24))
button_frame = Frame(root, background='lightgreen')
myButton = Button(button_frame, text="Escolha outra palavra", command=shuffler)
answerButton = Button(button_frame, text="Responda", command=answer)
hintButton = Button(button_frame, text="Dica", command=lambda: hint(hintCounter))
answer = Label(root, text='', font=('Helvetica', 18), background='lightgreen')
hintLabel = Label(root, text='', font=('Helvetica', 18), background='lightgreen')


# ---------------------------------------------------
# Layouts
myLabel.pack(pady=20)
myEntry.pack(pady=20)
button_frame.pack(pady=20)
myButton.grid(row=0, column=0, padx=20)
answerButton.grid(row=0, column=1, padx=20)
hintButton.grid(row=0, column=2, padx=20)
answer.pack(pady=20)
hintLabel.pack(pady=20)


# ---------------------------------------------------
# Run the function
shuffler()


# ---------------------------------------------------
# MainLoop
root.mainloop()
