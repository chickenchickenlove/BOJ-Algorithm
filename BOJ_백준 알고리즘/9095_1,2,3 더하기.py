import sys


def find(num):
    if num <= 0: return 0
    if num <= 3: return dp[num]
    return find(num - 1) + find(num - 2) + find(num - 3)


for _ in range(int(sys.stdin.readline().rstrip())):
    target = int(sys.stdin.readline().rstrip())
    dp = [0 for _ in range(11)]
    dp[0:3] = 0, 1, 2, 4

    print(find(target))