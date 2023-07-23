import sys
from collections import deque


# Solution 함수
def bfs(v, my_map) :

    # 초기화
    que = deque()
    que.append((0,0,0,0,0))

    #방문 처리
    v[0][0][0][0] = 0

    while que :

        #rbit : 현재 row bit
        #cbit : 현재 column bit
        #time : 현재 방문 시간

        r, c, rbit, cbit, time = que.popleft()
        next_time = time + 1

        #이 자리에서 스위치를 껐을 때, 비트 상태 전환 (XOR 비트 연산 처리)
        next_rbit = rbit ^ (1 << r)
        next_cbit = cbit ^ (1 << c)

        #도착했으면 종료
        if r == n-1 and c == m-1 :
            print(time)
            return


        # 이 자리에서 스위치를 켤 때
        if v[next_rbit][next_cbit][r][c] > next_time :
            v[next_rbit][next_cbit][r][c] = next_time
            que.append((r,c, next_rbit, next_cbit, next_time))

        # 좌우 이동 확인
        for rr, cc in tra_list_lr:
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < m :

                # Validation
                if ((my_map[rbit][cbit][r][c] == "D" or my_map[rbit][cbit][r][c] == "A") and
                    (my_map[rbit][cbit][next_r][next_c] == "D" or my_map[rbit][cbit][next_r][next_c] == "A")
                    and v[rbit][cbit][next_r][next_c] > next_time) :

                    que.append((next_r, next_c, rbit, cbit, next_time))
                    v[rbit][cbit][next_r][next_c] = next_time

        # 위아래 이동 확인
        for rr, cc in tra_list_ud:
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < m :

                # Validation
                if ((my_map[rbit][cbit][r][c] == "C" or my_map[rbit][cbit][r][c] == "A") and
                        (my_map[rbit][cbit][next_r][next_c] == "C" or my_map[rbit][cbit][next_r][next_c] == "A")
                        and v[rbit][cbit][next_r][next_c] > next_time):
                    que.append((next_r, next_c, rbit, cbit, next_time))
                    v[rbit][cbit][next_r][next_c] = next_time


    # 만약에 이동 못할 때, 그만두기.
    print(-1)

# 그래프 회전 함수

def rotate_Row(my_list, rbit_list):
    global n, m

    for r in rbit_list:
        for c in range(m):
            if my_list[r][c] == "C":
                my_list[r][c] = "D"
            elif my_list[r][c] == "D":
                my_list[r][c] = "C"


def rotate_Col(my_list, cbit_list):
    global n, m

    for c in cbit_list:
        for r in range(n):
            if my_list[r][c] == "C":
                my_list[r][c] = "D"
            elif my_list[r][c] == "D":
                my_list[r][c] = "C"



#그래프 복사용 함수
def copy_array(my_list) :
    global n,m
    return_list = [[] for _ in range(n)]
    for idx,value in enumerate(my_list) :
        for k in value :
            return_list[idx].append(k)

    return return_list


# 좌우 이동 그래프
tra_list_lr = [[0, 1], [0, -1]]

# 상하 이동 그래프
tra_list_ud = [[1, 0], [-1, 0]]



# 값 입력
n,m = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    for k in temp :
        my_list[i].append(k)

#비트 샹태에 따른 방문 배열 : [Row 비트 상태][Col 비트 상태][Row][Col]
v_map = [[[[1000 for _ in range(m)] for _ in range(n)] for _ in range(2**m)] for _ in range(2**n)]

#비트 샹태에 따른 실제 맵 상태 : [Row 비트 상태][Col 비트 상태][Row][Col]
my_map = [[copy_array(my_list) for _ in range(2**m)] for _ in range(2**n)]


# my_map에서 비트 상태에 따라 어떤 맵을 가지고 있는지 만들어준다.
for rbit in range(2**n):
    rbit_list = []

    # Row에 돌려야할 비트 있는지 확인
    for i in range(n):
        if rbit & (1 << i) != 0 :
            rbit_list.append(i)

    for cbit in range(2**m) :
        cbit_list = []

        # Col에 돌려야할 비트 있는지 확인
        for k in range(m) :
            if cbit & (1 << k) != 0 :
                cbit_list.append(k)

        # 비트 정보 넘겨서 Rotate
        rotate_Row(my_map[rbit][cbit], rbit_list)
        rotate_Col(my_map[rbit][cbit], cbit_list)



#문제 풀이
bfs(v_map, my_map)
