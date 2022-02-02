import sys
N = int(sys.stdin.readline())
std = list(map(int,sys.stdin.readline().split()))
std.sort()
sum=[]
for i in range(N):
    team = std[i] + std[2*N-1-i]
    sum.append(team)
print(min(sum))
