import sys
n = int(sys.stdin.readline().rstrip())
a = list(map(int,sys.stdin.readline().split()))
dp = [9876543210 for _ in range(n+1)]
dp[1] = a[0]

for idx in range(2, n+1) :
	dp[idx] = a[idx-1]
	for interval in range(idx):
		dp[idx] = min(dp[idx-interval-1] + a[interval], dp[idx])
print(dp[-1])