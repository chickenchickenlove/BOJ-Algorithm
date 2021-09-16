import sys
from collections import deque

#1번섬 출발, 1번섬 도착

def bfs(gems, island) :
    que = deque()


    gem_dict = {}
    cnt = 0
    for i in gems :
        gem_dict[i] = cnt
        cnt +=1

    v = [[-1 for _ in range(n+1)] for _ in range(2**len(gems))]

    if 1 in gems :
        que.append((1,1,0 | 1 << gem_dict[1]))
        v[0 | 1 << gem_dict[1]][1] = 1

    que.append((1,0,0))
    v[0][1] = 0

    answer = 0


    while que :
        now_node, now_cnt, gem_status = que.popleft()
        if now_node == 1 :
            answer = max(answer, now_cnt)


        for next_node, next_limit in island[now_node] :
            if now_cnt <=  next_limit :

                if v[gem_status][next_node] < now_cnt :
                    v[gem_status][next_node] = now_cnt
                    que.append((next_node, now_cnt, gem_status))

                if next_node in gems :
                    next_gem_status = gem_status
                    next_cnt = now_cnt

                    if gem_status & 1 << gem_dict[next_node] == 0 :
                        next_gem_status = gem_status | 1 << gem_dict[next_node]
                        next_cnt +=1

                    if v[next_gem_status][next_node] < next_cnt and next_limit >= now_cnt :
                        v[next_gem_status][next_node] = next_cnt
                        que.append((next_node, next_cnt, next_gem_status))



    return answer



n,m,k = map(int,sys.stdin.readline().split())
gems = set()

for _ in range(k) :
    gems.add(int(sys.stdin.readline().rstrip()))

island = [[] for _ in range(n + 1 )]
for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    island[a].append((b,c))
    island[b].append((a,c))




print(bfs(gems,island))


