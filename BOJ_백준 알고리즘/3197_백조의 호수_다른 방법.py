import sys
from collections import deque
import time

def break_ice(n,m, water,vv):
    global ss1, ss2, rrrrr

    que = deque()
    while water :
        a,b = water.pop()
        que.append((a,b,0))
        vv[a][b] = 0


    while que :
        r,c, day = que.popleft()
        next_day = day + 1

        for rr,cc in tra_list :
            next_r, next_c = r + rr, c + cc

            #경계 만족할 때
            if -1 < next_r < n and -1 < next_c < m:

                # 얼음인 경우에만 집어넣는다.
                if my_list[next_r][next_c] == "X" and vv[next_r][next_c] > next_day:
                    vv[next_r][next_c] = next_day
                    que.append((next_r, next_c, next_day))
                    rrrrr = max(rrrrr, next_day)

    return



def bfs(sr,sc, er, ec, n,m,day):

    que = deque()

    v = [[0 for _ in range(m)] for _ in range(n)]
    que.append((sr,sc))
    v[sr][sc] = 1


    while que :
        r,c = que.popleft()

        if r == er and c == ec:
            return True

        for rr,cc in tra_list :
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < m:
                if vv[next_r][next_c] <= day and v[next_r][next_c] == 0 :
                    que.append((next_r, next_c))
                    v[next_r][next_c] = day

    return False



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]



water = []
bird = set()
r,c = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(r)]
for i in range(r) :
    temp = sys.stdin.readline().rstrip()
    for k in temp :
        my_list[i].append(k)
        if k == "." :
            water.append((i,len(my_list[i])-1))
        if k == "L" :
            bird.add((i, len(my_list[i]) - 1))
            water.append((i, len(my_list[i]) - 1))




ans = 1
er,ec = bird.pop()
sr,sc = bird.pop()
v = [[0 for _ in range(c)] for _ in range(r)]
vv = [[5000 for _ in range(c)] for _ in range(r)]


qqq = time.time()

rrrrr = 0
break_ice(r,c,water,vv)
ll = 0

ans = 9876543210
rrrrr += 1
while ll < rrrrr :


    m = (ll+rrrrr) // 2
    if bfs(sr,sc,er,ec,r,c,m) :
        rrrrr = m
        ans = min(ans, m)
    else :
        ll = m + 1

print(ans)

