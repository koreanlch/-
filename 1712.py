a , b , c = map(int,input().split())

if c>b:
    laptops = a//(c-b) + 1
    
    print(str(laptops))

else :
    print('-1')
