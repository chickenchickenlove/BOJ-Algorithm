import sys
from collections import deque

def find(x, x_num) :

    # 루트 넘버 도착 시, 현재 값을 더해준다.
    # 루트 넘버 반환
    if k_list[x] == x :
        n_list[x] += x_num
        return x

    else :
        next_x_num = n_list[x] + x_num

        # 합쳐 졌으니, Count는 넘겨준다.
        n_list[x] = 0

        # 루트값을 현재 노드에 저장해둔다.
        k_list[x] = find(k_list[x],next_x_num)

        return k_list[x]

def union(x,y) :
    xx = find(x, 0)
    yy = find(y, 0)

    # 0을 기준으로 루트 넘을 합쳐준다.
    # 0에서 종료조건임.
    if xx > yy :
        # root_num끼리 합쳐줘야함.
        k_list[xx] = yy
        find(xx,0)
    else :
        k_list[yy] = xx
        find(yy, 0)

    return

#문명 전파
def bfs(city):
    que = deque()
    while city :
        a,b,city_num = city.pop()
        que.append((a,b,city_num))

    while que :
        r,c,city_num = que.popleft()

        for rr,cc in tra_list:
            next_r, next_c = r + rr, c + cc

            if -1 < next_r < n and -1 < next_c < n:
                if my_list[next_r][next_c] == -1 :
                    my_list[next_r][next_c] = city_num
                    city.append((next_r, next_c, city_num))



#이웃한 문명끼리 유니온 파인드 대상인지 확인
def union_find(city):

    for r,c,city_num in city:
        for rr, cc in tra_list:
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < n:

                next_city_num = my_list[next_r][next_c]


                #Union Find 대상
                if my_list[next_r][next_c] != -1 and city_num != next_city_num :
                    union(next_city_num, city_num)


tra_list = [[1,0],[-1,0],[0,1],[0,-1]]


n,k = map(int,sys.stdin.readline().split())
# 분리 집합 루트보관
k_list = [q for q in range(k)]
# 분리 집합 현재 가지고 있는 갯수 보관
n_list = [1 for _ in range(k)]
my_list = [[-1 for _ in range(n)] for _ in range(n)]
city = []
for cnt in range(k):
    a,b = map(lambda x:x-1, map(int,sys.stdin.readline().split()))
    my_list[a][b] = cnt
    city.append((a,b,cnt))


day = 0


# 초기 조건 경계 조건 클리어

union_find(city)

while n_list[0] != k :
    day += 1

    # 영토 확장
    bfs(city)

    # 분리집합 처리
    union_find(city)

print(day)
