import sys
from collections import deque

def sol(my_list, targe) :
    global n
    que = deque()
    que.append((0,0, min(my_list[0][0], my_list[n-1][n-1]), max(my_list[0][0], my_list[n-1][n-1])))

    min_map = [[set() for _ in range(n)]for _ in range(n)]
    max_map = [[set() for _ in range(n)] for _ in range(n)]

    min_map[0][0].add(my_list[0][0])
    max_map[0][0].add(my_list[0][0])

    while que :
        r,c,min_, max_ = que.popleft()
        if r == n-1 and c == n - 1 :
            return True
        for rr, cc in tra_list :
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < n :
                if abs(min(min_, my_list[next_r][next_c]) - max(max_, my_list[next_r][next_c])) <= targe  :
                    next_min = min(min_, my_list[next_r][next_c])
                    next_max = max(max_, my_list[next_r][next_c])
                    if next_min in min_map[next_r][next_c] and next_max in max_map[next_r][next_c] :
                        continue
                    que.append((next_r, next_c, min(min_, my_list[next_r][next_c]), max(max_, my_list[next_r][next_c])))
                    min_map[next_r][next_c].add(next_min)
                    max_map[next_r][next_c].add(next_max)


# 같은 지점에 왔을 때, 포함되는 구간이 반복되는 경우가 있음. 이걸 que에서 없애줘야할 거 같다.
    return False



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]

n = int(sys.stdin.readline().rstrip())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
l,r,ans = 0, 200, 200
while l <= r :
    mid = (l+r) // 2
    if sol(my_list, mid) :
        r = mid - 1
        ans = min(ans, mid)
    else :
        l = mid + 1

print(ans)
