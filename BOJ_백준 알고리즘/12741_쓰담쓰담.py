import sys
import math

#12741_쓰담쓰담

#바로 앞사람보다 키가 크거나 같으면 0
#바로 앞사람보다 키가 작으면 1
#각 노드마다 값을 3개씩 담는다 (left, right, 논리지수)
#원하는 구간의 논리지수가 1이면 항상 실패. (or 연산으로 위로 올린다)
#애매한 구간은 right, left 비교해서 보는 것으로 한다. 항상 구간 업데이트를 해준다.
#왼쪽의 오른쪽과 오른쪽의 왼쪽을 비교하면 된다


def init(tree, node, left, right) :
    if left == right :
        tree[node][0] = my_list[left]
        tree[node][1] = my_list[left]
        tree[node][2] = 0
        return
    else :
        mid = (left + right) // 2
        init(tree, node*2, left, mid)
        init(tree, node*2+1, mid+1, right)

        if tree[node*2][1] <= tree[node*2+1][0] :
            tree[node][2] = 0
        else :
            tree[node][2] = 1

        tree[node][2] = tree[node][2] | tree[node*2][2] | tree[node*2+1][2]
        tree[node][0] = tree[node*2][0]
        tree[node][1] = tree[node*2+1][1]
        return




def update(tree, node, left, right, idx, value) :
    if left == right == idx :
        tree[node] = [value, value, 0]
        return
    elif idx < left or right < idx :
        return
    else :
        mid = (left + right) // 2
        update(tree, node * 2, left, mid, idx, value)
        update(tree, node * 2 + 1, mid + 1, right, idx, value)

        if tree[node * 2][1] <= tree[node * 2 + 1][0]:
            tree[node][2] = 0
        else:
            tree[node][2] = 1

        tree[node][2] = tree[node][2] | tree[node * 2][2] | tree[node * 2 + 1][2]
        tree[node][0] = tree[node * 2][0]
        tree[node][1] = tree[node * 2 + 1][1]
        return



def query(tree, node, left, right, start, end) :
    if right < start or end < left :
        return [0,9876543210,0]
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
        a = query(tree, node*2, left, mid, start, end)
        b = query(tree, node*2+1, mid+1, right, start, end)
        c = [a[0],b[1],0]
        if a[1] == 9876543210 :
            c = b

        elif b[1] == 9876543210 :
            c = a

        else :
            if a[1] <= b[0] :
                temp = 0
            else :
                temp = 1

            c[2] = a[2] | b[2] | temp

        return c


n,k = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
h_tree = 2**math.ceil(math.log2(n)+1)
tree = [[0,0,0] for _ in range(h_tree)]
init(tree, 1,0,n-1)


for _ in range(k) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1 :
        z = query(tree,1,0,n-1,b-1,c-1)
        if z[2] == 0 :
            print('CS204')
        else :
            print('HSS090')
    else :
        my_list[b-1],my_list[c-1] = my_list[c-1], my_list[b-1]
        update(tree, 1, 0 ,n-1,b-1, my_list[b-1])
        update(tree, 1, 0, n - 1, c - 1, my_list[c- 1])
