import sys
from collections import deque

#이분 탐색으로 들어가야 하는 위치를 찾아야 할 듯.
#그래서 여기부터 여기까지 싹 다 들어가게...


def binary_search_lower(start,end,target1, my_list,posi) :
    l = start
    r = end
    lower = 9876543210


    while l <= r :
        mid = (l+r) // 2

        if target1 -2 <= my_list[mid][posi] <= target1 + 2 :
            lower = min(mid, lower)
            r = mid - 1
        elif target1 - 2 > my_list[mid][posi] :
            l = mid + 1
        elif target1 + 2 < my_list[mid][posi] :
            r = mid-1

    return lower

def binary_search_upper(start,end, target, my_list,posi) :
    l = start
    r = end
    upper = -1
    while l <= r :
        mid = (l+r+1)//2
        if target-2 <= my_list[mid][posi] <= target + 2:
            upper = max(mid, upper)
            l = mid + 1
        elif target-2 > my_list[mid][posi] :
            l = mid + 1
        else :
            r = mid - 1





    return upper




def bfs(max_,n,my_list) :
    que = deque()
    v = [0 for _ in range(n)]

    que.append((0,0,0))


    while que :
        x,y,now_cnt = que.popleft()
        next_cnt = now_cnt + 1
        if y == max_ :
            return now_cnt


        lower = binary_search_lower(0, len(my_list)-1, x,my_list,0)
        upper = binary_search_upper(0, len(my_list)-1, x,my_list,0)

        for idx in range(lower, upper + 1 ) :
            if v[idx] == 0 :
                next_x, next_y = my_list[idx]
                if abs(y-next_y) <= 2 :
                    v[idx] = 1
                    que.append((next_x, next_y, next_cnt))



    return -1



n,T = map(int,sys.stdin.readline().split())
my_list = []
max_ = 0

for _ in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    my_list.append((a,b))


my_list = sorted(my_list, key = lambda x : (x[0],x[1]))
print(bfs(T,n,my_list))

