numbers=""
for i in range(9):
   a=input()
   numbers += a
   numbers += " "
N=list(map(int,numbers.split()))
print(max(N))
print(N.index(max(N))+1)
