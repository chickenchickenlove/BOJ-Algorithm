import sys
import math


#merge sort tree를 만든다.
#lazy는 필요없다.

#1. merge sort tree를 만든다
#2. query를 입력 받는다. XOR 처리해준다. 그 후 i,j는 반드시 순서 정렬을 해준다.
#3. 해당 되는 구간의 merge sort tree에서  binary search를 통해서 갯수를 세서 return 해준다.
#4. 구현 필요한 함수. 초기화 함수 / query 함수 / Lower Bouned


def init(tree, node, left, right) :
    if left == right :
        tree[node].append(my_list[left])
        return
    else :
        mid = (left + right) // 2
        init(tree, node*2, left, mid)
        init(tree, node*2+1, mid+1, right)
        for num in tree[node*2] :
            tree[node].append(num)
        for num in tree[node * 2+1]:
            tree[node].append(num)
        tree[node] = sorted(tree[node])
        return


def binary_search(find_list, value) :
    l,r = 0, len(find_list) -1
    answer = 0
    while l < r :
        mid = (l + r) // 2
        if find_list[mid] > value :
            r = mid
            answer = mid
        else : l = mid + 1
    answer = (l + r )// 2
    if find_list[answer] > value :
        return len(find_list) - answer
    else :
        return 0



def query(tree, node, left, right, start, end,value) :
    if right < start or end < left :
        return 0
    elif start <= left and right <= end :
        return_value = binary_search(tree[node],value)
        return return_value
    else :
        mid = (left + right) // 2
        a = query(tree, node*2, left, mid, start, end, value)
        b = query(tree, node*2+1, mid+1, right, start, end, value)
        return a+b





n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
h_tree = 2**math.ceil(math.log2(n) + 1)
tree = [[] for _ in range(h_tree)]
init(tree,1,0,n-1)


last_answer = 0
for _ in range(int(sys.stdin.readline().rstrip())) :
    a,b,c = map(int,sys.stdin.readline().split())
    i,j,k = map(lambda x : x ^ last_answer,(a,b,c))
    if a > b :
        a,b = b,a
    last_answer = query(tree,1,0,n-1,i-1,j-1,k)
    print(last_answer)
