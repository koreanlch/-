import sys
import math

N = int(sys.stdin.readline())
k = round(math.log(N,3))
def shape(x): 
    if x==1:
        star = ["*"*3,"* *","*"*3]
        return star
    else:
        star = [i*3 for i in shape(x-1)] + [i +" "*(3**(x-1))+i for i in shape(x-1)]+ [i*3 for i in shape(x-1)]
        return star
    
    
for j in shape(k):
    print(j)
