import tkinter as tk
import random

with open("./task28/lodicky.txt", "r") as f:
    width, height = f.readline().strip().split(" ")
    l_map = [line.strip("\n").replace(" ","") for line in f.readlines()]

root = tk.Tk()
canvas = tk.Canvas(root,width=550,height=400)
canvas.pack()

def create_map(l_map: list)-> None:
    canvas.delete("all")
    for y_idx, line in enumerate(l_map):
        for x_idx, block in enumerate(line):
            x =55*x_idx
            y =55*y_idx
            if block == "0":
                canvas.create_rectangle(x,y,x+55,y+55, fill="lightblue", outline="lightblue")
            elif block == "1":
                canvas.create_rectangle(x,y,x+55,y+55, fill="gray", outline="gray")
            elif block == "2":
                canvas.create_rectangle(x,y,x+55,y+55, fill="yellow", outline="yellow")

def generate_ship(l_map =l_map)->None:
    select_line = random.randint(0,int(height)-1)
    temp = ""
    for i in range(int(width)-2):
        if l_map[select_line][i:i+3] == "000" and (l_map[select_line][i-1]!="2" or i == 0):
            temp+=l_map[select_line][:i]+"222"+l_map[select_line][i+3:]
            break
    if temp:
        create_map(l_map)
        l_map[select_line]=temp
    else:
        try:
            generate_ship()
        except:
            create_map(l_map)
            canvas.create_text(200, 200,font=("Arial", 20), text="it is full")
    
create_map(l_map)
tk.Button(root, command=generate_ship, text="add ship").pack()

root.mainloop()