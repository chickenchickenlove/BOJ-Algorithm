import sys
n = int(sys.stdin.readline().rstrip())
d = [x for x in range(n+1)]


for i in range(4,n+1) :
    for j in range(1,i+1) :
        if i - j**2 < 0 :
            break
        if d[i] > d[i-j**2] + 1 :
            d[i] = d[i-j**2] + 1

print(d[n])
