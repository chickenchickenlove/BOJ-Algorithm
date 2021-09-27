import sys
import heapq

n = int(sys.stdin.readline().rstrip())
hq = []
max_day = 0
for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    max_day = max(max_day, a)
    heapq.heappush(hq,(-a,b))

hq2 = []
answer = 0
for now_day in range(max_day+1, 0, -1) :
    if len(hq) > 0 :
        while now_day == -hq[0][0] :
            a,b = heapq.heappop(hq)
            heapq.heappush(hq2,-b)
            if len(hq) == 0 :
                break

    if len(hq2) > 0 :
        b = heapq.heappop(hq2)
        answer -= b


print(answer)