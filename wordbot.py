import PySimpleGUI as sg
from utils import get_meaning, get_synonyms, get_antonyms
sg.theme('Purple')

greeting = "Hello, I am a word bot. I can help you with words\n"

layout = [
    [sg.Multiline(greeting, font=("Time New Roman", 14), disabled=True,size=(70, 15), key='output')],
    [sg.InputText("", font=("Times New Roman", 14), size=(50, 1), key='input', enable_events=True)],
    [sg.Button("Meaning", font=("Times New Roman", 14), bind_return_key=True, key='meaning'),
     sg.Button("Synonyms", font=("Times New Roman", 14), key='synonym'),
     sg.Button("Antonyms", font=("Times New Roman", 14), key='antonym'),
     sg.Button("Clear", font=("Times New Roman", 14), key='clear')
    ]
]

def display_meaning(word):
    meaning = get_meaning(word)
    window['output'].print("WORD: " + word)
    if meaning:
        window['output'].print("MEANING: ", meaning)
    else:
        display_error("Word is not found in corpus")

def display_synonyms(word):
    synonym = get_synonyms(word)
    window['output'].print("WORD:"+word)
    if synonym:
        window['output'].print("SYNONYMS:", list(synonym))
    else:    
        display_error("Word is not found in corpus")

def display_antonyms(word):        
    antonym= get_antonyms(word)
    window['output'].print("WORD:"+ word)
    if antonym:
        window['output'].print("ANTONYMS:", antonym)
    else:    
        display_error("Word is not found in corpus")

def clear():
    right


def display_error(message):
    window['output'].print("ERROR: " + message, text_color='red')


if __name__ == '__main__':
    window = sg.Window('File Explorer', layout)

    while True:
        event, values = window.Read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'meaning':
            display_meaning(values['input'])
        elif event == 'synonym':    
            display_synonyms(values['input'])
        elif event == 'antonym':    
            display_antonyms(values['input'])
        elif event =='clear':
            window.FindElement('output').Update(greeting)
    window.Close()