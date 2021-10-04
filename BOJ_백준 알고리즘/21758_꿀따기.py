import sys

n = int(sys.stdin.readline().rstrip())
my_list = list(map(int, sys.stdin.readline().split()))
s = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    s[i] = s[i - 1] + my_list[i - 1]
answer = 0

for k in range(2, n):
    temp = (s[k] - s[1]) + (s[-2] - s[k - 1])
    answer = max(answer, temp)

for k in range(2, n):
    temp = (s[-2] - s[k]) + 2 * (s[k - 1] - s[0])
    answer = max(answer, temp)

for k in range(2, n):
    temp = (s[k - 1] - s[1] + 2 * (s[-1] - s[k]))
    answer = max(answer, temp)

print(answer)