a,b,v=map(int,input().split())

remain = v-a
day = a-b
time = remain//day
if remain%day == 0:
    print(str(time+1))
else:
    print(str(time+2))
