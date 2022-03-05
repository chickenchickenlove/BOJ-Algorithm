import sys
from collections import deque

def find_min_value(min_value, now_node, prev) :
    pre_node = prev[now_node]
    if pre_node == 0 :
        return min_value

    possible_capacity = c[pre_node][now_node] - f[pre_node][now_node]
    min_value = min(min_value, possible_capacity)
    return find_min_value(min_value, pre_node, prev)

def update_flow(min_value, now_node, prev) :
    global ans
    pre_node = prev[now_node]
    if now_node == 0 :
        ans +=1
        return

    f[pre_node][now_node] += min_value
    f[now_node][pre_node] -= min_value
    update_flow(min_value, pre_node, prev)
    return



def bfs() :
    global n,d
    # 초기화
    que = deque()
    prev = [-1 for _ in range(n+d+2)]
    que.append(0)


    while que :
        here = que.popleft()

        if here == n+d+1 :
            break

        for there in range(n+d+2) :

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






n,k,d = map(int,sys.stdin.readline().split())

# 시작 -> people 유량 설정
f = [[0 for _ in range(n+d+2)] for _ in range(n+d+2)]
c = [[0 for _ in range(n+d+2)] for _ in range(n+d+2)]
for people in range(1,n+1) :
    c[0][people] = k

#food → -1까지 유량을 정하는 것이다.
food_node = list(map(int,sys.stdin.readline().split()))
for idx, capacity in enumerate(food_node):
    food = n + 1 + idx
    c[food][-1] = capacity

#people -> food 설정
for people in range(1,n+1) :
    nothing, *food_path = map(int,sys.stdin.readline().split())
    for food_idx in food_path:
        food = n + food_idx
        c[people][food] = 1

ans = 0

while 1 :
    not_continuable = bfs()
    if not_continuable :
        break

print(ans)