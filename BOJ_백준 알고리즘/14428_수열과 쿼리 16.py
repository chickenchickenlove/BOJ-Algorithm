import sys
import math


def init_tree(tree, node, left, right,my_list ) :
    if left == right :
        tree[node] = my_list[left]
        tree2[node] = left
        return
    else :
        mid = (left + right) // 2
        init_tree(tree, node*2, left, mid, my_list)
        init_tree(tree, node * 2 + 1 , mid+1, right, my_list)
        tree[node] = min(tree[node*2] , tree[node*2 + 1 ])
        if tree[node * 2 ] <= tree[node * 2 +1 ] :
            tree2[node] = tree2[node*2]
        else :
            tree2[node] = tree2[node*2 + 1]
        return


def modify(tree, node, left, right, idx, value) :
    if idx == left == right :
        tree[node] = value
        tree2[node] = left
        return
    elif idx < left or right < idx :
        return
    else :
        mid = (left + right) // 2
        modify(tree, node*2, left, mid, idx, value)
        modify(tree, node * 2 + 1, mid + 1 , right, idx, value)
        tree[node] = min(tree[node*2] , tree[node*2 + 1 ])
        if tree[node * 2 ] <= tree[node * 2 +1 ] :
            tree2[node] = tree2[node*2]
        else :
            tree2[node] = tree2[node*2 + 1]
        return


def query(tree2, node, left, right, start, end,tree) :
    if right < start or end < left :
        return (9876543210, 9876543210)
    elif start <= left and right <= end :
        return (tree[node], tree2[node])
    else :
        mid = (left + right) // 2

        a, a_idx = query(tree2, node * 2, left, mid, start, end, tree)
        b, b_idx = query(tree2, node*2 + 1, mid + 1 , right, start, end,tree)

        if a <= b :
            return (a, a_idx)
        else :
            return (b, b_idx)








n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))

if math.log2(n) == n**0.5 :
    h_tree = n * 2
else :
    h_tree =      2** (int(math.log2(n) + 1) + 1 )

tree = [9876543210 for _ in range(h_tree)]
tree2 = [9876543210 for _ in range(h_tree)]
init_tree(tree, 1, 0, n-1, my_list)


for _ in range(int(sys.stdin.readline().rstrip())) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1 :
        modify(tree,1,0,n-1,b-1,c)

    elif a == 2 :
        q,w = query(tree2,1,0,n-1,b-1,c-1,tree)
        print(w +1 )


