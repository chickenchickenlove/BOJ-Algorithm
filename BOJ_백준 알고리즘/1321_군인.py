import sys
import math


def init(tree, node, left, right) :
    if left == right :
        tree[node] = my_list[left]
        return tree[node]
    else :
        mid = (left + right) // 2
        a = init(tree, node*2, left, mid)
        b = init(tree, node*2+1, mid+1, right)
        tree[node] = a+b
        return tree[node]



def modify(tree, node, left, right, idx, value) :
    if left == right == idx :
        tree[node] += value
    elif idx < left or right < idx :
        return
    else :
        mid = (left + right) // 2
        modify(tree, node*2, left, mid, idx, value)
        modify(tree, node * 2+1, mid+1, right, idx, value)
        tree[node] = tree[node*2] + tree[node*2+1]
        return


def query(tree, node, left, right, start, end) :
    if right < start or end < left :
        return 0
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left+right) // 2
        a = query(tree, node*2, left, mid, start, end)
        b = query(tree, node*2+1, mid+1, right, start, end)
        return a+b













n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
h_tree = 2**(math.ceil(math.log2(n))+1)
tree = [0 for _ in range(h_tree)]
init(tree, 1, 0,n-1)


for _ in range(m) :
    a = list(map(int,sys.stdin.readline().split()))
    if a[0] == 1 :
        modify(tree,1,0,n-1, a[1]-1,a[2])

    else :
        l,r = 0, n-1
        answer = 0
        while l <= r :
            mid = (l + r + 1 )// 2
            zzz = query(tree, 1,0,n-1,0,mid)
            if zzz < a[1] :
               l = mid + 1
            elif zzz == a[1] :
                answer = mid
                break
            else :
                answer = mid
                r = mid-1

        print(answer+1)











