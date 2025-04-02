import random

guess = []
while len(set(guess)) != 6 or any(int(num) < 1 or int(num) > 49 for num in guess):
    guess = input("enter 6 numbers: ").split()

answer = []
while len(answer) != 6:
    num = str(random.randint(1,49))
    if num not in answer:
        answer.append(num)

print(guess)
print(answer)
print(set(guess) & set(answer))
print(len(set(guess) & set(answer)))

with open("./task5/loteria_2.txt", "r") as f:
    player = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in f.read().split("\n"):
        if len(set(i.split()) & set(answer)) != 0:
            player[len(set(i.split()) & set(answer))] = 1
print(player)

