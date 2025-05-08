
seed = "0123456789ABCDEFGH"
def check_base(num):
    mx_num = 0
    for digit in num: 
        if seed.index(digit)+1 > mx_num:
            mx_num = seed.index(digit)+1
    return mx_num

def converter(num, base):
    count = 0
    for idx,  digit in enumerate(num[::-1]): 
        count += seed.index(digit)*(base**idx)
    return count

with open("./task40/test_cody.txt", "r") as f:
    text = f.read().strip()
    data = []
    for i in range(0, len(text), 8):
        data.append(text[i:i+8])

bases = check_base(text)

for num in data:
    print(chr(converter(num, bases)), end="")

