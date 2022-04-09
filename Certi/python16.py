import sys
import heapq as hq


# sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input().rstrip())
nq = []
pq = []
key = int(input().rstrip())
print(key)
for idx in range((n-1)//2) :


    a,b = map(int,input().split())

    hq.heappush(nq, -a) if a < key else hq.heappush(pq,a)
    hq.heappush(nq, -b) if b < key else hq.heappush(pq,b)

    while len(nq) != len(pq) :
        if len(nq) > len(pq) :
            hq.heappush(pq,key)
            key = -hq.heappop(nq)
        elif len(nq) < len(pq) :
            hq.heappush(nq, -key)
            key = hq.heappop(pq)
    print(key)







# 값을 꺼낸다.
# 중앙값은 중앙에 있는 값이다.
# 1. 정렬을 통해 접근한다.
# 정렬은 한번에 nlogn이다 --> 1 ~ 100,000이기 때문에 매번 정렬하면 N^2 Logn^2이 되어서 시간 복잡도 초과가 발생한다.
# 따라서 안된다.
# 2. 3개만 관리하면 될 거 같음.
# 1,2,5 ->
# 1,2,5 --> 1,2,4,5,7 --> 1,4,7
# 이전 정보가 반드시 필요할까? -> 필요없다. 왜냐하면
# 중앙값을 판단할 때는 처음부터 끝까지 다 줄을 세워야 할까?
# 5
# 1,2,5 --> 2가 된다.
# 10,10
# 1,2,5,10,10  --> 5
# 2,5,10 -> 10,10 --> 1,2,5,10,10,10,10, -> 따라서 2번 방식은 논리적으로 오류가 발생한다.
# 3. 가운데인 값들은 항상 바뀐다. 왼쪽 / 오른쪽에 어떤 값이 추가되느냐에 따라 가운데의 값이 바뀌게 된다.
# 5 = 1 -->
# 1,2가 들어왔다. 5 = +2가 된다.
# 1,2,5 --> 2번이 된다. (총 3개 중에 가운데) --> 2 = 2이 된다.
# 1,2,5,10,10 --> 총 길이는 5가 되고, 3인 녀석을 찾아야 한다.  2 + 1 인 녀석을 찾아야 한다.
# 1,2,5,10,10,-30000,-30000 --> 총 길이는 7이 되고, 4인 녀석을 찾아야 한다.
# 즉, 각각 1,2,3,4를 찾아야 한다. 점점 올라가는 형식이다.
# 자료 형 : deque, list, hq
# deque : 가운데에 있는 것을 넣을 방법이 없다.
# list : 안 쓰는게 낫다.
# hq : 우선순위에 따라 배열이 되긴 하다. n개가 있을 때, nlogn + n --> nlogn

# 1,2,3,4,5,6를 각각 Heap에서 빼고 stack에 집어 넣는 방식으로 처리를 했다 --> 시간초과가 발생함.
# 그래서 현재 중앙값을 기준으로 최소힙, 최대힙을 관리함.



