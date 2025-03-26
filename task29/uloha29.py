

table = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
user = "AKO SA MAS"

result = ""
for letter in user:
    if letter == " ":
        result += "0 "
    elif table.index(letter)%3 == 1:
        result += str((table.index(letter)//3+1)) + " "
    elif table.index(letter)%3 == 2:
        result += str((table.index(letter)//3+1))*2+ " "
    elif table.index(letter)%3 == 0:
        result += str((table.index(letter)//3))*3+" "

print(result)

count = 0
for num in range(9):
    if result.count(str(num)) > count:
        count = result.count(str(num))

max_len = []
for num in range(9):
    if result.count(str(num)) == count:
        max_len.append(num)

print(max_len)

