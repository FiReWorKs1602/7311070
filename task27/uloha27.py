

with open("./task27/cesty.txt", "r") as f:
    data = [line.split() for line in f.read().split("\n")]
print(data)


count = 0
for line in range(1, len(data)):
    for column in range(0,line):
        count += int(data[line][column])
print(count)

max_len=[0,0]
for line in range(1, len(data)):
    for column in range(line):
        if  int(data[line][column]) > int(data[max_len[0]][max_len[1]]):
            max_len = [line, column]
        elif data[line][column] == data[max_len[0]][max_len[1]]:
            max_len.append(line)
            max_len.append(column)

for i in range(0,len(max_len),2):
    print(f"{max_len[i]+1} - {max_len[i+1]+1}")