import sys
from builtins import map
from collections import deque


#tra_list = ((1,0,0),(0,1,1),(-1,0,2),(0,-1,3))

def find_answer(next_r, next_c, dd, my_map):
    global a,b,n,m
    nn_r, nn_c = next_r + a - 1, next_c + b-1
    if nn_r < 0 or nn_r > n-1 or nn_c < 0 or nn_c > m-1 :
        return False

    if dd == 2 :
        for ccc in range(next_c, nn_c + 1 ) :
            if -1 < ccc < m :
                if my_map[next_r][ccc] == 1 :
                    return False
            else :
                return False
    if dd == 0 :
        for ccc in range(next_c, nn_c + 1 ) :
            if -1 < ccc < m :
                if my_map[nn_r][ccc] == 1 :
                    return False
            else :
                return False

    elif dd == 1 :
        for rrr in range(next_r, nn_r + 1 ) :
            if - 1 < rrr < n :
                if my_map[rrr][nn_c] == 1 :
                    return False
            else : return False

    elif dd == 3:
        for rrr in range(next_r, nn_r + 1 ) :
            if - 1 < rrr < n :
                if my_map[rrr][next_c] == 1 :
                    return False
            else : return False


    return True




def bfs(n,m,sr,sc, er,ec) :
    global a,b

    que = deque()
    v = [[9876543210 for _ in range(m)] for _ in range(n)]

    que.append((sr,sc,0))
    v[sr][sc] = 0

    while que :
        now_r, now_c, now_cnt = que.popleft()
        if now_r == er and now_c == ec :
           # for qqqq in range(n) :
           #     print(v[qqqq])
            return now_cnt


        for rr,cc,dd in tra_list :
            next_r, next_c = now_r + rr, now_c + cc
            if -1 < next_r < n and -1 < next_c < m :

                if find_answer(next_r, next_c, dd, my_map) :
                    if v[next_r][next_c] > now_cnt + 1  :
                        que.append((next_r, next_c, now_cnt + 1 ))
                        v[next_r][next_c] = now_cnt+1
    return -1

tra_list = ((1,0,0),(0,1,1),(-1,0,2),(0,-1,3))


n,m,a,b,k = map(int,sys.stdin.readline().split())
my_map = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k) :
    q,w = map(int,sys.stdin.readline().split())
    my_map[q-1][w-1] = 1


sr,sc = map(int,sys.stdin.readline().split())
er,ec = map(int,sys.stdin.readline().split())
sr,sc,er,ec= sr-1, sc-1, er-1, ec-1



print(bfs(n,m,sr,sc, er,ec))





