import sys
from collections import deque

def find_min_value(min_value, now_node, prev, max_price, min_price) :
    global ans, total_len
    pre_node = prev[now_node]
    if now_node == 0 :
        ans -= max_price * min_value
        ans += min_price * min_value
        return min_value, min_price, max_price

    possible_capacity = c[pre_node][now_node] - f[pre_node][now_node]
    min_value = min(min_value, possible_capacity)
    min_price = min(min_price, p[pre_node][now_node])
    max_price = max(max_price, p[pre_node][now_node])
    return find_min_value(min_value, pre_node, prev, max_price, min_price)

def update_flow(min_value, now_node, prev, min_price, max_price) :
    global ans
    pre_node = prev[now_node]
    if now_node == 0 :
        ans +=min_value
        return

    f[pre_node][now_node] += min_value
    f[now_node][pre_node] -= min_value
    pf[pre_node][now_node] += min_value * min_price
    pf[pre_node][now_node] -= min_value * max_price


    update_flow(min_value, pre_node, prev, min_price, max_price)
    return



def bfs() :
    global n,m, total_len
    # 초기화
    que = deque()
    prev = [-1 for _ in range(total_len)]
    que.append(0)


    while que :
        here = que.popleft()

        if here == total_len - 1 :
            break

        for there in range(total_len) :

            next_cost = (c[here][there] - f[here][there]) * p[here][there]
            # 갈 수 있는 유량이 있고, 한번도 방문한 적이 없으면 간다.
            if c[here][there] - f[here][there] > 0 and prev[there] == -1 and pf[here][there] > next_cost:
                que.append(there)
                prev[there] = here

    if prev[-1] == -1 :
        return True

    #최소값 찾아서 넣어준다.
    min_value, min_price, max_price = find_min_value(9876543210, -1, prev, 0, 9876543210)
    update_flow(min_value,-1,prev, min_price, max_price)
    return False






n,m = map(int,sys.stdin.readline().split())
total_len = n+m+2
# 시작 -> people 유량 설정
f = [[0 for _ in range(total_len)] for _ in range(total_len)]
c = [[0 for _ in range(total_len)] for _ in range(total_len)]
p = [[0 for _ in range(total_len)] for _ in range(total_len)]
pf = [[0 for _ in range(total_len)] for _ in range(total_len)]

# 시작 -> 사람까지 갈 수 있는 유량 설정 완료
people_node = list(map(int,sys.stdin.readline().split()))
for people_idx, capacity in enumerate(people_node):
    people = 1 + people_idx
    c[0][people] = capacity
    for book in range(n+1, total_len -1) :
        c[people][book] = capacity


#book → -1까지 유량을 정하는 것이다.
book_node = list(map(int,sys.stdin.readline().split()))
for idx, capacity in enumerate(book_node):
    book = n + 1 + idx
    c[book][-1] = capacity
    p[book][-1] = 0


for book_idx in range(m) :
    book = 1 + n + book_idx
    price_node = list(map(int,sys.stdin.readline().split()))

    for people_idx, price in enumerate(price_node):
        people = 1 + people_idx
        p[people][book] = price
        p[book][people] = price

for ppp in p :
    print(ppp)


ans = 0

while 1 :
    not_continuable = bfs()
    if not_continuable :
        break

print(ans)