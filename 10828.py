number =[]
N = int(input())

def a(x):
    number.append(x)

for i in range(N):
    command = input()
    if command.startswith("push"):
        pu = list(command.split())
        pu.remove("push")
        
        x = int(pu[0])
        a(x)
    elif command == "pop":
        if len(number) ==0:
            print("-1")
        else:
            print(number.pop())
    elif command == "size":
        print(len(number))
    elif command == "empty":
        if len(number)==0:
            print("1")
        else:
            print("0")
    elif command == "top":
        if len(number)==0:
            print("-1")
        else:
            print(number[len(number)-1])
