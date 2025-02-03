import tkinter as tk

with open("./task7/trasa_linky_metra.txt", "r") as f:
    data = f.read().split("\n")

cv = tk.Canvas(width=450, height=300)
cv.pack()

bar_width = 13
x_spacing = 20
y_base = 270
y_end = 255

cv.create_rectangle(5,262,len(data[1:])*x_spacing-5, 263)

for i, station in enumerate(data[1:]):
    x_start = 5 + x_spacing * i
    x_end = x_start + bar_width
    if i == 0 or i == len(data[1:])-1:
        cv.create_rectangle(x_start, y_base, x_end, y_end, fill=f"{data[0]}")
    elif "*" in station:
        
        cv.create_oval(x_start, y_base, x_end, y_end, fill="white")
    else:
        cv.create_oval(x_start, y_base, x_end, y_end, fill=f"{data[0]}")
    cv.create_text((x_start+x_end)/2, (y_base+y_end)/2-10, angle=45, font=("Arial", 10), text= station.strip("*"), anchor="w")

cv.mainloop()
