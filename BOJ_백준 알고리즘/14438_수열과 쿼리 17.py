import sys
import math


def init_tree(tree, node, left, right,my_list ) :
    if left == right :
        tree[node] = my_list[left]
        return
    else :
        mid = (left + right) // 2
        init_tree(tree, node*2, left, mid, my_list)
        init_tree(tree, node * 2 + 1 , mid+1, right, my_list)
        tree[node] = min(tree[node*2] , tree[node*2 + 1 ])
        return


def modify(tree, node, left, right, idx, value) :
    if idx == left == right :
        tree[node] = value
        return
    elif idx < left or right < idx :
        return
    else :
        mid = (left + right) // 2
        modify(tree, node*2, left, mid, idx, value)
        modify(tree, node * 2 + 1, mid + 1 , right, idx, value)
        tree[node] = min(tree[node*2] , tree[node*2 + 1 ])
        return


def query(tree, node, left, right, start, end) :
    if right < start or end < left :
        return 9876543210
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
        a = query(tree, node*2, left, mid, start, end)
        b = query(tree, node*2 + 1, mid + 1 , right, start, end)
        return min(a,b)



n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))

if math.log2(n) == n**0.5 :
    h_tree = n * 2
else :
    h_tree =      2** (int(math.log2(n) + 1) + 1 )

tree = [9876543210 for _ in range(h_tree)]
init_tree(tree, 1, 0, n-1, my_list)


for _ in range(int(sys.stdin.readline().rstrip())) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1 :
        modify(tree,1,0,n-1,b-1,c)

    elif a == 2 :
        print(query(tree,1,0,n-1,b-1,c-1))

