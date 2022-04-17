from typing import List
from collections import defaultdict, deque
from heapq import heappop, heappush, nlargest

global GRAPH, n, CAFENAME, CAFEEXIST, HOMECAFE, HOMECAFESCORE, CAFESCORE, HOMENAMEBYCAFEID


"""
1. 와일드 카드용 딕셔너리 -> List로 선언 : CAFENAME
2. 카페 + 레이지 체크용 딕셔너리 선언  : CAFEEXIST
3. 각 마을별 딕셔너리 형태로 카페가 있는지 확인. : HOMECAFE
4. 각 마을별 우선순위 큐 형태로 카페 최대값을 가진다. : HOMECAFESCORE
5. 지도를 가진다.
6. 카페의 마을 이름
6. 카페별 스코어 : GRAPH
"""


def init(N: int, M: int, mRoads: List[List[int]]) -> None:
    global GRAPH, n, CAFENAME, CAFEEXIST, HOMECAFE, HOMECAFESCORE, CAFESCORE, HOMENAMEBYCAFEID

    n = N
    GRAPH = [[] for _ in range(N+1)]
    for i in range(M) :
        s,e = mRoads[i]
        GRAPH[s].append(e)
        GRAPH[e].append(s)

    CAFENAME = defaultdict(list)
    CAFEEXIST = defaultdict(int)
    HOMECAFE = [defaultdict(int) for _ in range(N+1)]
    HOMECAFESCORE = defaultdict(list)
    CAFESCORE = defaultdict(int)
    HOMENAMEBYCAFEID = defaultdict(int)

def inputWildCard(mName,score):
    global GRAPH, n, CAFENAME, CAFEEXIST, HOMECAFE, HOMECAFESCORE, CAFESCORE, HOMENAMEBYCAFEID


    for i in range(len(mName)) :
        for j in range(i, len(mName)):
            myStr = mName[i:j+1]
            heappush(CAFENAME[myStr], (-score, mName))

def addRestaurant(mCityID: int, mName: str) -> None:
    global GRAPH, n, CAFENAME, CAFEEXIST, HOMECAFE, HOMECAFESCORE, CAFESCORE, HOMENAMEBYCAFEID

    inputWildCard(mName,0)
    CAFEEXIST[mName] = 1
    heappush(HOMECAFESCORE[mCityID], (0, mName))
    HOMECAFE[mCityID][mName] = 1
    CAFESCORE[mName] = 0
    HOMENAMEBYCAFEID[mName] = mCityID


def addValue(mName: str, mScore: int) -> None:
    #카페 평점 추가
    CAFESCORE[mName] += mScore

    #평점 업데이트 되는 input 우선순위 큐 값이 바뀐다.
    inputWildCard(mName, CAFESCORE[mName])

    #마을 카페에 값을 추가한다.
    mCityId = HOMENAMEBYCAFEID[mName]
    heappush(HOMECAFESCORE[mCityId], (-CAFESCORE[mName], mName))

def bestValue(mStr: str) -> int:

    BEST = 0
    while CAFENAME[mStr] :
        score, mName = heappop(CAFENAME[mStr])
        if CAFESCORE[mName] != abs(score) : continue
        BEST = abs(score)
        heappush(CAFENAME[mStr], (score, mName))
        break

    # print(BEST)
    return BEST

def bfs(start, dis) :
    global GRAPH, n, CAFENAME, CAFEEXIST, HOMECAFE, HOMECAFESCORE, CAFESCORE, HOMENAMEBYCAFEID

    V = [0 for _ in range(n+1)]
    que = deque()
    que.append((start,0))

    V[start] = 1
    cafe_list = []

    while que :
        now_city, now_dis = que.popleft()

        cnt = 0
        stack = []
        while HOMECAFESCORE[now_city] and cnt < 3 :
            score, cafe_name = heappop(HOMECAFESCORE[now_city])
            if CAFESCORE[cafe_name] != abs(score) : continue
            cnt += 1
            stack.append((score, cafe_name))

        while stack :
            score, cafe_name = stack.pop()
            heappush(HOMECAFESCORE[now_city], (score, cafe_name))
            cafe_list.append(score)


        next_dis = now_dis + 1
        for next_city in GRAPH[now_city] :
            if next_dis > dis : break
            if V[next_city] == 0 :
                V[next_city] = 1
                que.append((next_city, next_dis))

    return cafe_list





def regionalValue(mCityID: int, mDist: int) -> int:
    ret = bfs(mCityID, mDist)
    ret.sort(reverse=True)
    value = 0
    for i in range(3) :
        if not ret : break
        value += abs(ret.pop())

    return value


"""
1. 와일드 카드용 딕셔너리 -> List로 선언
2. 카페 + 레이지 체크용 딕셔너리 선언 
3. 각 마을별 딕셔너리 형태로 카페가 있는지 확인.
4. 각 마을별 우선순위 큐 형태로 카페 최대값을 가진다. 
5. 지도를 가진다.

카페 이름 중
STR이 포함되어 있는 카페의 가치 중, 가장 높은 가치를 반환한다.
150,000 -> 이게 가장 크다. 카페 이름이 총 3~5개임. 

데이터 셋트 고려
1. 이 경우 총 3번을 살펴봐야함.
2. 각 데이터에는 3333개가 있을 수 있음. -> 
3. 3 * 3333 * 150,000을 해야함. 
이렇게 살펴 볼 경우 15억번이다. 당연히 초과다.
각 문자열을 우선순위 큐로 살펴보자.

1. 와일드 카드를 만든다. 와일드 카드는 우선순위 큐를 가진다. 
2. 우선순위 큐에 값, 카페이름을 넣어둔다. --> 레이지 업데이트가 필요하다.

따라서 레이지 업데이트를 위한 카페이름 default dict도 만든다.
이 default dict에 값을 넣어두고, 우선순위 큐에서 값을 꺼내오고 맞으면 넣고, 아니면 버린다.  

   



"""



"""
N개의 마을, M개의 도로가 있음.
마을 : 최대 50개
도로 : 최대 50개
--> 마을과 마을이 모두 이어질 수 있다. 하나도 안 이어질 수 있다.


도로 정보 :
1. 양방향 통행만 가능 : 그래프 표현 필요

마을 정보 :
2. 연결되지 않은 마을 존재 가능.
3. 마을에는 카페 존재 가능
4. 한 마을에 여러 개 카페 존재 가능.
5. 카페 평점은 0점이 기본.
6. 마을 번호 : 1 ~ N번


카페 정보
1. 카페 평점은 0점이 기본
2. 카페의 가치는 받은 평점의 총합


시작 시, 카페 존재하지 않음.

"""