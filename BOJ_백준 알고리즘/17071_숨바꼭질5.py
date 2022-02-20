import sys
from collections import deque


def inner_function(now_posi, next_time, que, v ):
    if now_posi + 1 <= 500000 and v[now_posi + 1] > next_time:
        v[now_posi + 1] = next_time
        que.append((now_posi + 1, next_time))

    if now_posi - 1 >= 0 and v[now_posi - 1] > next_time:
        v[now_posi - 1] = next_time
        que.append((now_posi - 1, next_time))

    if now_posi * 2 <= 500000 and v[now_posi * 2] > next_time:
        v[now_posi * 2] = next_time
        que.append((now_posi * 2, next_time))
    return

def sol(n):
    global ans
    que = deque()
    que.append((n,0))

    if n % 2 == 0 :
        v_even[n] = 0
    else :
        v_odd[n] = 0

    while que :
        now_posi, time = que.popleft()
        next_time = time + 1
        if next_time % 2 == 0 :
            inner_function(now_posi, next_time, que, v_even)
        else :
            inner_function(now_posi, next_time, que, v_odd)

    return

def sol2(k):
    global ans
    time = 0
    while True:
        k = k + time
        if k > 500000 :
            return
        if time % 2 == 0 :
            if v_even[k] <= time:
                ans = time
                return
        elif time % 2 == 1:
            if v_odd[k] <= time:
                ans = time
                return

        time +=1


n,k = map(int,sys.stdin.readline().split())
v_odd = [9876543210 for _ in range(500000 + 1 )]
v_even = [9876543210 for _ in range(500000 + 1 )]

ans = 9876543210
if n == k :
    print(0)
else :
    myStr = sol(n)
    sol2(k)

    if ans == 9876543210 :
        print(-1)

    else:
        print(ans)
