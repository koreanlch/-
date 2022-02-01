T= int(input())
for i in range(T):
    s = int(input())
    n = int(input())
    option = 0
    for k in range(n):
        q , p = map(int,input().split())
        option += q*p
    price = s + option
    print(price)
