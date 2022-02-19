import sys
from collections import deque

def sol(n,k):
    global ans, time_
    que = deque()
    que.append((n,0))
    v[n] = 0

    while que :
        now_posi, time = que.popleft()

        if now_posi == k :
            time_ = min(time, time_ )
            ans +=1

        next_time = time + 1

        if now_posi + 1 <= 100000 and v[now_posi + 1] >= next_time :
            v[now_posi + 1] = next_time
            que.append((now_posi + 1 , next_time))

        if now_posi - 1 >= 0 and v[now_posi -1] >= next_time :
            v[now_posi - 1] = next_time
            que.append((now_posi -1 , next_time))

        if now_posi * 2  <= 100000 and v[now_posi * 2] >= next_time :
            v[now_posi * 2 ] = next_time
            que.append((now_posi * 2  , next_time))


n,k = map(int,sys.stdin.readline().split())
v = [9876543210 for _ in range(100000 + 1 )]
ans = 0
time_ = 987654321
if n == k :
    print(0)
    print(1)
else :

    myStr = sol(n, k)
    print(time_)
    print(ans)


