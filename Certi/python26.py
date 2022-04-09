import sys
from collections import deque

def bfs(sr,sc,v) :
    global n,m, ans

    que = deque()
    cnt = 1

    que.append((sr,sc))
    v[sr][sc] = 1

    while que :
        r,c= que.popleft()

        for rr,cc in tra_list :
            next_r, next_c = r+rr, c+cc

            if -1 < next_r < n and -1 < next_c < m :
                if v[next_r][next_c] == 0 and my_map[next_r][next_c] == "*" :
                    que.append((next_r, next_c))
                    v[next_r][next_c] = 1
                    cnt +=1

    return cnt

tra_list = [[1,0],[0,1],[-1,0],[0,-1]]


# sys.stdin = open("input.txt")
input = sys.stdin.readline
n,m = map(int, input().split())
n,m = m,n
my_map = [input().strip() for _ in range(n)]


v = [[0 for _ in range(m)] for _ in range(n)]
ans = 0
for r in range(n) :
    for c in range(m) :
        if my_map[r][c] == "*" and not v[r][c]:
            ans = max(bfs(r,c,v),ans)
print(ans)