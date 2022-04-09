import sys
from heapq import heappop, heappush
from collections import defaultdict


def sell_func(pq, cnt, tofu_dict, flag) :
    answer = 0
    while pq :
        worth = heappop(pq) if flag == 0 else -heappop(pq)
        if not tofu_dict[worth] : continue

        if tofu_dict[worth] >= cnt :
            answer += worth * cnt
            tofu_dict[worth] = tofu_dict[worth] - cnt
            heappush(pq, worth) if flag == 0 else heappush(pq, -worth)
            break
        else :
            answer += worth * tofu_dict[worth]
            cnt -= tofu_dict[worth]
            tofu_dict[worth] = 0
    print(answer)

# sys.stdin = open("input.txt")
input = sys.stdin.readline
tofu_dict = defaultdict(int)

minq = []
maxq = []


for _ in range(int(input().strip())):
    query = list(map(int,input().split()))
    # print(*query)

    if query[0] == 1 :
        worth,cnt = query[1:]
        tofu_dict[worth] += cnt
        heappush(minq, worth)
        heappush(maxq, -worth)
        print(tofu_dict[worth])

    if query[0] == 2:
        worth,cnt = query[1:]
        tofu_dict[worth] = max(0, tofu_dict[worth] - cnt)
        print(tofu_dict[worth])

    if query[0] == 3:
        if query[1] == 0:
            sell_func(minq, query[2], tofu_dict,query[1])
        elif query[1] == 1 :
            sell_func(maxq, query[2], tofu_dict,query[1])



#배열로 관리해야한다. 그런데 int 범위이기 때문에 다 만들면 오류가 발생한다.
#defaultdict로 key만 관리하자.
# 가치가 낮은 순, 높은순 --> 정렬 or 우선순위 큐. 근데 매번 정렬할 수 없다. 우선순위 큐로 한다.
# 우선순위 큐로 했을 때..
# 뽑는다...

# 근데 만약에 판매할 게 없다고 하면 계속 넣는게 맞는 것일까? 아니다.
# 다시 만들 때 넣어주면 되기 때문이다.