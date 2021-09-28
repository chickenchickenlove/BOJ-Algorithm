import heapq
import sys
from collections import deque


# 대기 시간이 짧은 곳으로 이동함
# 대기 시간이 동일하면 → 가장 작은 번호로 안내
# 같이 계산 끝나면, 높은 번호가 먼저 나감
# 계산 걸리는 시간은 물건 갯수 (W개면 W분 소요)

#N : 고객 수
#K : 계산대 수



# 1. 나갈 고객이 있는지 확인한다. 기다리고 있는 고객을 먼저 넣어준다.
# 2. 나갈 고객을 답에 처리한다. (1 * r1 + 2 * r2 , cnt 처리 해주자)


n,k = map(int,sys.stdin.readline().split())
hq = []
time = 1
answer = 0
answer_cnt = 1
wait = []
for iii in range(1,k+1) :
    wait.append(iii)

heapq.heapify(wait)
p_list = []
answer_list = []
for _ in range(n) :
    a, b = map(int, sys.stdin.readline().split())

    #대기하고 있는 안내원이 없을 때
    #안내원이 있도록 만들어준다.
    if len(wait) == 0 :

        # 시간이 같아지도록 시간을 흘려준다.
        if len(hq) > 0 :
            while hq[0][0] > time :
                time +=1

        #시간이 같으면, 현재 시간에 나올 수 있는 계산원들을 다 나오게 한다.
        while hq[0][0] == time :
            q,w,e = heapq.heappop(hq)
            heapq.heappush(wait,w)
            p_list.append(e)
            if len(hq) == 0 :
                break

        while p_list:
            answer_list.append(p_list.pop())



    w = heapq.heappop(wait)
    heapq.heappush(hq, (time + b, w, a))


while hq :
    if len(hq) > 0:
        while hq[0][0] > time:
            time += 1

    # 시간이 같으면, 현재 시간에 나올 수 있는 계산원들을 다 나오게 한다.
    while hq[0][0] == time:
        q, w, e = heapq.heappop(hq)
        heapq.heappush(wait, w)
        p_list.append(e)
        if len(hq) == 0 :
            break

    while p_list:
        answer_list.append(p_list.pop())



while p_list:
    answer_list.append(p_list.pop())


for idx,value in enumerate(answer_list) :
    answer += (idx+1) * value


print(answer)


