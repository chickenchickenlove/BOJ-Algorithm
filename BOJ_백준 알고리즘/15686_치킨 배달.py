#15686_치킨배달
import sys
from collections import deque


#1. 시작 시, 치킨집, 집 배열을 따로 구한다.
#2. 재귀로 폐업시킬 치킨집을 고르고, 배열로 관리한다. 그리고 그 값을 0으로 해준다. 중복은 안되니, 잘 조합해야함.
#3. 재귀 마지막에 갔을 때, 그 값을 바탕으로 각 집을 BFS 돌려서 값을 구해서 저장한다.


def sol(depth, now_level, now_posi):
    global answer
    if depth == now_level :
        temp = 0
        for rr,cc in h :
            ttemp = 9876543210
            for idx, value in enumerate(c) :
                if vvv[idx] == 0 :
                    rrr,ccc = value
                    ttemp = min(ttemp,  abs(rrr-rr) + abs(ccc-cc))
            temp += ttemp
        answer = min(answer, temp)
    else :
        for idx in range(now_posi, len(c)) :
            vvv[idx] = 1
            sol(depth, now_level +1, idx + 1)
            vvv[idx] = 0


def bfs(sr,sc) :
    global n
    que = deque()
    que.append((sr,sc,0))
    v = [[0 for _ in range(n)] for _ in range(n)]
    v[sr][sc] = 1

    while que :
        rrr, ccc, cnt = que.popleft()
        if my_list[rrr][ccc] == 2 :
            return cnt
        for rr,cc in tra_list :
            next_r,next_c = rrr + rr, ccc + cc
            if -1 < next_r < n and -1 < next_c < n :
                if v[next_r][next_c] == 0 :
                    v[next_r][next_c] = 1
                    que.append((next_r,next_c,cnt+1))



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]




answer = 9876543210

n,m = map(int,sys.stdin.readline().split())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
c, h = [],[]
for i in range(n) :
    for j in range(n) :
        if my_list[i][j] == 1 :
            h.append((i,j))
        elif my_list[i][j] == 2  :
            c.append((i,j))

vvv = [0 for _ in range(len(c))]

sol(len(c)-m, 0, 0 )
print(answer)