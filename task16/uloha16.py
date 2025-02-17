
letter = {}
with open("./task16/frekv.txt") as file:
    for i in file.readlines():
        symbol,frec = i[0], i[2:].strip()
        letter[frec] = symbol
print(letter)

with open("./task16/sifro.txt", "r")as file:
    context = file.read()

result = ""
for i in context:
    if i =="\n":
        result+="\n"
    else:
        ctx_frec = str(context.count(i))
        result+=letter[ctx_frec]
print(result)