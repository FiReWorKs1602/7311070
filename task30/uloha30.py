import random
user = "Prave som uspesne zmaturoval."

ratio = round(len(user)**0.5)
if len(user)%ratio != 0:
    user =  user+" "*(ratio-len(user)%ratio)

table = [list(user[line:line+ratio]) for line in range(0,len(user), ratio)]

def print_table(table):
    for line in table:
        for letter in line:
            print(letter, end=" ")
        print()

def shift(table):
    num = 1
    for line in range(len(table)):
        for idx in range(len(table[line])):
            table[line][num], table[line][idx] = table[line][idx], table[line][num]
            
    
print_table(table)
shift(table)
print("-------------------------")
print_table(table)