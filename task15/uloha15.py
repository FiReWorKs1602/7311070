

with open("./task15/jedla.txt", 'r') as file:
    context = file.read()
    schedule = context.split("\n")

print("pocet jedla na nasledujuci den: ", len(schedule))


print("zelena: ", context.count("z"))
print("cervena: ",context.count("c"))
print("modra: ", context.count("m"))
print("hneda: ", context.count("h"))

min_people = ""
jedlo = "zchm"
for i in jedlo:
    if context.count(i) < 20:
        print(i, context.count(i))
        min_people = i

code = []
for day, line in enumerate(schedule):
    
    if min_people in line:
        people = int(line.split()[0])
        code.append(people)

print( code, " studenti zobrali m")