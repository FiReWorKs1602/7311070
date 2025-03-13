with open("./task23/elektricky.txt", "r") as f:
    trams = f.readlines()

print("there are ",len(trams),"trams")

for idx, tram in enumerate(trams):
    if tram[0][0] != trams[0][-2]:
        print(f"the {idx} tram doesn't end with starting station")
    
for idx, tram in enumerate(trams):
    if tram.strip().split()[::-1] != tram.strip().split():
        print(f"the {idx} tram doesn't return with same path: {tram.strip()}")
    