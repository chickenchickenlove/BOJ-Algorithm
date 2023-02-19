import sys
from collections import deque


def bfs(graph,tomato) :
    que = deque()
    for p in tomato :
        que.append(p)
        z,x,y = p
        graph[z][x][y] = graph[z][x][y] + 1
    while que :
        z,x,y = que.popleft()
        for position in find_li :
            next_x = x + position[1]
            next_y = y + position[2]
            next_z = z + position[0]
            if next_z < 1 or next_z > h or next_x < 1 or next_y < 1 or next_x > n or next_y > m :
                continue
            elif graph[next_z][next_x][next_y] == -1 :
                continue
            elif graph[next_z][next_x][next_y] == 0  :
                graph[next_z][next_x][next_y] = graph[z][x][y] + 1
                que.append([next_z,next_x,next_y])

m,n,h = map(int,sys.stdin.readline().split())
num_list = [[[0] for _ in range(n+1)] for _ in range(h+1)]
for zb in range(1,h+1) :
    for i in range(1,n+1) :
        a = list(map(int,sys.stdin.readline().split()))
        for k in a :
            num_list[zb][i].append(k)

find_li = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,-1],[0,0,1]]
day = 0
tomato_list = []

for k in range(1,h+1) :
    for i in range(1,n+1) :
        for j in range(1,m+1) :
            if num_list[k][i][j] == 1 :
                tomato_list.append([k,i,j])

bfs(num_list,tomato_list)
max_num = -1
end_flag = 'T'

for k in range(1,h+1) :
    for i in range(1,n+1):
        for j in range(1,m+1) :
                if num_list[k][i][j] == 0 :
                     end_flag = 'F'
                if num_list[k][i][j] > max_num :
                     max_num = num_list[k][i][j]

if end_flag == 'T' :
    print(max_num-2)
else :
    print(-1)