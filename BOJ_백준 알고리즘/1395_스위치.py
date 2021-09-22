import sys
import math


#init 처리할 필요가 없음. 처음부터 다 꺼져있음.

def propagation(left, right, node) :
    if left != right :
        tree[node * 2][1] = (tree[node * 2][1] +  tree[node][1]) % 2
        tree[node * 2 + 1][1] = (tree[node * 2 + 1 ][1] + tree[node][1]) % 2
    tree[node][1] = 0
    tree[node][0] = abs((right - left + 1 ) - tree[node][0])

    return




def update(tree, node, left, right, start, end) :
    if left == right == start or left == right == end:
        if tree[node][1] == 1 :
            tree[node][1] = 0
            tree[node][0] = (tree[node][0] + 1) % 2

        tree[node][0] = (tree[node][0] + 1 ) %2
        return
    else :
        if tree[node][1] == 1 :
            propagation(left, right, node)

        if right < start or end < left :
            return
        elif start <= left and right <= end :
            if left != right :
                tree[node*2][1] = (tree[node*2][1] + 1)%2
                tree[node*2 + 1][1] = (tree[node*2 + 1][1] + 1) % 2
            tree[node][0] = abs((right - left + 1 ) - tree[node][0])
        else :
            mid = (left + right) // 2

            update(tree, node * 2 , left, mid, start, end)
            update(tree, node * 2 +1 , mid + 1 , right, start, end)
            tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
            return




def query(tree, node, left, right, start, end) :
    if left == right == start or left == right == end :
        if tree[node][1] == 1 :
            tree[node][1] = 0
            tree[node][0] = (tree[node][0] + 1) % 2

        return tree[node][0]
    else :
        if tree[node][1] == 1 :
            propagation(left, right, node)

        if right < start or end < left :
            return 0
        elif start <= left and right <= end :

            return tree[node][0]
        else :
            mid = (left + right) // 2

            a = query(tree, node * 2 , left, mid, start, end)
            b = query(tree, node * 2 +1 , mid + 1 , right, start, end)
            tree[node][0] = tree[node*2][0] + tree[node*2+1][0]

            return a+b





# lazy 처리할 때, 여러번일 경우 %2 연산으로 설정하면 됨.



n,m = map(int,sys.stdin.readline().split())
h_tree = 2**(math.ceil(math.log2(n))+1)
tree = [[0,0] for _ in range(h_tree)]
#print(tree)
for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 0 :
        update(tree,1,0,n-1,b-1,c-1)
        #print(tree)


    else :
        print(query(tree,1,0,n-1,b-1,c-1))

