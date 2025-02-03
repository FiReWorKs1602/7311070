
import random
import tkinter as tk

def get_value():
    current_value = float(entry_var.get())
    if current_value == result:
        canvas.create_text(10, 20, text="spravne", font=("Arial", 10),anchor="w")
    else:
        canvas.create_text(10, 20, text="nespravne", font=("Arial", 10),anchor="w")

def create_circles():
    colors = ["red", "green", "blue", "orange", "purple", "cyan", "magenta", "yellow"]
    x, y = 10, 50  
    radius = 5  
    spacing = 5

    for i in range(0,num-(num%delitel)):
        color = colors[(i // delitel) % len(colors)]  
        canvas.create_oval(x, y, x + radius * 2, y + radius * 2, fill=color, outline="black")
        x += radius * 2 + spacing

    for i in range(num%delitel):
        color = colors[(i // delitel) % len(colors)]  
        canvas.create_oval(x+10, y, x + 10 + radius * 2, y + radius * 2, fill=color, outline="black")
        x += radius * 2 + spacing

num = random.randint(11,20)
delitel = random.randint(2,10)
task = f"{num} : {delitel} = "
result = num // delitel


root = tk.Tk() 
canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# create text
canvas.create_text(10,10 , text=task, font=("Arial", 10),anchor="w")

# create entry
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
canvas.create_window(200, 150, window=entry)

# create pole
b = tk.Button(root, command=get_value, text="skontroruj").pack()

#create circles
create_circles()

root.mainloop()