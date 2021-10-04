import sys
import math


def propagation(node, left, right) :
    #잎새 노드가 아니면
    if lazy[node] != 0 :
        if (right - left +  1) % 2 == 1 :
            tree[node] ^= lazy[node]
        if left != right :
            lazy[node * 2] ^= lazy[node]
            lazy[node * 2 + 1] ^= lazy[node]
    lazy[node] = 0
    return



def init(tree, node, left, right) :
    if left == right :
        tree[node] = my_list[left]
        return tree[node]
    else :
        mid = (left + right)//2
        tree[node] = init(tree, node*2, left, mid) ^ init(tree, node * 2+1, mid+1, right)
        return tree[node]


def update(tree, node, left, right, start, end, value) :

    #lazy가 있을 경우 전파한다
    propagation(node, left, right)

    #다른 구간일 경우 아무것도 하지 않는다.
    if right < start or end < left :
        return

    #포함되는 구간일 경우
    elif start <= left and right <= end :
        if (left - right + 1)%2 == 1 :
            tree[node] ^= value
        #잎새 노드가 아니면, lazy 전파해준다.
        if left != right :
            lazy[node*2] ^= value
            lazy[node*2+1] ^= value
        return

    else :
        mid = (left + right) // 2
        update(tree, node*2, left, mid, start, end, value)
        update(tree, node*2+1, mid+1, right, start, end, value)
        tree[node] = tree[node*2] ^ tree[node*2+1]
        return tree[node]


def query(tree, node, left, right, start, end) :
    #현재 노드에 lazy가 있다면, 전파 및 업데이트 해준다


    propagation(node, left, right)

    #원하는 구간이 아니면 return
    if right < start or end < left :
        return 0

    # 원하는 구간이면 return 해준다.
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
        return query(tree, node*2, left, mid, start, end) ^ query(tree, node*2+1, mid+1, right, start, end)



n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
h_tree = 2**(math.ceil(math.log2(n))+1)
tree,lazy = [0 for _ in range(h_tree)],[0 for _ in range(h_tree)]

init(tree, 1, 0, n-1)

m = int(sys.stdin.readline().rstrip())
for _ in range(m) :
    q = list(map(int,sys.stdin.readline().split()))
    if q[0] == 1 :
        a,b,c,d = q
        if b > c :
            b,c = c,b
        update(tree, 1,0,n-1,b,c,d)
    else :
        a,b,c = q
        if b > c :
            b,c = c,b
        print(query(tree,1,0,n-1,b,c))




