import sys
import math

#세그먼트 트리 -> 구간합.

def init_tree(tree, my_list, node, ml,mr) :

    if ml == mr :
        tree[node] = my_list[ml]
        return
    else :


        l_node, r_node = node * 2, node * 2 + 1
        mid = (ml + mr) // 2
        init_tree(tree, my_list, l_node, ml, mid )
        init_tree(tree, my_list, r_node, mid+1, mr)

        tree[node] = tree[node*2] + tree[node*2 + 1]
        return


def query(tree, my_list, node, ml, mr, tl, tr) :
    if mr < tl or tr < ml :
        return 0

    elif tl <= ml and mr <= tr :
        return tree[node]

    else :
        l_node , r_node = node*2 , node*2 + 1
        mid = (ml + mr) // 2
        a = query(tree, my_list, l_node, ml, mid, tl, tr )
        b = query(tree, my_list, r_node, mid+1, mr, tl, tr)
        return a + b


def change(tree, my_list, node, ml, mr, idx, value) :
    if ml == mr == idx :
        tree[node] = value
        return tree[node]
    elif mr < idx or idx < ml :
        return 0
    else :
        l_node , r_node = node*2 , node*2 + 1
        mid = (ml + mr) // 2
        a = change(tree, my_list, l_node, ml, mid, idx, value )
        b = change(tree, my_list, r_node, mid+1, mr, idx, value)
        tree[node] = tree[node*2] + tree[node * 2 + 1 ]

        return a + b









n,q = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))



if math.log2(n) == n ** 0.5 :
    h_tree = n*2
else :
    h_tree =  2 ** (int(math.log2(n) + 1) + 1)

tree = [0 for _ in range(h_tree)]
init_tree(tree, my_list, 1, 0, len(my_list) - 1)

for _ in range(q) :
    a,b,c,d = map(int,sys.stdin.readline().split())
    if a > b :
        tmp = a
        a = b
        b = tmp
    print(query(tree, my_list, 1, 0 , len(my_list) - 1, a-1, b-1))

    change(tree, my_list, 1, 0, len(my_list) - 1, c-1, d)


