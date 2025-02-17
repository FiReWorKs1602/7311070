import tkinter as tk

with open("./task10/anketa.txt", "r", encoding="UTF-8") as f:
    question = f.readline().strip("\n")
    votes = [int(num) for num in f.readline().split()]

root = tk.Tk()
canvas = tk.Canvas(root, height=200, width=400)
canvas.pack()
while True:
# initialize position
    x = 10
    y = 10
    y_spacing = 30
    bar_x = 100


    canvas.create_text(x, y, text=question, anchor="w", font=("Arial", 12))

    options = ["1) Áno", "2) Nie", "3) Neviem"]
    max_num = max(votes)

    for idx, num in enumerate(votes):
        y = y+y_spacing
        canvas.create_text(x, y, text=f"{options[idx]} - {num}", anchor="w")
        if num == max_num:
            canvas.create_rectangle(bar_x, y+10, bar_x+num*5, y-10, fill="green")
        else:
            canvas.create_rectangle(bar_x, y+10, bar_x+num*5, y-10, fill="red")
    
    user_input = int(input("enter your vote: "))
    if user_input  <= 3:
        votes[user_input-1] += 1
        canvas.delete("all")
        rewrite_context = f"{question}\n{votes[0]} {votes[1]} {votes[2]}"
        with open("./task10/anketa.txt", "w", encoding="UTF-8") as f:
            f.write(rewrite_context)
        continue
    else:
        break  

root.mainloop()