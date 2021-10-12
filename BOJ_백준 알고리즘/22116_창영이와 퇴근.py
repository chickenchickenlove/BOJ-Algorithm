import sys
from collections import deque

def bfs(my_list, target, n):
    v = [[0 for _ in range(n)] for _ in range(n)]
    que = deque()
    que.append((0,0))
    v[0][0] = 1
    tra_list = [[1,0],[0,1],[-1,0],[0,-1]]

    while que :
        r,c = que.popleft()
        if r == n-1 and c == n-1 : return True
        for rr,cc in tra_list :
            next_r,next_c = r+rr, c+cc
            if -1 < next_r < n and -1 < next_c < n :
                if v[next_r][next_c] == 0 and abs(my_list[next_r][next_c] - my_list[r][c]) <= target :
                    que.append((next_r,next_c))
                    v[next_r][next_c] = 1

    return False

n = int(sys.stdin.readline().rstrip())

my_list = [[] for _ in range(n)]
max_=0
min_=sys.maxsize
for i in range(n) :
    temp = list(map(int,sys.stdin.readline().split()))
    for kkk in temp :
        max_ = max(kkk,max_)
        min_ = min(kkk,min_)
        my_list[i].append(kkk)



l = 0
r = max_ + 10
answer = 9876543210
while l <= r :
    m = (l+r+1)//2
    if bfs(my_list,m,n) :
        if answer == m :
            r = m-1
        else :
            answer = min(answer, m)
            r = m
    else :
        l = m+1

print(answer)




