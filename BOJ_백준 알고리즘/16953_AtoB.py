from collections import deque
import sys

def bfs(a,b) :
    que = deque()
    que.append([a,1])
    while que :
        a,my_cnt = que.popleft()
        if a == b :
            return my_cnt
        else :
            if a*2 <= b:
                que.append([a*2,my_cnt+1])
            if int(str(a)+'1') <= b:
                que.append([int(str(a)+'1'),my_cnt+1])

a,b = map(int,sys.stdin.readline().split())
temp = bfs(a,b)

if temp == None:
    print(-1)
else :
    print(temp)









