import random


with open("./task11/obesenec.txt") as file:
    obesenec_lst = file.read().split("\n")


guess = random.choice(obesenec_lst)
player = [".",]*len(guess)
chance = 0
print(guess)

while "." in player:
    player_input = input("enter a letter: ")
    if player_input in guess:
        for idx, letter in enumerate(guess):
            if letter == player_input:
                player[idx] = player_input
        for letter in player:
            print(letter, end="")
        print()
    if chance == 10:
        print("you lose")
        break 
    chance += 1

else:
    print("you win")