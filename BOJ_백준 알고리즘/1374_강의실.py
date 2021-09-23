import sys
import heapq

n = int(sys.stdin.readline().rstrip())
my_list = []
for _ in range(n) :
    a,b,c = map(int,sys.stdin.readline().split())
    my_list.append((b,c,a))


my_list = sorted(my_list)
answer = 0
hq = []
for b,c,a in my_list :
    if len(hq) == 0 :
        heapq.heappush(hq,(c))
    else :
        if hq[0] <= b :
            heapq.heappop(hq)
        heapq.heappush(hq, (c))
    answer = max(answer, len(hq))

print(answer)



