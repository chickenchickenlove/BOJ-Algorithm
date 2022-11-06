import sys
import math
sys.setrecursionlimit(10**7)

def tree_init(start,end,node) : #tree 초기화 함수. 각 구간의 최소 값이 들어있는 인덱스를 리턴한다.
    if start == end :
        tree[node] = start
    else :
        mid = (start + end) // 2
        tree_init(start, mid, node*2)
        tree_init(mid+1, end, node*2 + 1)
        if ml[tree[node*2]] > ml[tree[node*2+1]] :
            tree[node] = tree[node*2 + 1]
        else :
            tree[node] = tree[node*2]

# 문제푸는 함수가 필요

# 구간의 최소 높이를 알려주는 인덱스 확인.
def find_min(start,end,node,left,right) :
    if end < left or right < start :
        return -1
    elif left <= start and end <= right :
        return tree[node]
    else :
        mid = (start + end) // 2
        a = find_min(start,mid,node*2,left,right)
        b = find_min(mid + 1 , end , node * 2 + 1 , left, right)

        if a == - 1 :
            return b
        elif b == - 1 :
            return a
        else :
            if ml[a] > ml[b] :
                return b
            else :
                return a

def sol(start,end) :
    global answer
    global n
    if start == end :
        if ml[start] > answer :
            answer = ml[start]
        return

    min_idx = find_min(1,n,1,start,end)
    v = ml[min_idx]
    if v * (end - start + 1 ) > answer :
        answer = v * (end - start + 1)
    if start <= min_idx -1 :
        sol(start, min_idx - 1)
    if min_idx + 1 <= end :
        sol(min_idx + 1, end)


while 1 :
    ml = list(map(int,input().split()))
    n = ml[0]
    if n == 0 :
        break
    answer = 0
    if math.log2(n) == n ** 0.5:
        htree = n * 2
    else:
        htree = (2 ** (int(math.log2(n)) + 1)) * 2
    tree = [987654321000 for _ in range(htree)]
    tree_init(1, len(ml) - 1, 1)
    sol(1,n)
    print(answer)

