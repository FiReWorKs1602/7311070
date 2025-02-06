file = open("./task6/spokojnost_1.txt", "r", encoding="utf-8")
data = file.read()

print(data.count("nie"))

time_respose_nie = [0,]*24 
for line in data.split("\n"):
    if "nie" in line:
        time = line[:2]
        time_respose_nie[int(time)] += 1
print(f"o {time_respose_nie.index(max(time_respose_nie))}:00 :{max(time_respose_nie)} ludi")

for time, ludi in enumerate(time_respose_nie):
    if ludi != 0:
        print(f"{str(time).zfill(2)}:00 - {ludi} ludi")
        
import tkinter as tk
cv = tk.Canvas(width=400, height=300, bg="white")
cv.pack()

# Scale factors for visualization
bar_width = 13
x_spacing = 16.5
y_base = 270
y_scale = 15

# Draw the bars
for hour, total_count in enumerate(time_respose_nie):
    x_start = 5 + x_spacing * int(hour)
    x_end = x_start + bar_width
    if total_count:
        y_end = y_base - time_respose_nie[hour] * y_scale
        cv.create_rectangle(x_start, y_base, x_end, y_end, fill="red")
    else:
        cv.create_rectangle(x_start, y_base, x_end, y_base, fill="gray")
    
    # Add hour labels below the bars
    cv.create_text(x_start + bar_width // 2, y_base + 10, text=str(hour).zfill(2), font=("Arial", 8))

cv.mainloop()