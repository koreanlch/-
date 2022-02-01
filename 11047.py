N, K =map(int, input().split())
coins = []
for i in range(N):
    value= int(input())
    coins.append(value)
    
for j in coins :
    if j>K:
        over = coins.index(j)
        break
coins= coins[:over]
coins.reverse()

count = 0
for k in coins:
    if K//k != 0:
        count += K//k
        K = K%k
    if K==0:
        break
print(count)
