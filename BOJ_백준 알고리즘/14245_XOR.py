import sys
import math


def propagation(node, left, right) :
    if left != right :
        lazy[node*2] ^= lazy[node]
        lazy[node*2+1] ^= lazy[node]
    else :
        tree[node] ^= lazy[node]

    lazy[node] = 0
    return


    #1. 현재 노드 lazy 있는지 확인한다.
    #2. 있으면 자식 노드로 내려준다.
    #3. 내려주면서 XOR 연산을 해준다.


def init(tree, node, left, right) :
    if left == right :
        tree[node] = my_list[left]
        return
    else :
        mid = (left + right)//2
        init(tree, node*2, left, mid)
        init(tree, node * 2+1, mid+1, right)
        return


def update(tree, node, left, right, start, end, value) :
    if left == right == start or left == right == end :
        if lazy[node] != 0 :
            tree[node] ^= lazy[node]
            lazy[node] = 0
        tree[node] ^= value
        return
    else :
        #lazy를 물려준다.

        if right < start or end < left :
            return
        else :
            if lazy[node] != 0:
                propagation(node, left, right)

            if start <= left and right <= end :
                lazy[node] = value
                return
            else :
                mid = (left + right) // 2
                update(tree, node*2, left, mid, start, end, value)
                update(tree, node*2+1, mid+1, right, start, end, value)
                return


def query(tree, node, left, right, idx) :
    if left == right == idx :
        if lazy[node] != 0:
            tree[node] ^= lazy[node]
            lazy[node] = 0

        return tree[node]
    else :
        if lazy[node] != 0 :
            propagation(node, left, right)

        if idx < left or right < idx :
            return 0
        else :
            mid = (left + right) // 2
            a = query(tree, node*2, left, mid, idx)
            b = query(tree, node*2+1, mid+1, right, idx)
            return a^b



n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
h_tree = 2**(math.ceil(math.log2(n))+1)
tree = [0 for _ in range(h_tree)]
lazy = [0 for _ in range(h_tree)]
init(tree, 1, 0, n-1)

m = int(sys.stdin.readline().rstrip())
for _ in range(m) :
    q = list(map(int,sys.stdin.readline().split()))
    if q[0] == 1 :
        a,b,c,d = q
        update(tree, 1,0,n-1,b,c,d)
        #print(tree)
    else :
        a,b = q
        print(query(tree,1,0,n-1,b))




