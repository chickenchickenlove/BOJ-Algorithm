import sys


n = int(sys.stdin.readline().rstrip())
num_list = list(map(int,sys.stdin.readline().split()))
num_list = num_list[::-1]
dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(n) :
	for j in range(i) :
		if num_list[j] > num_list[i] :
				dp[i] = max(dp[i], dp[j] + 1)
		else :
			dp[i] = max(dp[i], 1)
print(max(dp))