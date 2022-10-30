import sys
from collections import deque


def bfs(graph,cordi) :
    x,y = cordi
    graph[x][y] = 0 #init
    que = deque([cordi])
    while que :
        x,y = que.popleft()
        for i in posi_list :
            next_x = x + i[0]
            next_y = y + i[1]
            if next_x < 1 or next_x > n or next_y < 1 or next_y > m :
                continue
            elif graph[next_x][next_y] == 0 :
                continue
            elif graph[next_x][next_y] == 1 : # it da
                que.append([next_x,next_y])
                graph[next_x][next_y] = graph[x][y] + 1



n,m = map(int,sys.stdin.readline().split())
graph_cordi = [ [0] for _ in range(n+1)]
for p in range(1,n+1) :
    for abc in str(sys.stdin.readline().rstrip()) :
        graph_cordi[p].append(int(abc))

posi_list = [[1,0],[0,1],[-1,0],[0,-1]]
bfs(graph_cordi,[1,1])
print(graph_cordi[n][m] + 1)