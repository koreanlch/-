## 어느부분에서 자료형 오류가 났는지 물어보기 ##

a , b , c= input(), input(), input()
mul = str(int(a)*int(b)*int(c))

result = ''
for i in range(9):
    for j in range(10):
        result += mul.count(str(j))
    result += '\n'

print(result)
