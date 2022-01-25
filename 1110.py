a = input()
b = int(a)
c = b//10
d = b%10
e = c+d
new = int(str(d)+str(e%10)) 
times = '*'

while str(new) != a:
    b,new = new,b
    del(new,c,d,e)
    c = b//10
    d = b%10
    e = c+d
    new = int(str(d)+str(e%10))
    times += '*'

print(str(int(times.count('*'))))
