import sys
from collections import deque

def find_min_value(min_value, now_node, prev) :
    pre_node = prev[now_node]
    if now_node == 0 :
        return min_value

    possible_capacity = c[pre_node][now_node] - f[pre_node][now_node]
    min_value = min(min_value, possible_capacity)
    return find_min_value(min_value, pre_node, prev)

def update_flow(min_value, now_node, prev) :
    global ans
    pre_node = prev[now_node]
    if now_node == 0 :
        ans +=min_value
        return

    f[pre_node][now_node] += min_value
    f[now_node][pre_node] -= min_value
    update_flow(min_value, pre_node, prev)
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

            # 갈 수 있는 유량이 있고, 한번도 방문한 적이 없으면 간다.
            if c[here][there] - f[here][there] > 0 and prev[there] == -1:
                que.append(there)
                prev[there] = here

    if prev[-1] == -1 :
        return True

    #최소값 찾아서 넣어준다.
    min_value = find_min_value(9876543210, -1, prev)
    update_flow(min_value,-1,prev)
    return False






n,m = map(int,sys.stdin.readline().split())
total_len = n+m+2
# 시작 -> people 유량 설정
f = [[0 for _ in range(total_len)] for _ in range(total_len)]
c = [[0 for _ in range(total_len)] for _ in range(total_len)]

# 시작 -> 사람까지 갈 수 있는 유량 설정 완료
people_node = list(map(int,sys.stdin.readline().split()))
for people_idx, capacity in enumerate(people_node):
    people = 1 + people_idx
    c[0][people] = capacity


#book → -1까지 유량을 정하는 것이다.
book_node = list(map(int,sys.stdin.readline().split()))
for idx, capacity in enumerate(book_node):
    book = n + 1 + idx
    c[book][-1] = capacity


for book_idx in range(m) :
    book = 1 + n + book_idx
    book_node = list(map(int,sys.stdin.readline().split()))

    for people_idx, capacity in enumerate(book_node):
        people = 1 + people_idx
        c[people][book] = capacity


ans = 0

while 1 :
    not_continuable = bfs()
    if not_continuable :
        break

print(ans)