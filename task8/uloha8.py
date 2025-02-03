
sys_seed = "0123456789ABCDEFG"

def converter(num, sys):
    num = num[::-1]
    count = 0
    for i, cislo in enumerate(num):
        count += sys_seed.index(cislo)*(sys**i)
    print(f"({num[::-1]}){sys} = {count}")
    

num, sys= input().split()

converter(num, int(sys))