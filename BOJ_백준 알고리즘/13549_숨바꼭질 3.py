import sys
from collections import deque

def sol(n,k):
    que = deque()
    que.append((n,0))
    v[n] = 0

    while que :
        now_posi, time = que.popleft()

        if now_posi == k :
            print(time)
            return

        next_time = time + 1

        if now_posi + 1 <= 100000 and v[now_posi + 1] > next_time :
            v[now_posi + 1] = next_time
            que.append((now_posi + 1 , next_time))

        if now_posi - 1 >= 0 and v[now_posi -1] > next_time :
            v[now_posi - 1] = next_time
            que.append((now_posi -1 , next_time))

        if now_posi * 2  <= 100000 and v[now_posi * 2 ] > time :
            v[now_posi * 2 ] = time
            que.appendleft((now_posi * 2  , time))


n,k = map(int,sys.stdin.readline().split())
v = [9876543210 for _ in range(100000 + 1 )]

sol(n,k)






