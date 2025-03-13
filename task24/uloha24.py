with open("./task24/sms.txt") as f:
    text = f.readlines()

result = ""
for line in text:
    if len(line) == 1:
        result += line
    else:
        line = line.strip().split()
        for word in line:
            result+=word .capitalize()

print(result)

