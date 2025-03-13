with open("./task19/pretekari.txt", "r") as file:
    participants = [i.strip("\n").split() for i in file.readlines()]

with open("./task19/stanovista.txt", "r") as file:
    stanovista = file.read().split("\n")

def checker(participant, stanovista):
    
    pass_all = True
    for i in stanovista:
        if i not in participant: 
            pass_all = False
        
    print(f"participant-{participant[0]} pass: {pass_all}")
    return pass_all
    
verified = []
not_qualified = []
for i in participants:
    if checker(i, stanovista) :
        verified.append(i)
    else:
         not_qualified.append(i) 

rank = []
for participant in verified:
    rank.append(int(participant[1][:2])*60 + int(participant[1][3:]))


rank.sort()
place = 1
for i in rank:
    for participant in verified:
        if int(participant[1][:2])*60 + int(participant[1][3:]) == i:
            print(f"{place}-{participant[0]}")
    place+=1
for participant in not_qualified:
    print(f"{place}-{participant[0]}")
    place+=1