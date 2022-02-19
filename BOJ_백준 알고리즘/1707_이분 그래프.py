import sys
from collections import deque

def getNextValue(value):
    if value == 1 :
        return 2
    if value == 2 :
        return 1

# 반복문으로 돌려야함.
# group이 없는 경우만 들어온다.
# 시작하는 group은 1 , 받는 그룹은 2다.
def sol(start_node):
    que = deque()
    que.append((start_node, 1))
    node_group[start_node] = 1

    while que :
        now_node, now_group = que.popleft()

        for next_node in node[now_node]:

            # 다음 방문할 노드가 같은 로드라면 볼 필요도 없다. 이건 Fail임.
            if node_group[next_node] == now_group:
                return False

            if node_group[next_node] == 0 :
                next_value = getNextValue(now_group)
                node_group[next_node] = next_value
                que.append((next_node,next_value))

    return True



k = int(sys.stdin.readline().rstrip())
for _ in range(k) :
    v,e = map(int,sys.stdin.readline().split())
    # v + 1 개 노드 만듬
    node = [[] for _ in range(v+1)]

    # 0이 아니면 방문 처리 하는 것임.
    node_group = [0 for _ in range(v+1)]

    for _ in range(e) :
        a,b = map(int,sys.stdin.readline().split())
        node[a].append(b)
        node[b].append(a)


    yes_flag = True
    for start_node in range(1,v+1):
        if node_group[start_node] == 0:
            yes_flag = sol(start_node)
        if not yes_flag:
            break
    if yes_flag :
        print("YES")
    else:
        print("NO")








