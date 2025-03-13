import tkinter as tk

with open("./task22/sr.txt", "r") as f:
    data = f.read().split("\n") 

with open("./task22/sneh.txt", "r") as f:
    info = f.read().split("\n")

map_x = []
map_y = []
for ski_cor in data:
    x,y = ski_cor.split()[0], ski_cor.split()[1]
    map_x.append(int(x))
    map_y.append(int(y))

ski_cor = []
information =[]
for ski in info:
    x, y, data = ski.split()[0], ski.split()[1], ski.split()[2:]
    ski_cor.append([int(x),int(y)])
    information.append("".join(data))

root = tk.Tk()
canvas= tk.Canvas(root, width=800, height=800)
canvas.pack()
count = 0
def swich_info(event):
    canvas.delete("all")
    global count
    for idx in range(len(map_x)-2):# 1261 
        canvas.create_line(map_x[idx], map_y[idx]+90, map_x[idx+1], map_y[idx+1]+90)

    try:
        canvas.create_oval(ski_cor[count][0]-5,ski_cor[count][1]-5,ski_cor[count][0]+5,ski_cor[count][1]+5, fill="black")
        canvas.create_text(200,50,text=f"{information[count]}", font="Arial 15")
        count+=1
    except:
        root.quit()

swich_info("<Space>")
root.bind("<KeyPress>",swich_info)
root.mainloop()