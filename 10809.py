ab="a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z"
alphabet = list(map(str,ab.split(',')))

S = input()
result=""
for _ in alphabet :
    if S.count(_) <1:
        result += str(-1)
        result += " "
    else:
        result += str(S.index(_))
        result += " "
print(result)
