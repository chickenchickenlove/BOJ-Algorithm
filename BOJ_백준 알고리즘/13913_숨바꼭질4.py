import sys
from collections import deque

def sol(n,k):
    que = deque()
    que.append((n,0,""))
    v[n] = 0

    while que :
        now_posi, time, path = que.popleft()

        if now_posi == k :
            print(time)
            return path

        next_time = time + 1

        if now_posi + 1 <= 100000 and v[now_posi + 1] > next_time :
            v[now_posi + 1] = next_time
            que.append((now_posi + 1 , next_time, path + "+"))

        if now_posi - 1 >= 0 and v[now_posi -1] > next_time :
            v[now_posi - 1] = next_time
            que.append((now_posi -1 , next_time,  path + "-"))

        if now_posi * 2  <= 100000 and v[now_posi * 2] > next_time :
            v[now_posi * 2 ] = next_time
            que.append((now_posi * 2  , next_time, path + "*"))


n,k = map(int,sys.stdin.readline().split())
v = [9876543210 for _ in range(100000 + 1 )]

if n == k :
    print(0)
    print(n)
else :
    myStr = sol(n, k)
    my_list = [n]
    for s in myStr:
        if s == "+":
            my_list.append(my_list[-1] + 1)
        elif s == "-":
            my_list.append(my_list[-1] - 1 )
        elif s == "*":
            my_list.append(my_list[-1] * 2 )

    print(" ".join(map(str, my_list)))

