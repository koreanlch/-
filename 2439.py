r = int(input())

body = ''
for i in range(r):
    for j in range(r-i-1):
    	body += " "
    for k in range(i+1):
    	body +='*'
    body += '\n'

print(body)
