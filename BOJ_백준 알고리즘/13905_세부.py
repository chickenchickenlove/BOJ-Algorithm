import sys
from collections import deque


def bfs(start, e, d,value) :
    global n
    que = deque()
    v = [0 for _ in range(n+1)]

    v[start] = 1
    que.append(start)

    while que :
        now_node = que.popleft()
        if now_node == e :
            return True

        for next_node, limit in d[now_node] :
            if limit >= value and v[next_node] == 0 :
                v[next_node] = 1
                que.append(next_node)

    return False


n,m = map(int,sys.stdin.readline().split())
s,e = map(int,sys.stdin.readline().split())
d = [[] for _ in range(n+1)]
for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    d[a].append((b,c))
    d[b].append((a,c))


l = 0
r = sys.maxsize
answer = 0
while l < r :
    mid = (l+r+1) // 2
    if bfs(s,e,d,mid) :
        l = mid

        answer = max(answer,mid)
    else :
        r = mid - 1

print(answer)