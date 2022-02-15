import sys
n = int(sys.stdin.readline().rstrip())
m = list(map(int,sys.stdin.readline().split()))

l,r,ans = 0, len(m)-1, 0

while l < r :
    ans = max(ans, (min(m[r], m[l]) * (r-l-1)))
    if m[l] <= m[r] :
        l +=1
    else :
        r -=1
print(ans)