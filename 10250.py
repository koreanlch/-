T=int(input())

for i in range(T):
    H , W , N = map(int,input().split())
    yy = N%H
    if yy == 0:
        YY = str(H)
    else:
        YY = str(yy)
    xx = N//H + 1
    if yy == 0:
        xx = N//H
    if len(str(xx)) == 1:
        XX="0"+str(xx)
    else:
        XX=str(xx)
    print(str(YY)+XX)
