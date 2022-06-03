import sys
from collections import deque


def dfs(here, car_list_final, v, limit_time, parking_list):
    if v[here] == 1: return False
    v[here] = 1

    for parking_num, spend_time in car_list_final[here]:

        # 이분탐색에 주어진 시간보다 더 많은 시간이 걸리면 무시
        if spend_time > limit_time:
            continue

        # 이분탐색에 주어진 시간보다 더 적은 시간이 걸린다.
        # 만약 주차장이 비어있으면, 현재 차를 바로 주차
        # 만약 주차장이 비어있지 않으면, 현재 주차장에 주차된 자동차를 옮겨서 주차할 수 있는지 확인하고 가능하다면 여기에 주차.
        if parking_list[parking_num] == 9876543210 or dfs(parking_list[parking_num], car_list_final, v, limit_time,
                                                          parking_list):
            parking_list[parking_num] = here
            return True


# 이분매칭 메인함수
def sol1(limit_time):
    # 주차장에 주차된 자동차 번호를 담을 배열
    parking_list = [9876543210 for _ in range(parking_cnt)]

    # 이분 매칭
    for i in range(car_cnt):
        vvv = [0 for _ in range(car_cnt)]
        dfs(i, car_list_final, vvv, limit_time, parking_list)

    # 모든 차가 주차되었는지 확인.
    my_set = set()
    for k in parking_list:
        if k != 9876543210:
            my_set.add(k)

    if len(my_set) == car_cnt:
        return True
    else:
        return False


#각 자동차마다 BFS로 주차장까지 걸리는 시간 확인
def bfs(car_list, v):
    global n, m
    que = deque()
    sr, sc, car = car_list.pop()

    que.append((sr, sc, 0))
    v[car][sr][sc] = 0

    while que:
        r, c, time = que.popleft()
        next_time = time + 1

        for rr, cc in tra_list:
            next_r, next_c = r + rr, c + cc

            if -1 < next_r < n and -1 < next_c < m:
                if v[car][next_r][next_c] > next_time and my_list[next_r][next_c] != "X":
                    que.append((next_r, next_c, next_time))
                    v[car][next_r][next_c] = next_time

                    if my_list[next_r][next_c] == "P":
                        park_num = p_map[next_r][next_c]
                        car_list_final[car].append((park_num, next_time))


tra_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
car_list = []

for idx in range(n):
    temp = sys.stdin.readline().rstrip()
    for k in temp:
        my_list[idx].append(k)

cnt = 0
for rrr in range(n):
    for ccc in range(m):
        if my_list[rrr][ccc] == "C":
            my_list[rrr][ccc] = str(cnt)
            car_list.append((rrr, ccc, cnt))
            cnt += 1

car_cnt = cnt

# 각 자동차에 대한 방문 배열(BFS)
v = [[[9876543210 for _ in range(m)] for _ in range(n)] for _ in range(cnt)]

# 주차장의 좌표 + 이름위한 맵
p_map = [[1000 for _ in range(m)] for _ in range(n)]


#각 자동차 위치 + 번호 추가
cnt = 0
for rrr in range(n):
    for ccc in range(m):
        if my_list[rrr][ccc] == "P":
            p_map[rrr][ccc] = cnt
            cnt += 1
parking_cnt = cnt



# 이분 매칭을 위한 리스트 만들기
# 이분 매칭을 위한 자동차 → 주차장 정보 가지는 스택 만들기
car_list_final = [[] for _ in range(car_cnt)]
while car_list:
    bfs(car_list, v)





#차가 1대도 없을 때 0출력(문제 조건)
if car_cnt == 0:
    print(0)
    exit()


#이분 탐색으로 구간의 최소값 찾기
left, right = 0, 9876543210
ans = 9876543210


while left < right:

    # 구간의 최소값
    mid = (left + right) // 2

    # 만족하면 이 구간을 포함해서 재탐색
    if sol1(mid):
        right = mid
        ans = min(ans, mid)
    # 만족하지 않으면 이 구간을 제외하고 재탐색
    else:
        left = mid + 1

#정답 출력
if ans == 9876543210:
    print(-1)
else:
    print(ans)