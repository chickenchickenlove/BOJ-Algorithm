import sys
from heapq import heappop, heappush


def get_min(minq, id_list) :
    #3번째값 출력, 없으면 -1을 출력한다.
    cnt = 0
    stack = set()
    while minq :
        score, my_id = heappop(minq)
        if id_list[my_id] != score : continue
        if (score, my_id) in stack : continue
        stack.add((score, my_id))
        cnt +=1
        if cnt == 3 :
            print(my_id)
            break

    if cnt < 3 : print(-1)
    while stack : heappush(minq, stack.pop())


def get_max(maxq, id_list) :
    #3번째값 출력, 없으면 -1을 출력한다.
    cnt = 0
    stack = set()
    while maxq :
        score, my_id = heappop(maxq)
        if id_list[-my_id] != -score : continue
        if (score, my_id) in stack : continue
        stack.add((score, my_id))
        cnt +=1
        if cnt == 3 :
            print(-my_id)
            break

    if cnt < 3 : print(-1)
    while stack : heappush(maxq, stack.pop())


# sys.stdin = open("input.txt")
input = sys.stdin.readline

minq = []
maxq = []
id_list = [-1 for _ in range(100_000 + 1)]

for _ in range(int(input().strip())):
    query = list(map(str,input().split()))
    if query[0] == "1" :
        my_id, my_score = map(int,query[1:])
        id_list[my_id] = my_score
        heappush(minq, (my_score, my_id))
        heappush(maxq, (-my_score, -my_id))

    if query[0] == "2" :
        id_list[int(query[1])] = -1

    if query[0] == "3" :
        get_min(minq, id_list)

    if query[0] == "4" :
        get_max(maxq, id_list)



