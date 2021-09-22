import sys
import math
sys.setrecursionlimit(100000)


def propagtation(tree, node, left, right) :
    if left != right :
        tree[node*2][1] += tree[node][1]
        tree[node*2 + 1][1] += tree[node][1]
    tree[node][0] += (right - left + 1 ) * tree[node][1]
    tree[node][1] = 0
    return



def init(tree, node, left, right) :
    if left == right :
        tree[node][0] = my_list[left]
        return tree[node][0]
    else :
        mid = (left + right) // 2
        init(tree, node*2, left, mid)
        init(tree, node*2+1, mid+1, right)
        tree[node][0] = tree[node*2][0] + tree[node*2 + 1 ][0]
        return tree[node][0]


def update(tree, node, left, right, start, end, value) :
    if left == right == start or left == right == end :
        if tree[node][1] != 0 :
            tree[node][0] += tree[node][1]
            tree[node][1] = 0
        tree[node][0] += value
    else :
        if tree[node][1] != 0 :
            propagtation(tree, node, left, right)

        if right < start or end < left :
            return

        elif start <= left and right <= end :
            tree[node][0] += (right - left + 1) * value
            if left != right :
                tree[node*2][1] += value
                tree[node*2+1][1] += value
            return

        else :
            mid = (left + right) // 2
            update(tree, node*2 , left, mid, start, end,value)
            update(tree, node*2 +1, mid + 1 , right, start, end,value)
            tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
            return


def query(tree, node, left, right, start, end):
    if left == right == start or left == right == end:
        if tree[node][1] != 0:
            tree[node][0] += tree[node][1]
            tree[node][1] = 0
        return tree[node][0]
    else:
        if tree[node][1] != 0:
            propagtation(tree, node, left, right)

        if right < start or end < left:
            return 0

        elif start <= left and right <= end:
            return tree[node][0]

        else:
            mid = (left + right) // 2
            a = query(tree, node * 2, left, mid, start, end)
            b = query(tree, node * 2 +1, mid + 1, right, start, end)
            tree[node][0] = tree[node * 2][0] + tree[node * 2 + 1][0]

            return a + b


n, q1, q2 = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))

h_tree = 2**(math.ceil(math.log2(n))+1)
tree = [[0,0] for _ in range(h_tree)]
init(tree, 1, 0, n-1)
for _ in range(q1+q2) :
    q = list(map(int,sys.stdin.readline().split()))

    if len(q) == 3 :
        if q[1] > q[2]:
            q[1], q[2] = q[2], q[1]
        print(query(tree,1,0,n-1,q[1]-1,q[2]-1))


    else :

        if q[1] > q[2] :
            q[1],q[2] = q[2],q[1]
        update(tree,1,0,n-1,q[1]-1,q[2]-1,q[3])
