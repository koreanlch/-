T = int(input())
for i in range(T):
   N = int(input())
   schools =""
   quantities = []
   for j in range(N):
      S,L =input().split()
      schools += S
      schools += ','
      Sl = schools.split(',')
      quantities.append(int(L))
      schools
   N1 = max(quantities)
   order = quantities.index(N1)
   print (Sl[order])
