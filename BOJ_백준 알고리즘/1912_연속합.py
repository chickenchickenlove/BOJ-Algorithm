import sys

sys.setrecursionlimit(100000)


def sol(num):
    global ans
    if num == - 1: return 0
    pre_num = num - 1
    pre_sum = sol(pre_num)

    now_max = max(num_list[num] + pre_sum, num_list[num])
    ans = max(ans, now_max)
    return now_max


ans = -9876543210
n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
sol(n - 1)
print(ans)