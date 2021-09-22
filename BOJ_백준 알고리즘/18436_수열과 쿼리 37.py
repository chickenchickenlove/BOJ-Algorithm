import sys
import math



#왼쪽이 짝수, 오른쪽이 홀수
def init(tree, node, left, right) :
    if left == right :
        if my_list[left] % 2 == 0 :
            tree[node][0] = 1
        else :
            tree[node][1] = 1

        return
    else :

        mid = (left + right) // 2
        init(tree, node*2, left, mid)
        init(tree, node*2 + 1 , mid + 1 , right)
        tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
        tree[node][1] = tree[node*2][1] + tree[node*2+1][1]
        return


# start, end는 내가 확인하는 구간
def query(tree, node, left, right, start, end) :
    if right < start or end < left :
        return [0,0]

    elif start <= left and right <= end :
        return tree[node]

    else :

        mid = (left + right) // 2
        a = query(tree, node *2 , left , mid, start, end)
        b = query(tree, node *2 + 1 , mid + 1  , right, start, end)

        even = a[0] + b[0]
        odd = a[1] + b[1]

        return [even, odd]


def modify(tree, node, left, right, idx, value) :
    if left == right == idx :
        if value % 2 == 0 :
            tree[node] = [1,0]
        else :
            tree[node] = [0,1]
        return
    elif idx < left or right < idx :
        return


    else :
        mid = (left + right) // 2
        modify(tree, node * 2, left, mid, idx, value)
        modify(tree, node * 2 + 1, mid+1, right, idx, value)

        even = tree[node*2][0] + tree[node*2+1][0]
        odd = tree[node * 2][1] + tree[node * 2 + 1][1]
        tree[node] = [even,odd]
        return







































n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))


if math.log2(n) == n ** 0.5 :
    h_tree = n * 2
else :
    h_tree = 2 ** (int(math.log2(n) + 1) + 1 )



tree = [[0,0] for _ in range(h_tree)]

m = int(sys.stdin.readline().rstrip())


init(tree,1,0, n-1)

for _ in range(m) :
    a,b,c = map(int,sys.stdin.readline().split())


    # i번째 수를 x로 바꾼다.
    if a == 1 :
        modify(tree,1,0,n-1,b-1,c)
    #b,c 짝수 갯수 출력
    elif a == 2 :
        k = query(tree,1,0,n-1,b-1,c-1)
        print(k[0])


    #b,c 홀수 갯수 출력
    else :
        k = query(tree,1,0,n-1,b-1,c-1)
        print(k[1])