import sys
from collections import deque

def bfs(my_list, n, height) :
    que = deque()
    que.append((0,0))
    v = [[0 for _ in range(n)] for _ in range(n)]
    v[0][0] = 1
    while que :
        r,c = que.popleft()
        if r == n-1 and c == n-1 :
            return True
        for rr,cc in tra_list :
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < n :
                if v[next_r][next_c] == 0 and abs(my_list[next_r][next_c] - my_list[r][c]) <= height :
                    v[next_r][next_c] = 1
                    que.append((next_r, next_c))
    return False

tra_list = [[1,0],[0,1],[-1,0],[0,-1]]

n = int(sys.stdin.readline().rstrip())
my_list = [[] for _ in range(n)]
min_, max_ = 9876543210, 0
for i in range(n) :
    temp = list(map(int,sys.stdin.readline().split()))
    for num in temp :
        my_list[i].append(num)
        min_ = min(min_,num)
        max_ = max(max_,num)

l,r,answer = 0,abs(max_- min_),9876543210
while l <= r :
    mid = (l+r)//2
    if bfs(my_list, n, mid) :
        r = mid - 1
        answer = min(answer, mid)
    else :
        l = mid + 1

print(answer)



