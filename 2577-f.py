a , b , c= input(), input(), input()
mul = str(int(a)*int(b)*int(c))

result = ''
for i in range(9):
    for j in range(10):
        result += mul.count(str(j))
    result += '\n'

print(result)
