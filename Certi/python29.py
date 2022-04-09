import sys
from collections import deque

def bfs(s,e) :
    global n
    v = [0 for _ in range(n)]
    que = deque([s])
    v[s] = 1
    while que :
        node = que.popleft()
        if node == e : return True
        for next_node in graph[node]:
            if v[next_node]  : continue
            v[next_node] = 1
            prev[next_node] = node
            que.append(next_node)

    return False

# sys.stdin = open("input.txt")

n,k = map(int,sys.stdin.readline().split())
num_list = []
for _ in range(n) :
    num = sys.stdin.readline().rstrip()
    num_list.append(num)

graph = [[] for _ in range(n)]

for i in range(len(num_list)):
    here_value = num_list[i]
    for j in range(i+1, len(num_list)):
        there_value = num_list[j]
        diff = 0
        for q in range(len(here_value)) :
            if here_value[q] != there_value[q] : diff +=1
        if diff == 1 :
            graph[i].append(j)
            graph[j].append(i)


s,e = map(int,sys.stdin.readline().split())
s,e = s-1,e-1

prev = [-1 for _ in range(n)]
if not bfs(s,e) :
    print(-1)
else :
    node = e
    answer_list = []
    while node != -1 :
        answer_list.append(str(node+1))
        node = prev[node]
    print(' '.join(map(str,answer_list[::-1])))



