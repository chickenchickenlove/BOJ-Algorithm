import sys
import math


def propagation(node, left, right):
    if left != right:
        tree[node * 2][1] = tree[node][1]
        tree[node * 2 + 1][1] = tree[node][1]
    tree[node][0] = tree[node][1]
    tree[node][1] = 0

    return


def update(tree, node, left, right, start, end, value):
    if left == right == start or left == right == end:
        if tree[node][1] != 0:
            tree[node][0] = tree[node][1]
            tree[node][1] = 0

        tree[node][0] = value

    else:
        if tree[node][1] != 0:
            propagation(node, left, right)

        if right < start or end < left:
            return

        elif start <= left and right <= end:
            if left != right:
                tree[node * 2][1] = value
                tree[node * 2 + 1][1] = value
            tree[node][0] = value

        else:
            mid = (left + right) // 2

            update(tree, node * 2, left, mid, start, end, value)
            update(tree, node * 2 + 1, mid + 1, right, start, end, value)

            tree[node][0] = tree[node * 2][0] | tree[node * 2 + 1][0]
            return


def query(tree, node, left, right, start, end):
    if left == right == start or left == right == end:
        if tree[node][1] != 0:
            tree[node][0] = tree[node][1]
            tree[node][1] = 0

        return tree[node][0]

    else:
        if tree[node][1] != 0:
            propagation(node, left, right)

        if right < start or end < left:
            return 0

        elif start <= left and right <= end:
            return tree[node][0]

        else:
            mid = (left + right) // 2

            a = query(tree, node * 2, left, mid, start, end)
            b = query(tree, node * 2 + 1, mid + 1, right, start, end)

            tree[node][0] = tree[node * 2][0] | tree[node * 2 + 1][0]

            return a | b


n, t, q = map(int, sys.stdin.readline().split())
h_tree = 2 ** (math.ceil(math.log2(n)) + 1)
# 모든 집은 1번으로 색칠되어있음.
tree = [[1, 0] for _ in range(h_tree)]

for _ in range(q):
    my_list = list(map(str, sys.stdin.readline().split()))
    if my_list[0] == 'C':
        a, b, c, d = my_list
        b, c, d = map(int, (b, c, d))
        # b>c인 경우 있을 수 있음
        if b > c:
            b, c = c, b
        update(tree, 1, 0, n - 1, b - 1, c - 1, 1 << (d - 1))


    else:
        a, b, c, = my_list
        b, c = map(int, (b, c))
        # b>c인 경우 있을 수 있음
        if b > c:
            b, c = c, b

        k = bin(query(tree, 1, 0, n - 1, b - 1, c - 1))
        k = k.split('0b')[1]
        print(k.count('1'))
