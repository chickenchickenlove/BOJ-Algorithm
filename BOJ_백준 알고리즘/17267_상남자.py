import sys
from collections import deque


def bfs(my_map,s,l,r,n,m) :
    que = deque()

    v = [[(0,0,0) for _ in range(m)] for _ in range(n)]
    sr,sc = s[0], s[1]

    que.append((sr,sc,l,r,0))
    v[sr][sc] = ((l,r,0))

    while que :
        y,x,l,r,time = que.popleft()
        next_time = time + 1

        for yy, xx in tra_list :
            next_y = y + yy
            next_x = x + xx
            if [yy,xx] == [0,1] :
                nl,nr = l, r-1
            elif [yy,xx] == [0,-1] :
                nl,nr = l-1, r
            else :
                nl,nr = l,r


            if -1 < next_y < n and -1 < next_x < m :
                if my_map[next_y][next_x] == '1' :
                    continue
                next_l, next_r, next_cnt =  v[next_y][next_x][0],v[next_y][next_x][1], v[next_y][next_x][2]
                if next_l <= l and next_r < r or next_l < l and next_r <= r :
                    if nl >= 0 and nr >= 0 :
                        que.append((next_y, next_x, nl, nr, next_time))
                        v[next_y][next_x] = (nl,nr,next_time)
                elif next_l == l and next_r == r :
                    if nl >= 0 and nr >= 0 :
                        if v[next_y][next_x][2] > next_time :
                            que.append((next_y, next_x, nl, nr, next_time))
                            v[next_y][next_x] = (nl, nr, next_time)

    answer = 0
    for i in range(n) :
        for j in range(m) :
            if v[i][j] != (0,0,0) :
                answer +=1

    return answer




tra_list = [[1,0],[0,1],[-1,0],[0,-1]]



n,m = map(int,sys.stdin.readline().split())
l,r = map(int,sys.stdin.readline().split())
my_map = []
for _ in range(n) :
    my_map.append(str(sys.stdin.readline().rstrip()))

for i in range(n) :
    for j in range(m) :
        if my_map[i][j] == '2':
            s = (i,j)
            break



print(bfs(my_map,s,l,r,n,m))
