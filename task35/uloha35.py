import tkinter, random

root = tkinter.Tk()
canvas = tkinter.Canvas(root, width=700, height=800)
canvas.pack()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    canvas.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    canvas.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)


def Animation(record=[10]*15):
    canvas.delete("all")
    for i in range(15):
        record[i] += random.randint(1, 10)
        lodicka(record[i], i*50+30)
    canvas.create_line(650, 0, 650, 800, fill="red")
    if max(record) < 650:
        root.after(50, Animation)
    else:
        canvas.create_text(350, 400, text=f"vyhral lod cislo: {record.index(max(record))+1}", fill="red", font="Areal, 20")

canvas.create_line(650, 0, 650, 800, fill="red")
for i in range(15): 
    lodicka(10, i*50+30)
canvas.bind_all("<Key>", lambda e: Animation([10]*15))
root.mainloop()