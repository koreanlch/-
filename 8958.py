T=int(input())
for i in range(T):
   A=input().split("X")
   
   for j in A:
      if j =="":
         A.remove(j)
   score = 0
   for k in A:
      S=len(k)
      plus=int((S*S+S)/2)
      score += plus
   print(score)
