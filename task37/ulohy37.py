import tkinter as tk


with open("./task37/ciernobiely_obrazok_1.txt", "r") as f:
    w, h = f.readline().strip().split()
    datas = [] # process stings(separate by2) and put them into list 
    for line in f.readlines():
        line = line.strip()
        datas.append([line[i:i+2] for i in range(0, len(line), 2)])

print(w,h)
print(int(w)*int(h))

# find frequency as ff -> 255
frequncy = [0,]*256
for line in datas:
    for digit in line:
        frequncy[int(digit, 16)]+=1
print(format(frequncy.index(max(frequncy)), "x"))

# creating graph
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

def create_graph():
    x = 10
    for freq in frequncy:
        canvas.create_rectangle(x,800 ,x+2, 500-freq*500/max(frequncy), fill="gray", outline="gray")
        x+=2
create_graph()

root.mainloop()