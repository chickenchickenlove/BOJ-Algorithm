import sys
n = int(sys.stdin.readline().rstrip())
d = [0 for _ in range(82)]
d[0] = 0
d[1] = 1
d[2] = 1
for i in range(3,82) :
    d[i] = d[i-1] + d[i-2]

print(2*(d[n] + d[n+1]))