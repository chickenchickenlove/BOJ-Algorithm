import sys


def sol1() :
    global n,m
    stack = []
    for i in range(n) :
        for j in range(m) :
            if my_list[i][j] > 0 :
                stack.append((i,j,my_list[i][j]))

    while stack :
        r,c,mag = stack.pop()
        cnt = 0
        emag = mag //5
        for rr,cc in tra_list :
            next_r, next_c = r + rr , c + cc
            if -1 < next_r < n and -1 < next_c < m :
                if my_list[next_r][next_c] >= 0 :
                    cnt +=1
                    my_list[next_r][next_c] += emag
        my_list[r][c] -= emag * cnt

    return

def sol2(ur,uc,dr,dc) :
    global n,m
    ar,ac,br,bc = ur,uc,dr,dc
    now_value = 0
    next_value = 0
    while 1 :

        if my_list[ar][ac] != - 1 :
            next_value = my_list[ar][ac]
            my_list[ar][ac] = now_value
            now_value = next_value
        if ac + 1  == m :
            if (ar - 1) != -1 :
                ar -=1
            break

        ac +=1
    while 1 :

        if my_list[ar][ac] != - 1:
            next_value = my_list[ar][ac]
            my_list[ar][ac] = now_value
            now_value = next_value
        if ar - 1 == - 1 :
            if (ac - 1 ) != -1 :
                ac -=1
            break
        ar -=1

    while 1 :

        if my_list[ar][ac] != - 1:
            next_value = my_list[ar][ac]
            my_list[ar][ac] = now_value
            now_value = next_value
        if ac - 1 == -1 :
            if ar + 1 != ur :
                ar +=1
            break
        ac -=1

    while 1 :

        if my_list[ar][ac] != - 1:
            next_value = my_list[ar][ac]
            my_list[ar][ac] = now_value
            now_value = next_value
        if ar + 1 == ur  :
            break
        ar +=1


    now_value = 0
    next_value = 0
    while 1 :

        if my_list[br][bc] != -1 :
            next_value = my_list[br][bc]
            my_list[br][bc] = now_value
            now_value = next_value
        if bc + 1  == m :
            if br + 1 != n :
                br +=1
            break
        bc +=1

    while 1 :

        if my_list[br][bc] != -1:
            next_value = my_list[br][bc]
            my_list[br][bc] = now_value
            now_value = next_value
        if br + 1 == n :
            if bc - 1 != -1 :
                bc -=1
            break
        br += 1

    while 1 :


        if my_list[br][bc] != -1:
            next_value = my_list[br][bc]
            my_list[br][bc] = now_value
            now_value = next_value
        if bc - 1 == -1 :
            if br - 1 != dr :
                br -=1
            break
        bc -=1

    while 1 :

        if my_list[br][bc] != -1:
            next_value = my_list[br][bc]
            my_list[br][bc] = now_value
            now_value = next_value
        if br - 1 == dr:
            break
        br -= 1


    return



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]

n,m,t = map(int,sys.stdin.readline().split())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

ur,uc = -1,-1
dr,dc = -1,-1
for i in range(n) :
    for j in range(m) :
        if my_list[i][j] == -1 :
            if ur == -1 and uc == -1 : ur, uc = i,j
            else : dr,dc = i,j

for _ in range(t) :
    sol1()
    sol2(ur,uc,dr,dc)

ans = 0
for i in range(n) :
    for j in range(m) :
        if my_list[i][j] != - 1 :
            ans += my_list[i][j]
print(ans)

from importlib import import_module
fun = import_module("my_script").__dict__.get("myFunc")
fun()


