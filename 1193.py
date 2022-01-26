X=int(input())
a = 1
if X ==1:
    print('1/1')
else:
    while a*(a+1)/2 < X:
        a += 1
    b = a*(a+1)/2
    c = a*(a-1)/2
    if a%2 == 0:
        result = str(int(X-c)) + '/' + str(int(1+b-X))
    elif a%2 ==1:
        result = str(int(1+b-X)) + '/' + str(int(X-c))

    print (result)
