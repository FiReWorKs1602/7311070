import random
with open("./task14/virus.txt", "r", encoding="utf-8") as file:
    context = [i.strip("\n").split() for i in file.readlines()]

# create list_line

# change order of ech line
for line in range(len(context)):
    # reverse
    z = random.randint(0, len(context[line])-1)
    context[line][z] = context[line][z][::-1]
    
    # change text order
    x = random.randint(0,len(context[line])-1)
    y = random.randint(0,len(context[line])-1)
    context[line][x],context[line][y] = context[line][y],context[line][x]
    
    #change order
    random_line = random.randint(0,len(context)-1)
    context[random_line], context[line] = context[line],context[random_line]
    
print(context)
