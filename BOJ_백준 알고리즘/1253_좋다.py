import sys

# 정렬, 두포인터.

n = int(sys.stdin.readline().rstrip())
my_list = list(map(int, sys.stdin.readline().split()))
my_list = sorted(my_list)

answer = 0
last = 0
for now_idx in range(len(my_list)):
    l = 0
    r = len(my_list) - 1
    while l < r:
        if my_list[l] + my_list[r] == my_list[now_idx]:
            if now_idx not in [l, r]:
                answer += 1
                break
            else:
                if r == now_idx:
                    r -= 1
                else:
                    l += 1
        elif my_list[l] + my_list[r] < my_list[now_idx]:
            l += 1
            last = 1
        else:
            r -= 1
            last = -1

print(answer)