import sys
from collections import deque


def bfs(n,m,k):

    # 초기화
    que = deque()
    que.append((0,0,0,0))
    v[0][0][0] = 0

    while que :

        # 현재 위치 확인 및 변수 초기화
        r,c,horse, time = que.popleft()
        next_time = time + 1
        next_horse = horse + 1


        #도착 시 값 출력 (종료 조건)
        if r == n-1 and c == m-1 :
            print(time)
            return

        #원숭이처럼 움직일 때
        for rr, cc in monkey_list:
            next_r, next_c = r+rr, c+cc

            if -1 < next_r < n and -1 < next_c < m:
                #3차원 배열 HORSE 확인
                if my_list[next_r][next_c] == 0 and v[horse][next_r][next_c] > next_time :
                    v[horse][next_r][next_c] = next_time
                    que.append((next_r, next_c, horse, next_time))

        #말처럼 움직일 때
        for rr, cc in horse_list:
            next_r, next_c = r+rr, c+cc

            if next_horse > k :
                break

            if -1 < next_r < n and -1 < next_c < m:
                # 3차원 배열 NEXT_HORSE 확인
                if my_list[next_r][next_c] == 0 and v[next_horse][next_r][next_c] > next_time :
                    v[next_horse][next_r][next_c] = next_time
                    que.append((next_r, next_c, next_horse, next_time))

    #못 도착하면 종료
    print(-1)
    return

# 이동 배열 선언
monkey_list = [[1,0],[-1,0],[0,1],[0,-1]]
horse_list = [[1,2], [2,1], [2,-1],[1,-2], [-1,2],[-2,1], [-1,-2],[-2,-1]]

# 변수 입력
k = int(sys.stdin.readline().rstrip())
m,n = map(int,sys.stdin.readline().split())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

# 방문 체크용 배열
v = [[[9876543210 for _ in range(m)] for _ in range(n)] for _ in range(k+1)]

# SOLUTION
bfs(n,m,k)

