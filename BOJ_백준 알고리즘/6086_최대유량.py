import sys
from collections import deque


def find_min(node, prev, min_value):
    pre_node = prev[node]

    if node == d["A"]:
        return min_value
    min_value = min(min_value, my_list[pre_node][node] - f[pre_node][node])
    return find_min(pre_node, prev, min_value)


def update(node, prev, min_value):
    global ans
    pre_node = prev[node]
    if node == 26:
        ans += min_value
        return
    f[pre_node][node] += min_value
    f[node][pre_node] -= min_value
    update(pre_node, prev, min_value)


def bfs2(my_list, d):
    global my_str, ans
    que = deque()
    prev = [-1 for _ in range(len(my_str))]
    prev[26] =26
    for node, value in enumerate(my_list[d["A"]]):
        if value != 0:
            if my_list[26][node] - f[26][node] > 0:
                prev[node] = 26
                que.append(node)
    while que:
        now_node = que.popleft()

        if now_node == d["Z"]:
            break
        for next_node, value in enumerate(my_list[now_node]):
            flow = f[now_node][next_node]

            if my_list[now_node][next_node] > flow and prev[next_node] == -1 and my_list[now_node][next_node] != 0:
                que.append(next_node)
                prev[next_node] = now_node
    if prev[-1] == -1:
        return False
    min_value = find_min(len(prev) - 1, prev, 9876543210)
    update(len(prev) - 1, prev, min_value)
    return True


def bfs(my_list, d):
    while 1:
        trueFalse = bfs2(my_list, d)
        if not trueFalse:
            break
    return


my_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
d = {}
for idx, value in enumerate(my_str):
    d[value] = idx

n = int(sys.stdin.readline().rstrip())
my_list = [[0 for _ in range(len(my_str))] for _ in range(len(my_str))]
f = [[0 for _ in range(len(my_str))] for _ in range(len(my_str))]
for _ in range(n):
    q, w, e = sys.stdin.readline().split()
    Q, W = d[q], d[w]
    my_list[Q][W] += int(e)
    my_list[W][Q] += int(e)


ans = 0
bfs(my_list, d)
print(ans)