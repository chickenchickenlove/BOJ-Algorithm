import sys
from collections import deque


def bfs(my_list, fish, sr, sc, value, now_cnt) :
    global n
    stack = []
    que = deque()

    v = [[0 for _ in range(n)] for _ in range(n)]
    v[sr][sc] = 1
    que.append((sr,sc,0))
    sflag = 'F'

    while que :
        r,c,cnt = que.popleft()
        if 0 < my_list[r][c] < value :
            if sflag == 'F' :
                sflag = 'T'
                stack.append((r, c, cnt))
            elif sflag == 'T' :
                if stack[0][-1] == cnt :
                    stack.append((r,c,cnt))
                elif stack[0][-1] < cnt :
                    break
            continue

        for rr, cc in tra_list :
            next_r, next_c = r + rr, c+cc
            if -1 < next_r < n and -1 < next_c < n :
                if v[next_r][next_c] == 0 and my_list[next_r][next_c] <= value :
                    que.append((next_r, next_c, cnt+1))
                    v[next_r][next_c] = 1

    if len(stack) == 0 :
        return (-1,-1,-1)
    stack = sorted(stack, key = lambda x : (x[0], x[1]))
    dr,dc, time = stack[0]
    fish[my_list[dr][dc]].remove((dr,dc))
    my_list[dr][dc] = 0
    return (dr, dc, time)



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]





n = int(sys.stdin.readline().rstrip())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
fish = [set() for _ in range(7)]
for i in range(n) :
    for j in range(n) :
        if my_list[i][j] != 0 and my_list[i][j] != 9 :
            fish[my_list[i][j]].add((i,j))
        elif my_list[i][j] == 9:
            sr,sc = i,j


my_list[sr][sc] = 0

value = 2
now_cnt = 0
total_time = 0
while 1 :

    sr, sc, time = bfs(my_list, fish, sr, sc, value, now_cnt)
    if sr == -1 and sc == -1 and time == -1 :
        print(total_time)
        break
    total_time += time
    now_cnt +=1
    if now_cnt == value :
        value +=1
        now_cnt = 0

