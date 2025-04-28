import tkinter as tk

with open("./task32/mapa.txt", "r") as f:
    mp = [line.strip("\n").split() for line in f.readlines()]

area = [0]*15
for line in mp:
    for num in line:
        if num != "0":
            area[int(num)-1]+=1

num_islands = 0
for i in area:
    if i != 0:
        num_islands+=1
print(num_islands)
print(max(area))        

#creating map
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

def create_map():
    for y_idx, line in enumerate(mp):
        for x_idx, pixel in enumerate(line):
            if pixel != '0':
                canvas.create_rectangle(x_idx*45,y_idx*45,x_idx*45+45,y_idx*45+45,fill="green")
            else:
                canvas.create_rectangle(x_idx*45,y_idx*45,x_idx*45+45,y_idx*45+45,fill="lightblue")

create_map()
root.mainloop()

