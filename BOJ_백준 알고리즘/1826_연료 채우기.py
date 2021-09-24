import sys
import heapq

n = int(sys.stdin.readline().rstrip())
hq = []

for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    heapq.heappush(hq,((a,b)))
l,p = map(int,sys.stdin.readline().split())

answer = 0
a_p = p
last_a_p = p
hq2 = []

#현재 연료 상태로 갈 수 있는 곳들을 다 때려넣는다.
#거기서 가장 큰 놈을 빼서 연료 상태를 올린다.

while a_p < l :
    while a_p >= hq[0][0] :
        q,w = heapq.heappop(hq)
        heapq.heappush(hq2,(-w,q))
        if len(hq) == 0 :
            break
    if len(hq2) > 0 :
        q,w = heapq.heappop(hq2)
        a_p += -q
        answer +=1
    if last_a_p == a_p :
        break
    last_a_p = a_p

if a_p >= l :
    print(answer)
else :
    print(-1)
