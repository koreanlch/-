C = int(input())
for i in range(C):
    j =list(map(int,input().split()))
    j.remove(j[0])
    average = sum(j)/len(j)
    def over(n):
        if n > average:
            return 0
        else:
            return 1
    better = list(map(over,j))
    ratio = better.count(0)/len(j)
    answer = str(round(ratio*100,3))
    if len(answer) == 4:
        answer += "00"
    elif len(answer) ==5:
        answer +='0'
    result = answer + '%'
    print(result)
