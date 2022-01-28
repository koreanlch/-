N = int(input())

body =""
for i in range(N):
    body +=" "*(N-i-1)
    body +="*"*(2*i+1)
    body +="\n"

print(body)
