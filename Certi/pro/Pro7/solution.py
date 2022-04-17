### solution.py

from typing import List
from collections import defaultdict
from heapq import heappush, heappop
global DURATION, CAPACITY, TERMTIME, WAITING, TOTAL, PROC

"""
처음에 들어오는 경우를 생각해보자.
1. 두 가지로 나눠서 처리를 해야할 것 같다.
2. tick 시간 전인 경우에 처리하는 애들을 만들어서 처리를 한다.
3. 그리고 값을 넣어준다
4. tick 시간에 딱 도착했을 때 처리하는 애들을 만들어서 처리를 한다. 
"""




"""
체험 1회 파라미터  
    - duration : 운영시간
    - capacity : 수용인원

고객이 없으면
    체험관은 대기한다.
    
고객이 있으면
    체험관에 1명 이상 고객이 tick 시간에 추가된 경우, 체험관은 즉시 운행함.
        시작 시간 : tick
        종료 시간 : tick + duration
    tick+duration 전에 온 사람 : 대기자 명단.
    tick+duration 시각에 도착 고객 : 대기자 가능
    
체험관 운영
    capacity 초과 X
        모든 대기자가 체험관에 입장.
    capacity 초과 
        우선순위 높은 순으로 capacity만큼 입장.
"""




"""
변수
1. tick (시각) : 0 초기화
2. boothN -> booth N개의 체험관 id, 운영시간, 수용정보가 주어짐.
3. 체험관 id는 유일함.

범위
    n : 3 ~ 100
    체험관 ID : 0 ~ 10억 --> 배열로는 할 수 없음. > 
    duration : 1 ~ 100초
    capacity : 1 `100초 
> 각 체험관 공간은 딕셔너리로 생성하거나, 배열로 생성해서 key - value로 묶어준다. 

"""

def init(boothN: int, bidArr: [int], duration: [int], capacity: [int]):
    global DURATION, CAPACITY, TERMTIME, WAITING, TOTAL, PROC

    DURATION = defaultdict(int)
    CAPACITY = defaultdict(int)
    TERMTIME = defaultdict(int)
    WAITING = defaultdict(list)
    TOTAL = defaultdict(int)
    PROC = defaultdict(int)

    for i in range(boothN) :
        name = bidArr[i]
        dura = duration[i]
        capa = capacity[i]
        DURATION[name] = dura
        CAPACITY[name] = capa




"""
- TICK 시간, BID 체험관, 우선순위를 가지는 손님을 guestNum만큼 추가한다.
- 즉, 대기열의 사람들을 체험관에 때려박는 것임. 
- Pri가 높을수록 우선순위가 높음.
- 대기중인 고객이 없는 경우 0을 반환한다. 있는 경우 가장 우선순위가 높은 놈을 반환한다.

최대 호출 : 10000
"""

def process_pre(tick, bid) :
    global DURATION, CAPACITY, TERMTIME, WAITING, TOTAL, PROC

    if not PROC[bid] : TERMTIME[bid] = tick


    ""
    while TERMTIME[bid]  < tick :
        if not WAITING[bid] : break

        temp_capa = 0
        # 대기중인 사람들 처리
        while temp_capa <= CAPACITY[bid]  :
            PROC[bid] = 1
            if not WAITING[bid] : break
            PROC[bid] = 1
            pri, capa = heappop(WAITING[bid])
            if temp_capa + capa >= CAPACITY[bid] :
                gain = CAPACITY[bid] - temp_capa
                remain = capa - gain
                if remain > 0 :
                    heappush(WAITING[bid], (pri, remain))
                TOTAL[bid] -= gain

                break
            TOTAL[bid] -= capa
            temp_capa += capa
        TERMTIME[bid] += DURATION[bid]

    if TERMTIME[bid] <= tick :
        PROC[bid] = 0


def process_after(tick, bid) :
    global DURATION, CAPACITY, TERMTIME, WAITING, TOTAL, PROC

    if not PROC[bid] : TERMTIME[bid] = tick
    if TERMTIME[bid] <= tick :
        PROC[bid] = 0

    while TERMTIME[bid] <= tick :
        if not WAITING[bid] : break

        temp_capa = 0
        # 대기중인 사람들 처리
        while temp_capa <= CAPACITY[bid]  :

            if not WAITING[bid] : break
            PROC[bid] = 1
            pri, capa = heappop(WAITING[bid])
            if temp_capa + capa >= CAPACITY[bid] :
                gain = CAPACITY[bid] - temp_capa
                remain = capa - gain
                if remain > 0 :
                    heappush(WAITING[bid], (pri, remain))
                TOTAL[bid] -= gain

                break
            TOTAL[bid] -= capa
            temp_capa += capa
        TERMTIME[bid] += DURATION[bid]

    if TERMTIME[bid] <= tick :
        PROC[bid] = 0


def add(tick: int, bid: int, guestNum: int, priority: int):
    global DURATION, CAPACITY, TERMTIME, WAITING, TOTAL, PROC

    for findBid in DURATION.keys():
        process_pre(tick,findBid)

    TOTAL[bid] += guestNum
    heappush(WAITING[bid], (-priority, guestNum))

    for findBid in DURATION.keys():
        process_after(tick,findBid)


    if not WAITING[bid] : return 0
    return abs(WAITING[bid][0][0])



"""
TICK 시간에 대기중인 고객수가 많은 순으로 findCnt개의 체험관을 검색해야함.
tick 시간에 운영 시작해야 하는 경우, 체험관에 입장하는 고객은 대기 고객수에서 제외된다.
즉, 운영 먼저 처리 + 고객수 처리한다. 


우선순위
1. 대기수 많은 고객
2. 체험관 ID 큰 것 우선

10000 ~ 20000회 호출

체험관 전체 갯수 = 100 * 10000
1. 나이브
- 체험관 전체를 돌려본다. 어찌됐건, 각 체험관은 capacity만큼 처리를 해야하기 때문이다.
- 100 * 10000 = 1,000,000 할 수 있을 듯. 

2. 필요한 데이터
- 체험관의 정보 : capacity, duration, 끝나는 시간 --> 각각 default dict으로 만든다. 
- 체험관에 대기하고 있는 사람들 : defaultDict(pq) 형식 -> (-pri, count)




3. 필요한 로직
- 매번 for 문을 돌면서 TC 처리를 해줘야함.
- TC 처리
  

"""



def search(tick: int, findCnt: int, bidArr: [int], numResult: [int]):
    global DURATION, CAPACITY, TERMTIME, WAITING, TOTAL
    # print(tick)
    for bid in DURATION.keys():
        process_after(tick, bid)

    bid_list = DURATION.keys()
    ret = []
    for bid in bid_list:
        ret.append((TOTAL[bid], bid))
    ret.sort(key = lambda x : (-x[0], -x[1]))
    # print(ret)
    for i in range(findCnt) :
        bidArr[i] = ret[i][1]
        numResult[i] = ret[i][0]


    # print(ret)
    # for
    # 1. tc 처리
    # 2. 처리 완료 후, list에 각각을 담는다.
    # 3. 리스트에 필요 정보 : 체험관 ID, 고객수 배열 --> 하나로 정렬하고, 값을 나눠서 bid / num에 넣어준다.
    # print(tick)
