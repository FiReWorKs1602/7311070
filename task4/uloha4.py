

with open("./task4/meteo_stanice.txt", "r") as file:
    num_train = file.read().split("\n")
    print(len(num_train))
    temp = []
    for i in num_train:
        print(i.split(" ")[3])
        if "+" in i:
            temp.append(float(i.split(" ")[3][1:].replace(",", ".")))
        else:
            temp.append(float(i.split(" ")[3].replace(",", "."))) 
    print(max(temp))
    print(num_train[temp.index(max(temp))][:4])
    print(sum(temp)/len(temp))