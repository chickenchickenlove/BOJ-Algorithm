import sys
import heapq as hq

# sys.stdin = open('input.txt')
input = sys.stdin.readline

hq1 = []
hq2 = []
hq3 = []

#x가 0일 때 출력해서 넣는다.
for _ in range(int(input().rstrip())):
    n = int(input().rstrip())
    if n == 0 :
        if len(hq2) == 0 :
            print(-1)
        else :
            a,b,c = -hq.heappop(hq2), hq.heappop(hq1), hq.heappop(hq3)[-1]
            print(a,b,c)
    else :
        hq.heappush(hq1, n)
        hq.heappush(hq2, -n)
        hq.heappush(hq3, (abs(n),n))

