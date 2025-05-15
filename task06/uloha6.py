import tkinter as tk

# Read the file
with open("./task06/spokojnost_1.txt", "r", encoding="utf-8") as f:
    data = f.read()

# Count occurrences of "nie"
nie_count = data.count("nie")
print(f"Total 'nie' occurrences: {nie_count}")

# Initialize dictionaries to track hourly data
all_cos = {f"{str(i).zfill(2)}": 0 for i in range(24)}  # Initialize for all hours
nie_cos = {}

# Process each line in the data
for line in data.split("\n"):
    hour = line[:2]  # Extract hour
    all_cos[hour] += 1
    if "nie" in line:
        nie_cos[hour] = nie_cos.get(hour, 0) + 1

# Find the hour with the most "nie"
max_nie_hour = max(nie_cos, key=nie_cos.get)
print(f"Hour with most 'nie': {max_nie_hour} ({nie_cos[max_nie_hour]} occurrences)")
print("Hourly 'nie' occurrences:", nie_cos)

# Create a visualization with Tkinter
root = tk.Tk()
cv = tk.Canvas(root, width=400, height=300, bg="white")
cv.pack()

bar_width = 13
x_spacing = 16.5
y_base = 270
y_scale = 15

# Draw the bars
for hour, total_count in all_cos.items():
    x_start = 5 + x_spacing * int(hour)
    x_end = x_start + bar_width
    if hour in nie_cos:
        y_end = y_base - nie_cos[hour] * y_scale
        cv.create_rectangle(x_start, y_base, x_end, y_end, fill="red")
    else:
        cv.create_rectangle(x_start, y_base, x_end, y_base, fill="gray")
    
    # Add hour labels below the bars
    cv.create_text(x_start + bar_width // 2, y_base + 10, text=hour, font=("Arial", 8))


root.mainloop()
