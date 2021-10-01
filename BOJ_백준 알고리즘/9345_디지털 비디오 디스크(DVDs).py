import sys
import math

#비재귀로 구현이 필요하다.
#min, max면 그 구간이 보장된다.

def init(tree, node, start) :
    value = my_list[node]
    node += start
    tree[node] = [value, value]
    while node > 1 :
        node //= 2
        tree[node] = [min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1],tree[node*2+1][1])]
    return




def update(tree, node, start, value) :
    node += start
    tree[node] = [value,value]
    while node > 1 :
        node //= 2
        tree[node] = [min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1],tree[node*2+1][1])]
    return

def query(tree, node, left, right, start, end) :
    if right < start or end < left :
        return [9876543210, -1]
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
        a = query(tree, node*2, left, mid, start, end)
        b = query(tree, node * 2+1, mid+1, right, start, end)
        c = [min(a[0],b[0]), max(a[1],b[1])]
        return c



for _ in range(int(sys.stdin.readline().rstrip())) :
    n,k = map(int,sys.stdin.readline().split())
    my_list = [i for i in range(n)]
    h_tree = 2**math.ceil(math.log2(n)+1)
    h_tree_index = h_tree//2
    tree = [[9876543210,-1] for _ in range(h_tree)]

    for num in my_list :
        init(tree,num,h_tree_index)



    for ___ in range(k) :
        a,b,c = map(int,sys.stdin.readline().split())
        if a == 0 :
            update(tree,b, h_tree_index,my_list[c])
            update(tree,c, h_tree_index, my_list[b])
            my_list[b], my_list[c] = my_list[c], my_list[b]
        elif a == 1 :
            answer = query(tree, 1,0,h_tree_index - 1, b,c)
            if b == answer[0] and c == answer[1] :
                print('YES')
            else :
                print('NO')
