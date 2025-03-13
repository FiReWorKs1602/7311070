import tkinter as tk

with open("./task21/krizovka1-1.txt", "r") as f:
    data = f.read().split("\n")

answer_pos = []
words = []
for line in data:
    answer_pos.append(line.split()[0]) 
    words.append(line.split()[1])


# Constants
CANVAS_WIDTH = 500
CANVAS_HEIGHT = 300
BASE_X = 20
BASE_Y = 20
LETTER_SPACING = 20
RECTANGLE_SIZE = 10

# Initialize the main window
root = tk.Tk()
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Iterate through each word and its position
def krizovka(BASE_X, BASE_Y, text = False):
    for pos, word in enumerate(words):
        shift = LETTER_SPACING * (len(words[0]) - int(answer_pos[pos]))
        for idx, letter in enumerate(word):
            x = BASE_X + LETTER_SPACING * idx + shift
            y = BASE_Y
            
            if idx == int(answer_pos[pos]) - 1:
                canvas.create_rectangle(x - RECTANGLE_SIZE, y - RECTANGLE_SIZE, x + RECTANGLE_SIZE, y + RECTANGLE_SIZE, fill="gray")
            else:
                canvas.create_rectangle(x - RECTANGLE_SIZE, y - RECTANGLE_SIZE,x + RECTANGLE_SIZE, y + RECTANGLE_SIZE)
            if text:
                canvas.create_text(x, y, text=letter, font="JetBrainsMono")
        
        BASE_Y += LETTER_SPACING

krizovka(BASE_X, BASE_Y)
krizovka(BASE_X+200, BASE_Y, text=True)
root.mainloop()
