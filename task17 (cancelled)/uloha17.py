import tkinter as tk
import random

random_code = str(random.randint(10000000, 99999999))

def generate_code(code, base_x = 10, base_y = 150):
    spacing_x= 10
    bar_lendth = 100
    diference = 20
    
    for idx, num in enumerate(code):
        if idx == 0 or idx == len(code)-1:
            cv.create_rectangle(base_x,base_y,base_x+int(num), base_y-bar_lendth, fill="black")
        else:
            cv.create_rectangle(base_x,base_y-diference,base_x+int(num), base_y-bar_lendth, fill="black")
        if idx == (len(code)-1)//2:
            cv.create_text(base_x+10,base_y-10, text=f"{code}")
        base_x += spacing_x

current_index = 0
def switch_code(event):
    cv.delete("all")
    global current_index
    with open("./task17/ciarkovy_kod_1.txt", "r") as file:
        lines = file.readlines()
        
        try:
            generate_code(lines[current_index].strip())
            generate_code(lines[current_index+1].strip(), 100)
            generate_code(lines[current_index+2].strip(), base_y=300)
            generate_code(lines[current_index+3].strip(), 100, base_y=300)
            current_index += 4
        except:
            current_index = 0

root = tk.Tk()
cv = tk.Canvas(root, height=500, width=500)
cv.pack()

generate_code(random_code)
root.bind("<space>", switch_code)

root.mainloop()