import sys

n = sys.stdin.readline().rstrip()
d = [0 for _ in range(len(n) + 1)]

if n[0] != "0":
    d[1] = 1
else:
    print(0)
    exit()

if len(n) == 1:
    print(d[-1])
    exit()

# 2인 경우에는
if int(n[1]) == 0:
    if 1 <= int(n[0]) <= 2:
        d[2] = d[1]

else:
    if int(n[0]) == 2:
        if 0 < int(n[1]) <= 6:
            d[2] = 2
        else:
            d[2] = 1
    elif int(n[0]) == 1:
        d[2] = 2
    else:
        d[2] = 1

if len(n) == 2:
    print(d[-1])
    exit()

for i in range(3, len(n) + 1):
    if int(n[i - 1]) != 0:
        d[i] += d[i - 1] % 1000000

    # 1 < < 2 사이일 때
    if int(n[i - 2]) == 1:
        d[i] += d[i - 2] % 1000000
    elif int(n[i - 2]) == 2 and int(n[i - 1]) <= 6:
        d[i] += d[i - 2] % 1000000

print(d[-1] % 1000000)
