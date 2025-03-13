import random


def checker(random_code):
    bit1 = (int(random_code[0])+int(random_code[1])+int(random_code[2])+int(random_code[3]))%2
    bit2 = (int(random_code[2])+int(random_code[3])+int(random_code[4])+int(random_code[5]))%2
    bit3 = (int(random_code[4])+int(random_code[5])+int(random_code[6])+int(random_code[7]))%2

    num = (2*bit1) + (2*bit2)**1 + (2*bit3)**2
    if random_code[-1] != str(num):
        print(random_code)

    return num 

random_code = str(random.randint(10000000, 99999999))
random_code += str(checker(random_code))

with open("./task18/kod_a.txt","r") as file:
    for i in file.readlines():
        checker(i.strip('\n'))