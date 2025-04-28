import tkinter as tk


with open("./task36/preklopenie_obrazka.txt", 'r') as f:
    w, h = f.readline().strip().split()
    data = [i.strip().split() for i in f.readlines()]

root = tk.Tk()
canvas = tk.Canvas(root, width=w, height=h)
canvas.pack()
 
def create_img():
    canvas.delete("all")
    for y_idx, line in enumerate(data):
        for x_idx, element in enumerate(line):
            if element == "1":
                canvas.create_oval(x_idx,y_idx,x_idx,y_idx, fill="black")
def rotate():
    for line in range(len(data)):
        data[line] = data[line][::-1]
    create_img()

create_img()
bt = tk.Button(text="rotate", command=rotate).pack()

root.mainloop()