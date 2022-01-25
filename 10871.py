n,x = map(int, input().split())

a = list(map(int,input().split()))
answer = ''
for i in a:
    if int(i) < x:
        answer += str(i)
        answer += " "
print(answer)
