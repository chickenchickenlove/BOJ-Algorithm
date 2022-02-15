import sys

n = int(sys.stdin.readline().rstrip())
m = list(map(int, sys.stdin.readline().split()))


def two_pointer(l, r, m, idx):
    global ans
    while l < r:
        now_sum = m[l] + m[r]
        if now_sum == m[idx]:
            if l != idx and r != idx:

                ans += 1
                return
            else:
                if r == idx:
                    r -= 1
                else:
                    l += 1
        elif now_sum > m[idx]:
            r -= 1
        elif now_sum < m[idx]:
            l += 1


m = sorted(m)
ans = 0
for idx in range(len(m)):
    l, r = 0, len(m) - 1
    two_pointer(l, r, m, idx)
print(ans)

