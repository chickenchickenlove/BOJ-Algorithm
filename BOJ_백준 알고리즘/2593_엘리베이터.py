import sys
from collections import defaultdict
from collections import deque


# BFS 시 방문햇던 층은 가지 않도록 방문 배열 관리 필요.
# 현재 층에 오는 엘리베이터 확인 후, 해당 엘리베이터에서 갈 수 있는 층으로 BFS 하면 될 듯


def bfs(e,f,start,end,n,m) :
    que = deque()


    v = [0 for _ in range(n+1)]
    ee = [0 for _ in range(m+1)]
    que.append((start,0,''))
    v[start] = 1




    while que :
        now_node, now_cnt, path = que.popleft()
        next_cnt = now_cnt + 1

        if now_node == end :
            print(now_cnt)
            return path


        for elev in f[now_node] :
            if ee[elev] == 0 :
                a,b = e[elev]
                while a <= n :
                    if v[a] == 0 :
                        que.append((a, next_cnt, path + str(elev) + ','))
                        v[a] = 1
                    a+=b
                ee[elev] = 1


            ee[elev] = 1

    return ''



n,m = map(int,sys.stdin.readline().split())

my_dict = defaultdict(dict)
for i in range(1,13) :
    my_dict[i] = defaultdict(dict)

e = [[] for _ in range(m+1)]
f = defaultdict(set)


for k in range(1,m+1) :
    a,b = map(int,sys.stdin.readline().split())
    e[k] = (a,b)


    for i in range(a,n+1, b) :
        f[i].add(k)


start,end = map(int,sys.stdin.readline().split())
temp = bfs(e,f,start,end,n,m)

if temp == '' :
    print(-1)
else :
    for c in temp.split(',') :
        print(c)


