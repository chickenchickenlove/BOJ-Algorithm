import sys
sys.setrecursionlimit(100000)


def dfs(node) :
    global d_node,ans,v

    if len(tree[node]) == 0 :
        ans +=1
        return
    else :
        for next_node in tree[node] :
            if next_node == d_node :
                if len(tree[node]) == 1  :
                    ans +=1
                continue
            else :
                if v[next_node] == 0 :
                    v[next_node] = 1
                    dfs(next_node)


    # 현재 노드가 마지막 노드면 하나 추가한다
    # 현재 노드가 dnode면 더 탐색하지 않는다.


n = int(sys.stdin.readline().rstrip())
tree = [[] for _ in range(n)]
temp = list(map(int,sys.stdin.readline().split()))

for idx, value in enumerate(temp) :
    if value != -1 :
        tree[value].append(idx)
    else :
        sr = idx
v = [0 for _ in range(n)]
ans = 0
d_node = int(sys.stdin.readline().rstrip())
if sr != d_node :
    dfs(sr)
print(ans)
