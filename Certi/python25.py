import sys

def dfs(node,cnt) :
    if not child_list[node] : return cnt
    return_value = 0
    for next_node in child_list[node] :
        return_value = max(dfs(next_node, cnt+1), return_value)
    return return_value

def dfs_up(node) :
    cnt = 0
    while node :
        cnt += 1
        node = parent_list[node]
    return cnt

def dfs_parent(x,y) :
    while 1 :
        if y == x : return 1
        if y == 0 : return 0
        y = parent_list[y]

def remove_func(child) :

    if child == 0 or parent_list[child] == -1: return
    parent = parent_list[child]
    child_list[parent].remove(child)

    for next_child in child_list[child] :
        child_list[parent].add(next_child)
        parent_list[next_child] = parent
    child_list[child].clear()
    parent_list[child] = -1

def query_func(node) :
    a = dfs_up(node)
    b = dfs(node,0)
    print(a,b)


def move_func(x, y) :
    if x == y or x == 0 or parent_list[x] == -1 or parent_list[y] == -1: return
    if dfs_parent(x,y) : return

    child_list[parent_list[x]].remove(x)
    child_list[y].add(x)
    parent_list[x] = y

# sys.stdin = open("input.txt")
input = sys.stdin.readline

k = 10001
child_list = [set() for _ in range(k)]
parent_list = [-1 for _ in range(k)]
parent_list[0] = 0



for _ in range(int(input().strip())):
    query = list(map(str,input().split()))

    if query[0] == "add":
        child, parent = map(int,query[1:])
        child_list[parent].add(child)
        parent_list[child] = parent

    elif query[0] == "remove":
        child = int(query[1])
        remove_func(child)

    elif query[0] == "query":
        node = int(query[1])
        query_func(node)

    elif query[0] == "move":
        child, parent = map(int, query[1:])
        if child == parent or parent_list[child] == -1 or parent_list[parent] == -1: continue
        move_func(child,parent)

