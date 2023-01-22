import sys
from collections import deque


def bfs(my_list,n,m) :
    que = deque()

    v = [[9876543210 for _ in range(m)] for _ in range(n)]
    que.append((0,0,0))
    d = [0 for _ in range(n*m)]


    while que :
        r,c,cnt = que.popleft()

        for rr,cc in tra_list :
            next_r = r + rr
            next_c = c + cc
            if -1 < next_r < n and -1 < next_c < m :
                if my_list[next_r][next_c] == 0 :
                    if v[next_r][next_c] > cnt :
                        v[next_r][next_c] = cnt
                        que.appendleft((next_r,next_c,cnt))
                        if next_r != 0 and next_r != n-1 and next_c != 0 and next_c != m-1 :
                            d[cnt] +=1
                else :
                    if v[next_r][next_c] > cnt + 1 :
                        v[next_r][next_c] = cnt + 1
                        que.append((next_r, next_c, cnt + 1 ))


    for i in range(n*m-1,-1,-1) :
        if d[i] != 0 :
            print(i, d[i])
            return






tra_list = [[1,0],[0,1],[-1,0],[0,-1]]





t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    n,m = map(int,sys.stdin.readline().split())
    n = n +2
    my_list = [[]for _ in range(n)]
    for i in range(n) :
        if i == 0 or i == n -1 :
            for _ in range(m + 2 ) :
                my_list[i].append(0)
        else :
            my_list[i].append(0)
            temp = list(map(int,sys.stdin.readline().split()))
            for c in temp :
                my_list[i].append(c)
            my_list[i].append(0)
    m = m + 2
    bfs(my_list,n,m)






