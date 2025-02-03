import random

player_input = []
while len(player_input) != 6:
    player_input = input("enter 6 numbers (1-49): ").split()

lottery_num = ['6', '29', '39', '13', '43', '16']
while len(lottery_num) != 6:
    num = str(random.randint(1,49))
    if num not in lottery_num:
        lottery_num.append(num)

match_num = []
right = 0
for num in player_input:
    if num in lottery_num:
        match_num.append(num)
        right += 1
print(f"you guessed {right} correctly: {match_num}")


cache = []
file = open("./task5/loteria_1.txt", "r")
guesses = file.read().split("\n")
for player_set in guesses:
    count = 0
    for num in player_set.split():
        if num in lottery_num:
            count += 1
    cache.append(count)
    
for i in range(1, 7):
    print(f"player have {i} right: {cache.count(i)}")
