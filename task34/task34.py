import random

rozmer = 5
mp = [[random.randint(-10,11) for _ in range(rozmer)] for _ in range(rozmer)]

count = 0
for i in mp:
    count += sum(i)
avg = round(count / rozmer**2, 4)
print(avg)

odnies =0
donies = 0
chance = 0
for line in range(rozmer):
    for idx in range(rozmer-1): 
        if mp[line][idx] > avg:
            mp[line][idx] -= mp[line][idx]-avg
            mp[line][idx+1] = mp[line][idx+1]+(mp[line][idx]-avg)
            donies += 1
        else:
            mp[line][idx] += avg - mp[line][idx]
            mp[line][idx+1] -= mp[line][idx+1]+avg - mp[line][idx]
            odnies += 1


for i in range(rozmer-1):
    if mp[i][rozmer-1] > avg:
        mp[i][rozmer-1] -= mp[i][rozmer-1]-avg
        mp[i+1][rozmer-1] = mp[i][rozmer-1]+mp[i][rozmer-1]-avg
        donies += 1
    else:
        mp[i][rozmer-1] += avg - mp[i][rozmer-1]
        mp[i+1][rozmer-1] = mp[i][rozmer-1]+avg - mp[i][rozmer-1]
        donies+=1

with open("./task34/pozemok.txt", "w") as f:
    for i in mp:
        f. write(f"{str(i)}\n")
    f.write(f"odnies - {odnies} \ndonies-{donies}\nspolu-{odnies+donies}")



