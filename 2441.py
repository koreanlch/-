r = int(input())

body = ''
for i in range(r):
    body +=" "*i
    body +="*"*(r-i)
    body +="\n"

print(body)
