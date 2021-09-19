import sys
import math



def modify(tree, node, tl, tr, idx, value) :
    if tl == tr == idx :
        tree[node] = value
        return
    elif idx < tl or tr < idx :
        return
    else :
        mid = (tl + tr) // 2
        if tl <= idx <= mid :
            modify(tree, node * 2, tl, mid, idx, value)
        if mid + 1 <= idx <= tr :
            modify(tree, node * 2 + 1, mid + 1, tr, idx, value)
        tree[node] = tree[node*2] + tree[node*2 + 1]
        return


def query(tree, node, tl, tr, vl, vr) :
    if tr < vl or vr < tl :
        return 0
    elif vl <= tl and tr <= vr :
        return tree[node]
    else :
        mid = (tl + tr) // 2
        return query(tree, node * 2 , tl, mid, vl, vr) + query(tree, node * 2 + 1, mid + 1, tr, vl, vr)

n,m = map(int,sys.stdin.readline().split())
if int(math.log2(n)) == n ** 0.5 :
    h_tree = n * 2
else :
    h_tree =   2 ** (int(math.log2(n) + 1) + 1)

tree = [0 for _ in range(h_tree)]


for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 0 :
        if b > c :
            b,c = c,b
        print(query(tree,1, 0, n-1, b-1, c-1))
    else :
        modify(tree, 1, 0, n-1, b-1, c)


