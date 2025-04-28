import tkinter as tk

degree = " hagfedcc"
noty = "cdefgahcdahdecdefgahhagfdec"

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=200)
canvas.pack()

def create_page():
    for i in range(5):
        canvas.create_line(0,i*10+10, 500, i*10+10)

def create_note():
    x = 10
    for i in noty:
        canvas.create_oval(x-7,degree.index(i)*5+4+25,x+7, degree.index(i)*5-4+25)
        x+=18

create_page()
create_note()
root.mainloop()