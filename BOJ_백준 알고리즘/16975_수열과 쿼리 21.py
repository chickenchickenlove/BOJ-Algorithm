import sys
import math


def propagation(tree, node, left, right):
    if left != right:
        tree[node * 2][1] += tree[node][1]
        tree[node * 2 + 1][1] += tree[node][1]

    # 현재 노드에 업데이트 해주고
    tree[node][0] += tree[node][1] * (right - left + 1)

    # 현재 lazy를 없애준다.
    tree[node][1] = 0
    return


def init(tree, node, left, right):
    if left == right:
        tree[node][0] = my_list[left]
        return tree[node][0]
    else:
        mid = (left + right) // 2
        tree[node][0] = init(tree, node * 2, left, mid) + init(tree, node * 2 + 1, mid + 1, right)
        return tree[node][0]


def modify(tree, node, left, right, start, end, value):
    # 마지막 노드라면, lazy 계산.
    # 현재 노드의 값을 더한다.
    if left == right and left == start:
        if tree[node][1] != 0:
            tree[node][0] += tree[node][1]
            tree[node][1] = 0

        tree[node][0] += value
        return tree[node][0]

    else:
        if tree[node][1] != 0:
            propagation(tree, node, left, right)

        if start <= left and right <= end:
            tree[node][0] += (right - left + 1) * value

            #이게 굉장히 중요한 것 같음.
            if left != right :
                tree[node * 2][1] += value
                tree[node * 2 + 1][1] += value
            return tree[node][0]

        elif right < start or end < left:
            return tree[node][0]

        else:
            mid = (left + right) // 2
            a = modify(tree, node * 2, left, mid, start, end, value)
            b = modify(tree, node * 2 + 1, mid + 1, right, start, end, value)
            tree[node][0] = a + b
            return tree[node][0]


def query(tree, node, left, right, start, end):
    # 잎새 노드일 때
    if left == right and left == start:
        if tree[node][1] != 0:
            tree[node][0] += tree[node][1]
            tree[node][1] = 0
        return tree[node][0]

    # 구간에 딱 들어올 때
    else:
        if tree[node][1] != 0:
            propagation(tree, node, left, right)

        if start <= left and right <= end:
            return tree[node][0]

        # 구간에 포함되지 않을 때
        elif right < start or end < left:
            return 0

        # 애매하게 구간에 포함되었을 때
        else:
            mid = (left + right) // 2
            a = query(tree, node * 2, left, mid, start, end)
            b = query(tree, node * 2 + 1, mid + 1, right, start, end)
            tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]
            return a + b


n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())


h_tree = 2 ** (math.ceil(math.log2(n)) + 1)

tree = [[0, 0] for _ in range(h_tree)]
init(tree, 1, 0, n - 1)

for _ in range(m ):
    query_list = list(map(int, sys.stdin.readline().split()))
    if len(query_list) == 2:
        a, b = query_list
        print(query(tree, 1, 0, n - 1, b - 1, b - 1))

    else:
        # find
        a, b, c, d = query_list
        if b > c:
            b, c = c, b
        modify(tree, 1, 0, n - 1, b - 1, c - 1, d)


