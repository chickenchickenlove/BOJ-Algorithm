import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))


a_nega = []
a_posi = []
for i in a :
    if i < 0 :
        a_nega.append(abs(i))
    else :
        a_posi.append(i)


b_nega = []
b_posi = []
for i in b :
    if i < 0 :
        b_nega.append(abs(i))
    else :
        b_posi.append(i)

a_nega = sorted(a_nega)
a_posi = sorted(a_posi)
b_nega = sorted(b_nega)
b_posi = sorted(b_posi)


s = 0
answer = 0

if a_nega and b_posi :

    for num in a_nega :
        if s >= len(b_posi) :
            break
        if s < len(b_posi) :
            if num > b_posi[s] :
                answer +=1
                s +=1

s = 0

if b_nega and a_posi :
    for num in b_nega :
        if s >= len(a_posi) :
            break
        if s < len(a_posi) :
            if num > a_posi[s] :
                answer +=1
                s +=1


print(answer)