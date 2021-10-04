import sys
import math




def update(min_tree, max_tree, node, start, value) :
    node += start
    min_tree[node] = value
    max_tree[node] = value
    while node > 1 :
        node //= 2
        min_tree[node] = min(min_tree[node*2], min_tree[node*2+1])
        max_tree[node] = max(max_tree[node*2], max_tree[node*2+1])
    return

def query(min_tree,max_tree, node, left, right, start, end) :
    if right < start or end < left :
        return [9876543210, 0 ]
    elif start <= left and right <= end :
        return [min_tree[node], max_tree[node]]
    else :
        mid = (left + right) // 2
        a = query(min_tree, max_tree, node*2, left, mid, start, end)
        b = query(min_tree, max_tree, node * 2+1, mid+1, right, start, end)

        if a[0] == 9876543210 :
            return b
        elif b[0] == 9876543210 :
            return a
        else :
            return [min(a[0],b[0]), max(a[1],b[1])]


n,m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list = list(map(lambda x : x-1, my_list))


h_tree = 2**(math.ceil(math.log2(n))+1)
min_tree = [9876543210 for _ in range(h_tree)]
max_tree = [0 for _ in range(h_tree)]



for idx,height in enumerate(my_list) :
    update(min_tree,max_tree, height, h_tree//2, idx)



for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1 :
        my_list[b-1], my_list[c-1] = my_list[c-1], my_list[b-1]
        update(min_tree, max_tree, my_list[b-1], h_tree//2, b-1)
        update(min_tree, max_tree, my_list[c-1],h_tree//2, c-1)
    else :
        k = query(min_tree, max_tree, 1, 0 , h_tree//2-1, b-1, c-1)
        if abs(k[1] - k[0]) == abs(b-c) :
            print('YES')
        else :
            print('NO')