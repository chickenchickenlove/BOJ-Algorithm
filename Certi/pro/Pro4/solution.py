from heapq import heappop, heappush
from collections import defaultdict, deque
global hqMin,hqSort , memLoc, memOri


# hq = []

def init(N):
    global hqMin,hqSort, memLoc, memOri
    hqMin = [(N,0)]
    hqSort = [(0,N-1)]
    memLoc = defaultdict(int)
    memOri = defaultdict(int)
    memOri[0] = N

def allocate(size):
    global hqMin,hqSort , memLoc, memOri
    stack = []
    RV = -1
    while hqMin :
        MS,S = heappop(hqMin)
        E = S + MS - 1

        #거짓일 경우 버린다.
        if MS != memOri[S] : continue

        #만족하는 경우
        if MS >= size:
            next_start = S + size
            NS = E - next_start + 1
            heappush(hqMin, (NS, next_start))
            memLoc[S] = size

            heappush(hqSort, (next_start, NS + next_start - 1))
            memOri[S] = 0
            memOri[next_start] = NS

            RV = S
            break
        stack.append((MS,S))
    while stack : heappush(hqMin, stack.pop())

    # print(RV)
    return RV


def mergeHeap():
    global hqMin, hqSort, memLoc, memOri

    stack = deque()
    while hqSort :
        start, end = heappop(hqSort)
        if memLoc[start] != 0 :continue
        if memOri[start] != end - start + 1 : continue
        stack.append((start, end))


    next_stack = []
    while stack :
        S,E = stack.popleft()
        while stack :
            NS, NE = stack[0]
            if E +1 == NS :
                E = NE
                memOri[NS] = 0
                stack.popleft()
            else :
                break
        next_stack.append((S,E))
        memOri[S] = E-S+1


    while next_stack :
        S,E = next_stack.pop()
        SIZE = E-S + 1
        heappush(hqSort, (S,E))
        heappush(hqMin, (SIZE,S))


def deallocate(start):
    global hqMin,hqSort , memLoc, memOri
    if memLoc[start] == 0 :
        # print(-1)
        return -1

    # 여기에 메모리가 있을 경우
    size = memLoc[start]
    end = start + memLoc[start] - 1
    memLoc[start] = 0
    memOri[start] = size

    heappush(hqMin, (size, start))
    heappush(hqSort,(start, end))

    mergeHeap()
    # print(size)
    return size






"""
1. allocate
- 작은 빈 공간 > 앞쪽에 있는 공간 순으로 반환한다. --> Min, 정렬, Heap 등
- 할당 공간이 없는 경우 -1 반환

2. deallocate
- start 값이 시작인 경우만 할당 해제
- 할당해제하면 인접한 빈 공간을 병합한다.
- 불가능할 경우 -1 반환. 

3. 병합
- 하나의 지점이 해제된다. 그러면 양쪽으로 병합 가능성이 생긴다.
- 이 때 병합 한 후에, 연쇄적으로 병합이 될까? -> 그렇지 않다. 
- 따라서, 병합 한 후에 좌/우만 살피면 된다.

4. 데이터 셋 관련
- 모든 함수의 호출 횟수 총합은 30000이다.
- 그럼 살펴봐야 할 모든 노드는 몇개인가?
- allocate만 3만번 할 경우 -> 총 N은 30,000개가 된다.  --> 따라서 O(N^2)으로는 할 수 없다. 
- 시작 / 끝점으로 나누어 관리할 수 있다. 
- 사용중인 경우도 삭제해야한다.


병합 :
병합을 위해서는 사용하지 않는 상태의 처리가 필요하다.
그리고 병합하는 부분은 좌/우의 처음과 끝을 알아야한다.
--> 
1. 사용하지 않는 것들의 시작지점을 나타내는 딕셔너리를 구한다
2. 사용하지 않는 것들의 끝지점을 나타내는 딕셔너리를 구한다.
3. 서로가 서로를 탐색할 수 있도록 가리킨다.
--> 이 경우, 해제된 부분의 좌우를 +-1로 찾아볼 수 있게 된다.
4. 병합하는 과정은 힙으로 처리하자.  

"""
