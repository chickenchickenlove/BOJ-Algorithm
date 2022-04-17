''' solution.py '''
from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop
global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
"""
경찰 
> 1명만 존재
> 정해진 규칙으로 트리를 돌아다님

트리(트리니 사이클을 고려하지 않음)
> N개의 마을, N-1개의 도로가 있음.
> 마을번호 : 0 ~ N-1
> 0번은 부모 마을
> 나머지 마을은 모두 부모 마을 하나 가짐. 
    -> 연결되어있음.


도로
> 양방향 통행 가능
> 가중치 동일함.
> 두 마을 사이에는 단 하나의 도로만 존재함. 


타임 스탬프
> 타임 스탬프의 초기값은 0임.
> 타임 스태프 1 증가 -> 1시간 증가

사건
1. 발생 시각
2. 고유 번호
3. 발생 마을 번호
4. 처리 우선순위
5. 취소 가능함(******)

목표 사건 -> 사건을 관리할 필요가 있음. 
- 남아있는 사건 중, 가장 우선순위가 높은 사건
- 남아있는 사건 = 처리 되지 않은 사건 + 취소되지 않은 사건.
- 우선순위
    > 우선순위
    > 발생 시각이 가장 빠른 것부터 처리
    
설명
1. 경찰은 0초에 0번 마을에 위치
2. 경찰의 마을 이동 시간은 1임.
3. 목표 사건 마을에 1시간 체류하면 목표 사건이 해결됨. 해당 목표 사건만 처리 됨(해당 마을의 모든 사건이 처리는 X)

경찰의 행동 방식
1. 타임스탬프 시간에 발생 / 취소되 사건에 대한 정보를 확인. 정보는 잊어버리지 않음. -> 정보를 기록해둔다.
2. 목표 사건을 찾는다. 
3. 목표 사건이 없으면, 현재 위치에서 1시간 대기한다.
4. 목표 사건이 & 동일 위치 > 현재 위치에서 1시간 동안 사건 해결한다.
5. 목표 사건이 & 다른 위치 > 1시간동안 해당 위치를 향해 최단 경로로 이동한다 

*** 매 시간, 매 목표 사건을 새롭게 찾는다. 즉, 1시간마다 목표 사건이 바뀔 수 있음. 
# input
1. 마을개수 : 350
2. TimeStampe : 5,000,000 -> 작기 때문에 1초마다 움직여야한다. 

"""



"""
1. 마을 리스트가 주어진다.
2. 존재하는 사건은 없다.
3. 경찰은 0번 마을에 있다. 

"""


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



"""
최대 호출 : 100,000
timestamp 시간에, townNum 마을에
사건 번호가 caseId인 우선순위가 prior인 사건이 만들어진다. 
사건 리스팅 하는 배열 필요.
> 우선순위
> 발생 시각이 가장 빠른 것부터 처리 
"""
def occur(timeStamp: int, caseID: int, townNum: int, prior: int) -> None:
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
    process(timeStamp)
    heappush(EVENT, (-prior, timeStamp, caseID))
    EVENTTOWN[caseID] = townNum
    EVENTCHECK[caseID] = 1



"""
최대 호출 : 50,000
timestamp 시간에 casdId번 사건을 취소함.
사건이 유효한지를 관리하는 배열 필요. 

"""
def cancel(timeStamp: int, caseID: int) -> None:
    global CITY, TIMESTAMP, EVENT, EVENTCHECK, POLICE, EVENTTOWN, CITY_NUM, ANS
    process(timeStamp)
    EVENTCHECK[caseID] = 0


"""
최대 호출 : 100,000
timeStamp 시각에 경찰이 위치한 마을 번호를 반환.
BFS로 돌린다. 따라서 350번을 한다.

"""


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










"""
시간을 흘려줘야한다.
흘려줘서 경찰이 사건을 처리하고, 또 넘어가고 하는 로직이 필요하다.

1. 목표 사건을 확인한다. (사건 확인 시, 유효한 사건이 아닐 경우 버린다)
2. 현재 위치 목표 사건이라면, time Stamp + 1을 하고 사건을 버려준다. 
3. 목표 사건이 다른 곳이라면 BFS로 Time Stamp 전까지 이동한다. 
    이 때 BFS는 이전 위치를 기록을 해두고, 그 위치를 따라서 실제로 이동한다.
    이동해서 사건을 처리하는 동안 시간을 보내고 비운다.
4. 목표 시간을 확인하고 목표 사건을 확인한다. 




"""

''' main.py '''
import sys
from typing import List

INIT = 1
OCCUR = 2
CANCEL = 3
POSITION = 4


def run():
    queryCnt = int(sys.stdin.readline())
    isCorrect = False

    for i in range(queryCnt):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == INIT:
            N = int(next(inputs))
            parent = [int(next(inputs)) for _ in range(N)]
            init(N, parent)
            isCorrect = True

        elif cmd == OCCUR:
            timeStamp = int(next(inputs))
            caseID = int(next(inputs))
            townNum = int(next(inputs))
            prior = int(next(inputs))
            occur(timeStamp, caseID, townNum, prior)

        elif cmd == CANCEL:
            timeStamp = int(next(inputs))
            caseID = int(next(inputs))
            cancel(timeStamp, caseID)

        elif cmd == POSITION:
            timeStamp = int(next((inputs)))
            userAns = position(timeStamp)
            ans = int(next(inputs))

            # print(f'index : {i}, userAns = {userAns}, ans = {ans}')
            if userAns != ans:
                isCorrect = False

        else:
            isCorrect = False

    return isCorrect


if __name__ == '__main__':
    # sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    SUCCESS = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = SUCCESS if run() else 0
        print("#%d %d" % (testcase, score), flush=True)