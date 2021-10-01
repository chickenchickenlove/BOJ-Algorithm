#16978 수열과 쿼리 22
import sys
import math
sys.setrecursionlimit(10**5)

def init(tree, node, left, right) :
    if left == right :
        tree[node] = my_list[left]
        return
    else :
        mid = (left + right) // 2
        init(tree, node*2, left, mid)
        init(tree, node*2 + 1 , mid + 1 , right)
        tree[node] = tree[node*2] + tree[node*2+1]
        return


def update(tree, node, left, right, idx, value) :
    if left == right == idx :
        tree[node] = value
        return
    elif right < idx or idx < left :
        return
    else :
        mid = (left + right) // 2
        update(tree, node*2, left, mid, idx,value)
        update(tree, node*2+1, mid+1, right, idx, value)
        tree[node] = tree[node*2] + tree[node*2 + 1 ]
        return

def query(tree, node, left, right, start, end ) :
    if left == right == start or left == right == end :
        return tree[node]

    elif right < start or end < left :
        return 0
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right ) // 2
        a = query(tree, node*2, left, mid,start, end)
        b = query(tree, node*2+1, mid+1, right, start, end)
        return a+b


n = int(sys.stdin.readline().rstrip())
tree_idx = n
my_list = list(map(int,sys.stdin.readline().split()))

q1 = []
q2 = []
h_tree = 2**math.ceil(math.log2(tree_idx)+1)
tree = [0 for _ in range(h_tree)]
init(tree,1,0,tree_idx - 1 )



t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    qqq = list(map(int,sys.stdin.readline().split()))
    if qqq[0] == 2  :
        a,b,c,d = qqq
        if c > d :
            c,d = d,c
        q2.append((b-1,c-1,d-1))
    else :
        a,b,c = qqq
        q1.append((b-1,c))

answer_list = [0 for _ in range(len(q2))]
q_list = []

for cnt, value in enumerate(q2) :
    a,b,c = value
    q_list.append((a,b,c,cnt))

q_list = sorted(q_list, key = lambda x  : x[0])

now_idx = 0
for a,b,c,idx in q_list :
    if a >= now_idx :
        while a >= now_idx :
            o,p = q1[now_idx]
            update(tree, 1, 0, tree_idx - 1, o, p)
            now_idx +=1
    answer_list[idx] = query(tree, 1, 0, tree_idx - 1, b, c)



print('\n'.join(map(str,answer_list)))



