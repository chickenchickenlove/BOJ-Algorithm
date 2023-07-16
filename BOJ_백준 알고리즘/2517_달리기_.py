import sys
import math
from collections import defaultdict


def update(tree, node, start) :
    node += start
    while node :
        tree[node] += 1
        node //= 2
    return


def query(tree, node, left, right, start, end) :
    if left == right == start or left == right == end :
        return tree[node]
    elif right < start or end < left :
        return 0
    elif start <= left and right <= end :
        return tree[node]
    else :
        mid = (left + right) // 2
    return query(tree, node*2, left, mid, start, end) + query(tree, node*2 + 1, mid+1, right, start, end)



n = int(sys.stdin.readline().rstrip())
my_list = []
my_set = set()
for ___ in range(n) :
    a = int(sys.stdin.readline().rstrip())
    my_list.append(a)
    my_set.add(a)


my_set = sorted(my_set, reverse=True)
rank = defaultdict(int)
for idx, value in enumerate(my_set) :
    rank[value] = idx

cnt = len(my_set)
h_tree = 2**math.ceil(math.log2(cnt) + 1)
tree = [0 for _ in range(h_tree)]

answer_list = []
#현재 순서에서 내 앞에 몇 명 있는게 중요하다.
#query하고 update한다.
for now_rank, now_value in enumerate(my_list) :
    c_value = rank[now_value]
    max_value = query(tree,1,0, h_tree//2 -1, 0, c_value-1) + 1
    update(tree,c_value, h_tree//2)
    answer_list.append(min(now_rank + 1, max_value))


for a in answer_list :
    print(a)