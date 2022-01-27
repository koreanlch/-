T= int(input())
for i in range (T):
   Y = 0
   K = 0
   for j in range(9):
      y,k=map(int,input().split())
      Y += y
      K += k
   if K > Y:
      print("Korea")
   elif Y == K:
      print("Draw")
   else : 
      print("Yonsei")
