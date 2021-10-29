import sys
from collections import deque

n,w,l = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
d = [0 for _ in range(n)]
que = deque()
ans = 0
my_sum = 0

while 1 :
    ans +=1
    for i in range(n) :
        if d[i] != 0 and d[i] != w + 1:
            d[i] +=1
    if que :
        if d[que[0]] == w + 1 :
            my_sum -= my_list[que[0]]
            que.popleft()

    i = 0
    while d[i] != 0 :
        i +=1
        if i == n :
            break
    if i != n :
        if my_list[i] + my_sum <= l :
            que.append(i)
            my_sum += my_list[i]
            d[i] = 1

    if d[n-1] == w+1 :
        print(ans)
        break







