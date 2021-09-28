import sys
import heapq

# 배울점
# 최소힙, 최대힙 동기화 하는 방법 (튜플로 동기화)
# 동기화 했을 때, 삭제하는 방법 (Lazy Propagation 같은 느낌)

t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    hq = []
    hq2 = []
    k = int(sys.stdin.readline().rstrip())
    cnt = 0
    v = [0 for _ in range(1000000 + 1)]
    for __ in range(k) :
        a,b = map(str,sys.stdin.readline().split())

        if a == 'I' :
            cnt +=1
            heapq.heappush(hq,(int(b),cnt))
            heapq.heappush(hq2,(-int(b),cnt))
        elif a == 'D' :
            if len(hq) == 0 :
                continue
            if b == '-1'  :
                if len(hq) > 0:
                    if v[hq[0][1]] == 0:
                        q, w = heapq.heappop(hq)
                        v[w] = 1
                    else:
                        while v[hq[0][1]] == 1:
                            heapq.heappop(hq)
                            if len(hq) == 0:
                                break
                        if len(hq) > 0:
                            q, w = heapq.heappop(hq)
                            v[w] = 1


            elif b == '1' :
                if len(hq2) > 0 :
                    if v[hq2[0][1]] == 0 :
                        q, w = heapq.heappop(hq2)
                        v[w] = 1
                    else :
                        while v[hq2[0][1]] == 1 :
                            heapq.heappop(hq2)
                            if len(hq2) == 0 :
                                break
                        if len(hq2) > 0 :
                            q, w = heapq.heappop(hq2)
                            v[w] = 1



    answer_list = []
    while hq :
        a,b = heapq.heappop(hq)
        if v[b] == 0 :
            answer_list.append(a)
    if len(answer_list) == 0 :
        print('EMPTY')
    else :

        answer_list = sorted(answer_list)
        print(answer_list[-1], answer_list[0])