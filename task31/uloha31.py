
import random

with open("./task31/poprehadzovany_text1_vstup.txt", "r",encoding="utf-8") as f:
    data = " ".join(f.readlines()).replace("\n", "").split()

result = " "
for idx, word in enumerate(data):
    if len(word) > 3:
        middle = list(word[1:-1])
        random.shuffle(middle)
        shuffle = "".join(middle)
        data[idx] = word[0] + shuffle + word[-1]

with open("./task31/text.txt", "w") as f:
    f.write(" ".join(data))