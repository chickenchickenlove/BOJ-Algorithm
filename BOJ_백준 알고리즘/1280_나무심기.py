import sys
import math


def update(tree, node, start, value):
    node += start
    tree[node][1] += 1
    tree[node][0] = value * tree[node][1]
    node //= 2
    while node:
        tree[node][1] = tree[node * 2][1] + tree[node * 2 + 1][1]
        tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]
        node //= 2
    return


def query(tree, node, left, right, start, end):
    if left == right == start or left == right == end:
        return tree[node]
    elif right < start or end < left:
        return (0, 0)
    elif start <= left and right <= end:
        return tree[node]
    else:
        mid = (left + right) // 2
        a, b = query(tree, node * 2, left, mid, start, end)
        c, d = query(tree, node * 2 + 1, mid + 1, right, start, end)

        return (a + c, b + d)


n = int(sys.stdin.readline().rstrip())
my_list = []
my_set = set()
for _ in range(n):
    a = int(sys.stdin.readline().rstrip())
    my_set.add(a)
    my_list.append(a)

cont = max(my_set) + 1
h_tree = 2 ** math.ceil(math.log2(cont) + 1)
tree = [[0, 0] for _ in range(h_tree)]
answer = 1

for idx in range(len(my_list)):
    k = my_list[idx]
    if idx > 0:
        a, b = query(tree, 1, 0, h_tree // 2 - 1, 0, k - 1)
        c, d = query(tree, 1, 0, h_tree // 2 - 1, k + 1, h_tree // 2 - 1)
        temp = k * b - a + c - k * d
        answer *= temp
        answer %= 1000000007

    update(tree, k, h_tree // 2, k)

print(answer)





