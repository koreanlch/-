N = int(input())

row = []
numbers = []
for i in range(N):
    line = list(map(int,input().split()))
    for k in line :
        numbers.append(k)
    row.append(line)

TF = 0
for k in range(N):
    plus= 0
    for j in range(N):
        plus +=row[k][j]
    if plus != N*(N**2+1)/2:
        TF += 1
        break

if TF == 0:
    for m in range(N):
        sum = 0
        for n in range(N):
            sum += row[n][m]
        if sum != N*(N**2+1)/2:
            TF += 1
            break

if TF == 0:
    total= 0
    for l in range(N):
        total += row[l][l]
    if total != N*(N**2+1)/2:
        TF +=1

if TF == 0:
    king = 0
    for _ in range(N):
        king += row[_][N-_-1]
    if king != N*(N**2+1)/2:
        TF +=1
if TF== 0:
    count = 0
    for i in range(N):
        for j in range(N):
            count += numbers.count(row[i][k])
    if count != N**2:
        TF+=1
            
if TF == 0:
    print("TRUE")
else:
    print("FALSE")
