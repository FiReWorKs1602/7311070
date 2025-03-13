import time

with open("./task20/knihy.txt", "r")as file:
    books = []
    dates = []
    for idx, data in enumerate(file.readlines()):
        if idx%2 == 0: # first line
            books.append(data.strip())
        else:          # second line
            dates.append(data.strip())


for idx, temp in enumerate(dates):
    notification = temp.split()
    if len(notification)%2!=0:
        print(books[idx])

max_length = max(len(line.split()) for line in dates)
longest_lines = "\n".join([books[idx] for idx,line in enumerate(dates) if len(line.split()) == max_length])
print()
print(longest_lines)

# date time
from datetime import datetime

# Vstupné dáta
data = [
    "1001 2901 1502 2502 0503 1503",
    "1501 2802 1003 2803 1505",
    "1402 1802 1004 2104 1205 3105",
    "1604 2504 0105 1305",
    "0803 2704 0405"
]

# Funkcia na výpočet počtu dní medzi dvoma dátumami
def calculate_days(date1, date2):
    date_format = "%d%m"
    d1 = datetime.strptime(date1, date_format)
    d2 = datetime.strptime(date2, date_format)
    return (d2 - d1).days

# Pre každú knihu vypočítame celkovú dobu vypožičania
today = "1506"
books_with_duration = []
for idx,book in enumerate(dates):
    dates = book.split()
    total_days = 0
    for i in range(0, len(dates), 2):
        if i + 1 < len(dates):  # Zabezpečíme, že máme pár dátumov
            total_days += calculate_days(dates[i], dates[i + 1])
        else:
            total_days += calculate_days(dates[i], today)
    books_with_duration.append((books[idx], total_days))

# Zoradenie kníh podľa celkovej doby vypožičania (od najkratšej po najdlhšiu)
sorted_books = sorted(books_with_duration, key=lambda x: x[1])

# Výpis zoradených kníh
for book, duration in sorted_books:
    print(f"{book} (Celková doba vypožičania: {duration} dní)")