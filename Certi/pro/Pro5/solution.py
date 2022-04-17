from typing import List
from collections import defaultdict
global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ
from heapq import heappop, heappush


def init(N: int, px: List[int], py: List[int]) -> None:
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ
    # print('init')
    FRIEND = [set([i]) for i in range(N)]
    HOME = []
    ORDER = [defaultdict(int) for _ in range(N)]
    PERSON_PQ = [[] for i in range(N)]
    CAFE = defaultdict(tuple)
    for x,y in zip(px, py): HOME.append((x,y))

def addCafe(cid: int, x: int, y: int) -> None:
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ
    # print('addCafe')
    CAFE[cid] = (x,y)

    for uid, cordi in enumerate(HOME):
        hx,hy = cordi
        dis = abs(hx-x) + abs(hy-y)
        heappush(PERSON_PQ[uid], (-ORDER[uid][cid], dis, cid))
        ORDER[uid][cid] = 0

    # print(PERSON_PQ[1])


def eraseCafe(cid: int) -> None:
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ
    # print('eraseCafe')
    CAFE[cid] = ()

    # print(PERSON_PQ[1])

def pushData(uid, cid):
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ

    hx,hy = HOME[uid]
    cx,cy = CAFE[cid]
    dis = abs(hx-cx) + abs(hy-cy)
    heappush(PERSON_PQ[uid], (-ORDER[uid][cid], dis, cid))


def order(uid: int, cid: int) -> None:
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ
    for person in FRIEND[uid] :
        ORDER[person][cid] += 1
        pushData(person, cid)


def beBuddy(tid: int, uid: int) -> None:
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ

    FRIEND[tid].add(uid)
    FRIEND[uid].add(tid)

    temp_list = []
    for cid, cnt in ORDER[tid].items() :
        if cnt == 0 : continue
        if CAFE[cid] == (): continue
        temp_list.append((uid,cid, cnt))

    for cid, cnt in ORDER[uid].items() :
        if cnt == 0: continue
        if CAFE[cid] == () : continue
        temp_list.append((tid, cid,cnt))

    for uid, cid, cnt in temp_list :
        ORDER[uid][cid] += cnt
        pushData(uid,cid)
    # print(PERSON_PQ[1])







"""
UID인 고객에게 CAFE 10개를 추천한다.
이 때, 우선순위가 10번째인 CID를 반환한다. 
호출횟수 : 최대 10000

1. 고객 + 친구들의 주문 횟수의 합 ↑ --> 
2. 1번이 동일할 때, 가까운 카페 
3. 2번이 동일할 때, ID가 작은 카페

1번에서 10개를 뽑는다. -> 해결되면 ㅇㅋ
안되면 2,3번에서 가장 마지막에 있는 녀석을 뽑는다. 
예를 들어 10개가 동순위였다고 하면... 10개를 돌리면서 2,3번에서 본다.


"""

def recommend(uid: int) -> int:
    global FRIEND, HOME, ORDER, DIS, CAFE, PERSON_PQ
    # print('recommand')
    # print(PERSON_PQ[1])


    # print(PERSON_PQ[1])

    stack = []

    while len(stack) < 10 :
        cnt, dis, cid = heappop(PERSON_PQ[uid])
        if ORDER[uid][cid] != -cnt or CAFE[cid] == (): continue
        stack.append((cnt,dis,cid))



    ans = stack[9][-1]

    while stack : heappush(PERSON_PQ[uid], stack.pop())
    return ans






#데이터 셋트

"""
데이터 셋트

1. 카페 : 총 6000개가 가능함.
2. 사람 : 총 25명의 사람이 가능함.
--> 각 사람마다 어떤 카페에 얼만큼 주문했는지를 확인해야함. 
--> 리스트로 접근한다. 6000 * 25 * 100,000 = 15억번. 리스트로 선형 탐색을 할 경우 할 수가 없다.

딕셔너리 접근 관점.
1. 총 3000번의 주문이 있다. 25명이 한번씩 주문한다고 한정하면, 대략 120개의 카페에 주문한다.
2. 3000 * 100,000 = 3억번 -> 가능할 것 같다. 
3. 주문한 정보는 딕셔너리로 가지고 있는다. 


친구 정보
1. 친구 정보는 어차피 전체 탐색을 해야한다. --> 각 사람은 각 리스트를 가진다. 25 * 25 = 625개


카페와 사람 간의 거리 + 카페 ID를 넣어준다. 
1. 1 * 6000 * 10000 = 6억 --> 모든 카페에 대해 매번 검색을 할 경우 느리다는 것을 알 수 있다.
2. 그리고 한번 정해진 카페는 없어지긴 하지만, 정해지면 그 거리는 유지가 된다.
3. 카페가 생길 때 마다 각 사람들에게 그것을 넣어주면 된다. 그리고 필요할 때 마다 
4. 필요할 때 마다 

"""


