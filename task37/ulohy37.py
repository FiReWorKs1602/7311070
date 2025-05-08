import tkinter as tk


with open("./task37/ciernobiely_obrazok_1.txt", "r") as f:
    w, h = f.readline().strip().split()
    datas = []  
    for line in f.readlines():
        line = line.strip()
        for n in range(0,len(line), 2):
            datas.append(line[n:n+2])
# print(datas)

print(w,h)
print(int(w)*int(h))

frequency = [0,]*256
for num in datas:
    frequency[int(num, 16)]+=1
print(format(frequency.index(max(frequency)), "x"))


root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

def create_graph():
    x = 10
    for freq in frequency:
        canvas.create_rectangle(x,500 ,x+2, 500-freq*500/max(frequency), fill="gray", outline="gray")
        x+=2

create_graph()
root.mainloop()