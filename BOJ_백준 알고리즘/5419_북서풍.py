import sys
import math


def update(tree,node,start) :
    node += start
    while node >= 1 :
        tree[node] += 1
        node //= 2
    return


def query(tree, node, left, right, start, end) :
    if right < start or end < left :
        return 0
    elif left == right == start or left == right == end:
        return tree[node]
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
        return query(tree, node*2, left, mid, start,end) + query(tree, node*2+1, mid+1, right, start,end)



t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    n = int(sys.stdin.readline().rstrip())
    #입력 받고 x좌표 순으로 정렬

    y_set = set()
    island_list = []
    for __ in range(n) :
        a,b = map(int,sys.stdin.readline().split())
        island_list.append((a,b))
        y_set.add(b)

    y_set = sorted(y_set)
    y_dict = { value : idx for idx,value in enumerate(y_set)}

    island_list2 = []
    for a,b in island_list :
        island_list2.append((a,y_dict[b]))
    island_list2 = sorted(island_list2, key = lambda x : (x[0],-x[1]))

    #tree 만듬
    h_tree = 2**math.ceil(math.log2(len(y_dict)) + 1)
    tree = [0 for _ in range(h_tree)]




    answer = 0
    for a,b in island_list2 :
        #구간을 나눠서 볼 필요가 없음.
        #구간을 나눠서 본 시간 복잡도 증가함.
        answer += query(tree, 1, 0, len(tree)//2 - 1, b, len(tree)//2 - 1)
        update(tree,b , len(tree)//2 )


    print(answer)

