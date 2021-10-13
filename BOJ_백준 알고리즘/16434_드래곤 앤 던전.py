import sys
import math


def sol(first_life,first_atk, my_list,n) :
    life = first_life
    atk = first_atk
    for i in range(n) :
        a,b,c = my_list[i]
        if a == 1 :
            #b 몬스터 공격력, c는 생명력력
            q = math.ceil(c/atk)
            if atk*q >= c and b*(q-1) < life :
                life -= b*(q-1)
            else : return False
        else :
            atk += b
            life += c
            if life >= first_life :
                life = first_life

    return True


n, hatk = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
for i in range(n) :
    a,b,c = map(int,sys.stdin.readline().split())
    my_list[i] = (a,b,c)


l = 0
r = 999999999999999999
answer = r
while l <= r :
    mid = (l+r) // 2
    if sol(mid,hatk,my_list,n) :
        r = mid- 1
        answer = min(answer,mid)
    else :
        l = mid +1

print(answer)
