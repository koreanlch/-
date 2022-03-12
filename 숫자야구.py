import random
print("숫자야구 게임 연습 프로그램입니다")
print("0을 포함하시겠습니까? (Y/N)")
zero = input()
while True :
    if zero =="Y" or zero =="N" :
        break
    print('"Y" 또는 "N"으로 답해주세요')
    zero = input()
num = [0,1,2,3,4,5,6,7,8,9]
if zero == "N" :
    num.remove(0)
    c = [1,2,3,4,5,6,7,8,9]
else:
    c = [0,1,2,3,4,5,6,7,8,9]
print("몇 자리 숫자로 진행하시겠습니까? (3~4)")
leng = input()
while True :
    if leng == "3" or leng == "4":
        break
    print('3~4자리 숫자 게임만 지원합니다')
    leng = input()
answer =[]
b = len(num)
for i in range(int(leng)):
    a = random.randint(0,b-1)
    answer.append(num[a])
    num.remove(num[a])
    b -=1
print("숫자를 정했습니다 맞춰보세요")
con = 0

while con == 0 :
    guess = input()
    same = 0
    for i in c:
        if guess.count(str(i)) > 1:
            same += 1
    if int(leng) ==len(guess) and same == 0 :    
        maybe = []
        for i in range(int(leng)):
            maybe.append(guess[i])
        
        strike = 0
        ball = 0
        for j in range(len(maybe)) :
            if int(maybe[j]) in answer :
                if int(maybe[j]) == answer[j]:
                    strike += 1
                else :
                    ball += 1
        if strike + ball ==0 :
            print("out")
        elif strike == int(leng):
            result = leng+ "S    축하합니다"
            print(result)
            print('"Enter"를 누르면 종료됩니다')
            k = input()
            con += 1
        else:
            result = str(strike) +"S"+str(ball)+"B"
            print(result)
    elif int(leng) ==len(guess) :
        print("중복되는 숫자 없이 입력해주세요")
    else:
        print(leng+"자리 수를 입력하세요")
