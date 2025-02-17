import tkinter as tk


with open("./task13/zastavba_na_ulici.txt", "r") as file:
    structures = []
    for data in file.readlines():
        structures.append(data.strip("\n").split())
    print(structures)

root = tk.Tk()
cv = tk.Canvas(root, width=600, height=200)
cv.pack()

def get_value():
    x = 10
    y = 150
    value = int(entry.get())
    for building in range(len(structures)-1):
        w = int(structures[building][0])
        h = int(structures[building][1])
        print(h)
        difference = h-int(structures[building+1][1])
        if (difference>value and int(structures[building+1][1]) != 0):
            cv.create_rectangle(x+w,y-h+difference,x+w,y-h, outline="red")
        if (difference < -value and int(structures[building][1]) != 0):
            cv.create_rectangle(x+w,y-h,x+w,y-h+difference , outline="red")
        x += w

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
cv.create_window(200, 170, window=entry)

botton = tk.Button(command=get_value, text="enter")
cv.create_window(200, 200, window=botton)

#initialize base
x = 10
y = 150

# create rectangles
for building in range(len(structures)):
    w = int(structures[building][0])
    h = int(structures[building][1])
    if h == 0:
        cv.create_rectangle(x,y,x+w,y-h, outline="green")
    else: 
        cv.create_rectangle(x,y,x+int(w),y-int(h)) 
    x += int(w)
root.mainloop()