import sys
from collections import deque


def bfs(my_list,dr,dc,n,lv,rv, stack) :

    #변수 선언
    que = deque()

    v = [[9876543210 for _ in range(n)] for _ in range(n)]


    if lv <= my_list[dr][dc] <= rv :
        que.append((dr, dc, 0))
        v[dr][dc] = 0


    while que :
        r,c, cnt = que.popleft()
        next_cnt = cnt + 1


        for rr,cc in tra_list :
            next_r = r + rr
            next_c = c + cc

            if -1< next_r < n and -1 < next_c< n :
                if  lv <= my_list[next_r][next_c] <= rv:
                    if v[next_r][next_c] > next_cnt :
                        v[next_r][next_c] = next_cnt
                        que.append((next_r, next_c, next_cnt))

    for r,c in stack :
        if v[r][c] == 9876543210 :
            return False

    return True



tra_list = [[1,0],[0,1],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

def find_start(a,n) :
    for i in range(n) :
        for j in range(n) :
            if a[i][j] == 'P' :
                return (i,j)

def find_k(a,n) :
    stack = []
    for i in range(n) :
        for j in range(n) :
            if a[i][j] == 'K' :
                stack.append((i,j))
    return stack




n = int(sys.stdin.readline().rstrip())
a = []
for _ in range(n) :
    a.append(str(sys.stdin.readline().rstrip()))

des = find_start(a,n)
k_posi = find_k(a,n)



my_list = []
num_list = []
for _ in range(n) :
    temp = list(map(int,sys.stdin.readline().split()))
    my_list.append(temp)
    for c in temp :
        num_list.append(c)

num_list = sorted(num_list)

lidx,ridx = 0,0
answer = 9876543210

while lidx <= len(num_list) - 1 and ridx <= len(num_list) - 1  :

    lv = num_list[lidx]
    rv = num_list[ridx]

    if ridx == len(num_list) - 1 :
        ff =  bfs(my_list,des[0],des[1],n, lv, rv, k_posi)

        if ff == True :
            lidx +=1
            answer = min(answer, rv - lv)
        else :
            break


    else :
        ff =  bfs(my_list,des[0],des[1],n, lv , rv , k_posi)

        if ff == True :
            lidx +=1
            answer = min(answer, rv-lv)
        else :
            ridx += 1

print(answer)
