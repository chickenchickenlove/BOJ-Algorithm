import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
num_list = num_list[::-1]
dp = [0 for _ in range(n)]
prev = [-6 for _ in range(n)]
dp[0] = 1

for i in range(n):
    for j in range(n):
        if num_list[j] > num_list[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j
        else:
            if 1 > dp[i]:
                dp[i] = 1
                prev[i] = -1

print(max(dp))
s = dp.index(max(dp))
while 1:
    print(num_list[s], end=' ')
    s = prev[s]
    if s == -6:
        break

    if prev[s] == -1:
        print(num_list[s])
        break