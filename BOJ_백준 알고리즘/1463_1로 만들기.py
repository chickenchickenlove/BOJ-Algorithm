import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dp = [9876543210 for _ in range(n + 1)]
cnt = 0


def sol(n):
    que = deque()
    que.append((1, 1))
    dp[1] = 0
    while que:
        now_node, cnt = que.popleft()
        next_cnt = cnt + 1

        if now_node * 2 <= n and dp[now_node * 2] > next_cnt:
            dp[now_node * 2] = cnt
            que.append((now_node * 2, next_cnt))

        if now_node * 3 <= n and dp[now_node * 3] > next_cnt:
            dp[now_node * 3] = cnt
            que.append((now_node * 3, next_cnt))

        if now_node + 1 <= n and dp[now_node + 1] > next_cnt:
            dp[now_node + 1] = cnt
            que.append((now_node + 1, next_cnt))


sol(n)
print(dp[-1])