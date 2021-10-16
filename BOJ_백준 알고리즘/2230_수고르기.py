import sys

n, m = map(int, sys.stdin.readline().split())
my_list = sorted([int(sys.stdin.readline().rstrip()) for _ in range(n)])
l, r, answer = 0, 0, 9876543210
while l <= r:
    if my_list[r] - my_list[l] < m:
        r += 1
    else:
        answer = min(my_list[r] - my_list[l], answer)
        l += 1
    if r == len(my_list):
        break

while l < len(my_list):
    if my_list[r - 1] - my_list[l] >= m:
        answer = min(my_list[r - 1] - my_list[l], answer)
    l += 1
print(answer)


