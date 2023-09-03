import sys
from collections import deque


def bfs(my_list,c,vv,limit,p,w) :
    que = deque()

    v = [9876543210 for _ in range(p+1)]
    v[c] = 0
    que.append((c,0))

    while que :
        node, time = que.popleft()
        next_time = time + 1
        if node == vv :
            return True


        for next_node, value in my_list[node] :
            if value >= limit and v[next_node] > next_time:
                v[next_node] = next_time
                que.append((next_node, next_time))

    return False
p,w = map(int,sys.stdin.readline().split())
c,v = map(int,sys.stdin.readline().split())

my_list = [[] for _ in range(p)]
for _ in range(w) :
    a,b,d = map(int,sys.stdin.readline().split())
    my_list[a].append((b,d))
    my_list[b].append((a,d))





l,r = 0, 9876543210
answer = 0

while l < r :
    mid = (l + r + 1 ) // 2
    a = bfs(my_list, c, v, mid, p, w)
    if a == True:
        l = mid

        answer = mid
    else :
        r = mid - 1


print(answer)