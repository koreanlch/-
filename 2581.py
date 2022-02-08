M = int(input())
N = int(input())
sosu = []
for i in range(M, N+1):
    T = 0
    if i ==1:
        T += 1
    else:
        for j in range(2,i):
            if i%j == 0:
                T += 1
                break
    if T == 0:
        sosu.append(i)
if sosu == []:
    print("-1")
else:
    print(sum(sosu))
    print(min(sosu))
