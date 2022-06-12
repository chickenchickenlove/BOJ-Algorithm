import sys
from collections import deque


def sol(path, node_list, v, end ) :
    que = deque()
    d = [0 for _ in range(len(path) + 1 )]


    for node in range(len(node_list)) :
        if node_list[node] == 0 :
            que.append(node)
            d[node] = v[node]


    while que :
        now_node = que.popleft()


        # 현재 노드에서 갈 수 있는 노드 제거
        # 노드 제거 후, 값이 0인 값을 찾음
        # 0인 값을 찾은 후, que에 넣어준다.
        # d[next_node] = max(d[next_node], d[now_node] + v[now_node]

        for next_node in path[now_node] :
            node_list[next_node] -=1
            d[next_node] = max( d[next_node], d[now_node] + v[next_node])

            if node_list[next_node] == 0 :
                que.append(next_node)

    return d[end]



t = int(sys.stdin.readline().rstrip())
for _ in range(t) :

    # 입력 받기
    n, k = map(int,sys.stdin.readline().split())
    v = [0 for _ in range(n+1)]

    my_list = list(map(int,sys.stdin.readline().split()))
    node_list = [0 for _ in range(n+1)]
    node_list[0] = 1
    path = [[] for _ in range(n+1)]

    for i in range(len(my_list)) :
        v[i+1] = my_list[i]

    for _ in range(k) :
        a,b = map(int,sys.stdin.readline().split())
        path[a].append(b)
        node_list[b] +=1

    end = int(sys.stdin.readline().rstrip())

    print(sol(path, node_list, v, end))