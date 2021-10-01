import sys
import math


#최대값을 무조건 2개씩 위로 올려준다.
#leaf node는 무조건 0을 끼워서 올려주면 될 듯
#2개,2개, 가지고 있던 거 비교해서 제일 위에 있는 것 2개를 저장하면 될 듯




def init(tree, node, left, right) :
    if left == right :
        tree[node] = [my_list[left], 0]
        return

    else :
        mid = (left + right) // 2
        init(tree, node*2, left, mid)
        init(tree, node*2+1 , mid+1, right)

        temp = []
        for num in tree[node*2] :
            temp.append(num)
        for num in tree[node*2+1] :
            temp.append(num)
        temp = sorted(temp, reverse = True)
        tree[node] = [temp[0], temp[1]]

        return



def update(tree, node, left, right, idx, value) :
    if left == right == idx :
        tree[node] = [value,0]
        return
    elif idx < left or right < idx :
        return
    else :
        mid = (left + right) // 2
        update(tree, node*2, left, mid, idx, value)
        update(tree, node*2+1, mid+1, right, idx, value)

        temp = []
        for num in tree[node*2] :
            temp.append(num)
        for num in tree[node*2+1] :
            temp.append(num)
        temp = sorted(temp, reverse = True)
        tree[node] = [temp[0], temp[1]]
        return


def query(tree, node, left, right, start,end):

    if right < start or end < left :
        return [0,0]
    elif start <= left and right <= end :
        return tree[node]
    else:
        mid = (left + right) // 2
        a = query(tree, node*2, left, mid, start, end)
        b = query(tree, node*2+1, mid + 1 , right, start, end)

        temp = a + b
        temp = sorted(temp, reverse = True)


        return [temp[0],temp[1]]

n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
h_tree = 2**math.ceil(math.log2(n) + 1 )
tree = [[] for _ in range(h_tree)]
init(tree,1,0,n-1)



for _ in range(int(sys.stdin.readline().rstrip())) :
    a,b,c = map(int,sys.stdin.readline().split())
    if a == 1 :
        update(tree,1,0,n-1,b-1,c)
    elif a == 2 :
        print(sum(query(tree,1,0,n-1,b-1,c-1)))
