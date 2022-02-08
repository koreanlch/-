T = int(input())

for i in range(T):
    PS = input()
    VPS = 0
    if len(PS)%2 != 0 :
        VPS += 1
    elif PS.startswith(")"):
        VPS += 1
    elif PS.endswith("("):
        VPS += 1
    elif PS.count("(") != len(PS)/2:
        VPS += 1 
    if VPS == 0:
        num = 0
        for i in PS :
            if i == "(":
                num += 1
            else:
                num -= 1
            if num < 0 :
                VPS += 1
                break
    if VPS == 0 :
        print("YES")
    else:
        print("NO")
