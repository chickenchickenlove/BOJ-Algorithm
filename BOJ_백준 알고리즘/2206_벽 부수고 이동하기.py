import sys
from collections import deque


def bfs(my_graph,visit_list_value,visit_list_wall) :
    visit_list_value[1][1] = 1
    que = deque()
    if my_graph[1][1] == 1 :
        b_wall = 1
    else :
        b_wall = 0
    que.append([1,1,b_wall])
    while que :
        x,y,wall = que.popleft()
        for z in tra_list :
            next_x = x + z[0]
            next_y = y + z[1]
            if 0 < next_x < n+1 and 0 < next_y < m + 1 :
                if my_graph[next_x][next_y] == 1 and visit_list_value[next_x][next_y] == 0:
                    if wall == 0: #벽을 한번도 뚫은 적이 없을 때는 이렇게 하면 되겠네.
                        que.append([next_x,next_y,1])
                        visit_list_value[next_x][next_y] = visit_list_value[x][y] + 1
                        visit_list_wall[next_x][next_y] = 1
                elif my_graph[next_x][next_y] == 0 :
                    if visit_list_value[next_x][next_y] == 0 :
                        visit_list_value[next_x][next_y] = visit_list_value[x][y] + 1
                        visit_list_wall[next_x][next_y] = visit_list_wall[x][y]
                        que.append([next_x, next_y,visit_list_wall[next_x][next_y]])

                    elif visit_list_value[next_x][next_y] > 0 and wall == 0 and visit_list_wall[next_x][next_y] == 1 :
                        visit_list_value[next_x][next_y] = visit_list_value[x][y] + 1
                        visit_list_wall[next_x][next_y] = visit_list_wall[x][y]
                        que.append([next_x,next_y,visit_list_wall[next_x][next_y]])
                    if next_x == n and next_y == m :
                        return




tra_list = [[1,0],[0,1],[-1,0],[0,-1]]

n,m = map(int,sys.stdin.readline().split())

my_graph = [ [0] for _ in range(n+1)]
for p in range(1,n+1) :
    temp = str(sys.stdin.readline().rstrip())
    for k in temp :
        my_graph[p].append(int(k))

visit_list_value = [ [0 for _ in range(m+1)] for _ in range(n+1)]
visit_list_wall = [ [0 for _ in range(m+1)] for _ in range(n+1)]

bfs(my_graph,visit_list_value,visit_list_wall)
if visit_list_value[n][m] == 0 :
    print(-1)
else :
    print(visit_list_value[n][m])