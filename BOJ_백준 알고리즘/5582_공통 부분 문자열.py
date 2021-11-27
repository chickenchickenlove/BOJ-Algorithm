import sys
a = str(sys.stdin.readline().rstrip())
b = str(sys.stdin.readline().rstrip())

d = [ [0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
max_len = 0

for i in range(1,len(b)+1) :
    for j in range(1,len(a)+1) :
        if b[i-1] == a[j-1] :
            d[i][j] = d[i-1][j-1] + 1
            if max_len < d[i][j] :
                max_len = d[i][j]

print(max_len)