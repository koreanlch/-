a , b , c= int(input()),int(input()),int(input())
mul = str(a*b*c)

result = ''
for j in range(10):
    k=str(j)
    result += str(mul.count(k))
    result += '\n'

print(result)
