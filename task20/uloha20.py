from datetime import datetime

with open("./task20/knihy.txt", "r") as f:
    data = f.readlines()
    books = [line.strip() for pos ,line in enumerate(data) if pos % 2 == 0]
    dates = [line.strip().split() for pos ,line in enumerate(data) if pos % 2 != 0]
    

def date_calculator(date1, date2):
    date1 = datetime.strptime(date1, "%d%m")
    date2 = datetime.strptime(date2, "%d%m")
    delta = date2 - date1
    return delta.days

# uloha a + c
today = "1508" 
result  = []
for pos, line in enumerate(dates):
    if len(line) % 2 != 0: 
        if date_calculator(line[-1], today) > 30: 
            print(f"{books[pos]}")
        result.append([date_calculator(line[-1], today), books[pos]]) 
    else: 
        result.append([date_calculator(line[-2], line[-1]), books[pos]])

print(result)
result.sort()
print(result)

# uloha b
most_borrowed = 0
for line in dates:
    count = 0
    for date in range(0, len(line), 2): 
        count += 1 
    if count > most_borrowed:
        most_borrowed = count

for pos ,line in enumerate(dates):
    count = 0
    for date in range(0, len(line), 2):
        count += 1 
    if count == most_borrowed: 
        print(f"{books[pos]}-most borrowed")