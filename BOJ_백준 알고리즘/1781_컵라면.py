import sys
import heapq


n = int(sys.stdin.readline().rstrip())
hq = []
dl = 0

for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    dl = max(dl, a)
    hq.append((a,-b))

heapq.heapify(hq)
hq2 = []

for i in range(1, dl + 1) :
    if len(hq) > 0 :
        cnt = 0
        while hq[0][0] <= i and cnt < i :
            a,b = heapq.heappop(hq)
            heapq.heappush(hq2, (-b))
            cnt +=1
            if len(hq) == 0 :
                break

    if len(hq) > 0 :
        while hq[0][0] <= i :
            heapq.heappop(hq)
            if len(hq) == 0 :
                break

    while len(hq2) > i:
        heapq.heappop(hq2)


print(sum(hq2))