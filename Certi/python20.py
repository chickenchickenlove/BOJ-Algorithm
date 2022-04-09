import sys
from heapq import heappop, heappush


# sys.stdin = open("input.txt")
input = sys.stdin.readline

n,m = map(int,input().split())
sid_table = [[0 for _ in range(m+1)] for _ in range(n+1)]
avg_table = [0 for _ in range(m+1)]
sum_table = [0 for _ in range(m+1)]
cnt_table = [0 for _ in range(m+1)]
minq = []
maxq = []
avgminq = []
avgmaxq = []


for i in range(1, m+1) :
    heappush(minq, (0,i))
    heappush(maxq, (0,-i))
    heappush(avgminq, (0, i))
    heappush(avgmaxq, (0, -i))


# clear에는 실제로 없애면 안된다.
# 모든 평가 정보를 삭제한다면... 그동안 스카우터가 실제로 선수들의 정보를 다 지워야한다.


def clearAll(sid):

    for pid, value in enumerate(sid_table[sid]) :
        if not pid or not value or not cnt_table[pid] : continue

        sum_table[pid] -= value
        cnt_table[pid] -=1
        if cnt_table[pid] != 0 :
            avg_table[pid] = round(sum_table[pid] / cnt_table[pid],1)
            heappush(minq, (sum_table[pid], pid))
            heappush(maxq, (-sum_table[pid], -pid))
            heappush(avgminq, (avg_table[pid], pid))
            heappush(avgmaxq, (-avg_table[pid], -pid))
        else :
            avg_table[pid] = 0
            heappush(minq, (0, pid))
            heappush(maxq, (0, -pid))
            heappush(avgminq, (0, pid))
            heappush(avgmaxq, (0, -pid))

        sid_table[sid][pid] = 0



for _ in range(int(input().strip())):
    query = list(map(str,input().split()))

    cmd = query[0]
    query_parameter = list(map(int,query[1:]))

    if cmd == "EVAL" :
        sid, pid, score = query_parameter

        if not sid_table[sid][pid] :
            sum_table[pid] += score
            cnt_table[pid] += 1
        else :
            sum_table[pid] -= sid_table[sid][pid]
            sum_table[pid] += score

        sid_table[sid][pid] = score
        avg_table[pid] = round(sum_table[pid]/cnt_table[pid], 1)
        heappush(minq, (sum_table[pid], pid))
        heappush(maxq, (-sum_table[pid], -pid))
        heappush(avgminq, (avg_table[pid], pid))
        heappush(avgmaxq, (-avg_table[pid], -pid))


    if cmd == "SUM" :
        if query_parameter[0] == 0 :
            while minq :
                my_sum, pid = heappop(minq)
                if sum_table[pid] != my_sum : continue
                print(pid)
                heappush(minq, (my_sum, pid))
                break
        else :
            while maxq :
                my_sum, pid = heappop(maxq)
                my_sum, pid = -my_sum, -pid
                if sum_table[pid] != my_sum : continue
                print(pid)
                heappush(maxq, (-my_sum, -pid))
                break


    if cmd == "AVG" :
        if query_parameter[0] == 0 :
            while avgminq :
                my_avg, pid = heappop(avgminq)
                if avg_table[pid] != my_avg : continue
                print(pid)
                heappush(avgminq, (my_avg, pid))
                break
        else :
            while avgmaxq :
                my_avg, pid = heappop(avgmaxq)
                my_avg, pid = -my_avg, -pid
                if avg_table[pid] != my_avg : continue
                print(pid)
                heappush(avgmaxq, (-my_avg, -pid))
                break

    if cmd == "CLEAR" :
        clearAll(query_parameter[0])
