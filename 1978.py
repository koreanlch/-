import sys
T = int(input())
count = T
numbers = list(map(int,sys.stdin.readline().split()))
for i in numbers:
   if i ==1:
      count -= 1
   elif i >2:
      for j in range(2,i):
         if i%j == 0:
            count -= 1
            break
print(count)
