import sys
n,k,b = map(int,sys.stdin.readline().split())
v = [0 for _ in range(n+1)]
for i in range(b) : v[int(sys.stdin.readline().rstrip())] = 1
b_cnt = 0
l,r,ans = 1,1,9876543210

for i in range(1,k+1) :
    if v[i] == 1 :
        b_cnt +=1
    r = i
ans = min(ans,b_cnt)
for i in range(k+1, n+1) :
    r += 1
    if r >= n+1 :
        break
    if v[r] == 1 :b_cnt +=1
    if v[l] == 1 :b_cnt -=1
    l +=1
    ans = min(ans,b_cnt)

print(ans)