import sys
from collections import deque

def bfs(my_list,n,m,v,cnt,q,w) :
    que = deque()
    que.append((q,w,0))
    v[cnt][q][w] = 0


    while que :
        r,c,wall = que.popleft()

        for rr,cc in tra_list :
            next_r = r + rr
            next_c = c + cc

            if -1 < next_r < n and -1 < next_c < m :
                if my_list[next_r][next_c] == '.' or my_list[next_r][next_c] == '$':
                    if v[cnt][next_r][next_c] > wall :
                        que.appendleft((next_r, next_c, wall))
                        v[cnt][next_r][next_c] = wall

                elif my_list[next_r][next_c] == '#' :
                    if v[cnt][next_r][next_c] > wall + 1 :
                        que.append((next_r, next_c, wall + 1 ))
                        v[cnt][next_r][next_c] = wall + 1


tra_list = [[1,0],[0,1],[-1,0],[0,-1]]


t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    n,m = map(int,sys.stdin.readline().split())
    my_list = [[] for _ in range(n+2)]
    start = [(0,0)]
    for i in range(len(my_list)):
        if i == 0 or i == len(my_list) - 1 :
            for _ in range(m+2) :
                my_list[i].append('.')
        else :
            my_list[i].append('.')
            temp = str(sys.stdin.readline().rstrip())
            for c in temp:

                my_list[i].append(c)
                if c == '$' :
                    start.append((i, len(my_list[i])-1))
            my_list[i].append('.')

    n +=2
    m +=2


    v = [[[9876543210 for _ in range(m)] for _ in range(n)] for _ in range(4)]


    cnt = 0
    while start :
        q,w = start.pop()
        bfs(my_list,n,m,v,cnt,q,w)
        cnt +=1

    answer = 9876543210
    for i in range(n) :
        for j in range(m) :
            temp = 0
            if my_list[i][j] == '*' :
                continue

            for k in range(3) :
                temp += v[k][i][j]

            if my_list[i][j] == '#' :
                temp -=2

            answer = min(answer , temp)

    if answer <= 0 :
        print(0)
    else :
        print(answer)
