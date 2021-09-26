import sys
import math


def init_tree(tree, node, left, right) :
    global my_list
    if left == right :
        if my_list[left] == 0 :
            tree[node] = 0
        elif my_list[left] < 0 :
            tree[node] = -1
        else :
            tree[node] = 1
        return tree[node]
    else :
        mid = (left + right) // 2
        tree[node] = init_tree(tree, node*2, left, mid) * init_tree(tree, node*2 + 1 , mid + 1 , right)
        return tree[node]


def update(tree, node, left, right, idx, value) :
    if left == right == idx :
        if value > 0 :
            value = 1
        elif value < 0 :
            value = -1

        tree[node] = value
        return
    elif idx < left or right < idx :
        return
    else :
        mid = (left + right) // 2

        if left <= idx <= mid :
            update(tree, node*2, left, mid , idx, value)
        if mid + 1 <= idx <= right:
            update(tree, node*2+1, mid + 1 , right , idx, value)
        tree[node] = (tree[node*2] * tree[node*2 + 1])
        return


def query(tree, node, left, right, start, end) :
    if left == right == start :
        return tree[node]
    elif right < start or end < left :
        return 1
    elif start <= left and  right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
        return query(tree, node*2, left, mid , start, end) *query(tree, node*2+1, mid + 1 ,right,start,end)



while 1 :
    try :
        n,k = map(int,sys.stdin.readline().split())
    except :
        exit()


    my_list = list(map(int,sys.stdin.readline().split()))

    h_tree =  2**(math.ceil(math.log2(n)) + 1)
    tree = [1 for _ in range(h_tree)]
    init_tree(tree, 1, 0, n-1)
    answer_list = []
    for _ in range(k) :
        q = list(map(str,sys.stdin.readline().split()))
        a,b = map(int,q[1:])
        if q[0] == 'C' :
        #UPDATE
            update(tree,1, 0, n-1, a - 1, b)
        else :
            result = query(tree,1,0,n-1, a-1, b-1 )
            if result == 0 :
                answer_list.append('0')
            elif result < 0 :
                answer_list.append('-')
            else :
                answer_list.append('+')
    print(''.join(answer_list))