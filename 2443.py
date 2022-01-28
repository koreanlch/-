N = int(input())

body =""
for i in range(N):
    body +=" "*i
    body +="*"*(2*(N-i)-1)
    body +="\n"

print(body)
