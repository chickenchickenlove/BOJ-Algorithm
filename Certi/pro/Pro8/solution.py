from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop
global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS

class Police(object):

    def __init__(self):
        self.town = 0
        self.eventId = -1
        self.event_time_stamp = -1
        self.event_pri = 0

    def initValue(self):
        self.eventId = -1
        self.event_time_stamp = -1
        self.event_pri = 0

def init(N: int, parent: List[int]) -> None:
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS

    CITY_NUM = N
    CITY = [set() for _ in range(N)]
    for child, parent in enumerate(parent) :
        if child == 0 : continue
        CITY[child].add(parent)
        CITY[parent].add(child)

    TIMESTAMP = 0
    EVENT = []
    EVENTTOWN = defaultdict(int)
    EVENTCHECK = defaultdict(int)
    POLICE = Police()
    ANS = 0

def occur(timeStamp: int, caseID: int, townNum: int, prior: int) -> None:
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
    process(timeStamp)
    heappush(EVENT, (-prior, timeStamp, caseID))
    EVENTTOWN[caseID] = townNum
    EVENTCHECK[caseID] = 1

def cancel(timeStamp: int, caseID: int) -> None:
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
    process(timeStamp)
    EVENTCHECK[caseID] = 0

def position(timeStamp: int) -> int:
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
    process(timeStamp)
    return POLICE.town


def process(timeStamp) :
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
    if POLICE.eventId < 0 and not EVENT:
        TIMESTAMP = timeStamp
        return

    while TIMESTAMP < timeStamp :
        if not EVENT and POLICE.eventId < 0 : TIMESTAMP = timeStamp

        # 진행 중인 사건이 있을 경우, 사건 초기화
        if POLICE.eventId >=0 :
            heappush(EVENT, (POLICE.event_pri, POLICE.event_time_stamp, POLICE.eventId))
            POLICE.initValue()

        #목표 사건 탐색
        target_event = []
        while EVENT :
            prior, start_time, caseID = heappop(EVENT)
            if EVENTCHECK[caseID] :
                target_event.append((prior, start_time, caseID))
                break

        if target_event :
            POLICE.event_pri, POLICE.event_time_stamp, POLICE.eventId = target_event.pop()
            start_time = POLICE.event_time_stamp

            if start_time > TIMESTAMP :
                TIMESTAMP = start_time

            #BFS를 해서 이동할 수 있는 곳 까지 이동한다.
            bfs(timeStamp, TIMESTAMP)


        if POLICE.eventId >= 0 and EVENTTOWN[POLICE.eventId] == POLICE.town and TIMESTAMP + 1 <= timeStamp:
            POLICE.initValue()
            TIMESTAMP +=1
            continue


        # 현재 위치가
def bfs(end_time, startTime):
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS

    limit_time = end_time
    que = deque()
    V = [-1 for _ in range(CITY_NUM+1)]
    T = [0 for _ in range(CITY_NUM+1)]
    que.append((POLICE.town, startTime ))

    while que :
        now_city, time = que.popleft()
        next_time = time + 1
        if now_city == EVENTTOWN[POLICE.eventId] : break
        for next_city in CITY[now_city] :
            if V[next_city] == -1:
                que.append((next_city, next_time))
                V[next_city] = now_city
                T[next_city] = next_time

    town = EVENTTOWN[POLICE.eventId]
    while V[town] != - 1 :
        if town == POLICE.town : break
        if T[town] <= limit_time :
            TIMESTAMP = T[town]
            POLICE.town = town
            break
        town = V[town]