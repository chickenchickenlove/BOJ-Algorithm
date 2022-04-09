import sys
from collections import deque

def dfs(r,c,v) :
    global n,m, ans, cnt
    ans = max(ans, v[r][c])
    for rr,cc in tra_list :
        next_r, next_c = r+rr, c+cc
        if -1 < next_r< n and -1 < next_c < m :
            if v[next_r][next_c] != 0  : continue
            if my_map[next_r][next_c] == "." : continue
            v[next_r][next_c] = 1
            cnt +=1
            dfs(next_r, next_c, v)
            # v[next_r][next_c] = 0


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
            cnt = 0
            dfs(r,c,v)
            ans = max(ans,cnt)

print(ans)