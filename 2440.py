r = int(input())

body = ''
for i in range(r):
    for j in range(r-i):
    	body += "*"
    body += '\n'

print(body)
