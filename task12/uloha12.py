import tkinter as tk

expression = "(a+b)-)(a-b)*2("

root = tk.Tk()
canvas = tk.Canvas(root, height=200, width=400)
canvas.pack()

colors= ["red", "green", "blue", "orange", "purple", "cyan", "magenta"]
count = 0
is_right = True
for idx, brace in enumerate(expression):
    if brace =="(":
        canvas.create_text(10+10*idx, 10, text=brace, fill=colors[count])
        count += 1
    elif brace == ")":
        count -= 1
        canvas.create_text(10+10*idx, 10, text=brace, fill=colors[count])
    else:
        canvas.create_text(10+10*idx, 10, text=brace, fill="black")
    
    if count == -1:
        is_right = False
if count == 0 and is_right:
    canvas.create_text(10, 25, text="Uzatvorkovanie je spravne", fill="black", anchor="w")
else:
    canvas.create_text(10, 25, text="Uzatvorkovanie je nespravne", fill="red", anchor="w")

root.mainloop()