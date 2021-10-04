import sys
n,k = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
pre_fix = [0 for _ in range(n+1)]
for i in range(0,n) :
    pre_fix[i+1] = pre_fix[i] + my_list[i]

answer = -9876543210

for i in range(n+1) :
    if i+k < n+1 :
        answer = max(answer, pre_fix[i+k] - pre_fix[i])
print(answer)

