N=int(input())
scores=list(map(int,input().split()))
M=max(scores)
total=0
for i in scores:
   k = i/M*100
   total += k
print(total/N)
