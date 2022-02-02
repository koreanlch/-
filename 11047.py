N, K =map(int, input().split())
coins = []
for i in range(N):
    value= int(input())
    coins.append(value)

coins.reverse()

count = 0
for k in coins:
    if K//k != 0:
        count += K//k
        K = K%k
    if K==0:
        break
print(count)
