import sys
from collections import deque


def bfs(n, m, k, my_list):
    que = deque()

    # 방문 배열 초기화
    v = [[[9876543210 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]

    # 시작점 방문 처리
    v[1][0][0] = 1
    que.append((0, 0, 1, 0, 1))


    # BFS 시작
    while que:


        r, c, time, break_cnt, day = que.popleft()

        # 도착지에 도착하면 현재 Time을 Return한다.
        # 다익스트라가 아니니 가장 먼저 도착하는 게 가장 빠르다.
        if r == n - 1 and c == m - 1:
            print(time)
            return

        for rr, cc in tra_list:

            # 다음으로 넘겨줄 변수들 정리
            next_r, next_c = r + rr, c + cc
            next_day = (day + 1) % 2

            # 좌표 범위 내에서만 탐색
            if -1 < next_r < n and -1 < next_c < m:

                #낮일 때
                if day == 0:
                    # 현재 상태의 다음 노드에 기록된 시간보다 현재 시간 + 1 이 더 작을 때만 추가 탐색
                    # 이미 방문했는데, 더 빠르게 방문했던 적이 있다면 그 후의 탐색을 동일하게 진행했으니 불필요함.

                    if v[break_cnt][next_r][next_c] > time + 1:

                        # 현재 위치가 0일 경우 추가 탐색
                        # 앞에서 이미 다음 방문할 노드가 재방문 노드인지 검토 끝남
                        if my_list[r][c] == '0':
                            v[break_cnt][next_r][next_c] = time + 1
                            que.append((next_r, next_c, time + 1, break_cnt, next_day))


                        # 현재 위치가 1일 경우 추가 탐색(낮이기 때문)
                        # 벽을 하나 더 새로 부술 예정이기 때문에 한번 더 재방문 노드 확인 필요함.

                        elif my_list[r][c] == '1' and break_cnt + 1 <= k:
                            if v[break_cnt + 1][next_r][next_c] > time + 1:
                                v[break_cnt + 1][next_r][next_c] = time + 1
                                que.append((next_r, next_c, time + 1, break_cnt + 1, next_day))
                #밤일 때
                elif day == 1:

                     # 밤일 때, 현재 위치가 벽이 아니면 이동 가능
                     if my_list[r][c] == '0' and v[break_cnt][next_r][next_c] > time + 1:
                        v[break_cnt][next_r][next_c] = time + 1
                        que.append((next_r, next_c, time + 1, break_cnt, next_day))


                    # 밤일 때, 현재 위치가 벽이면 대기한다.
                    # 단, 방문 노드에 기록된 시간과 현재 위치의 시간이 같을 때만 한다. 이외의 경우라면 어떤 경우라도 방문한 이력이 있음.
                    elif my_list[r][c] == '1' and v[break_cnt][r][c] == time:
                        v[break_cnt][r][c] = time + 1
                        que.append((r, c, time + 1, break_cnt, next_day))




    return print(-1)


# 변수 입력 받기
n, m, k = map(int, sys.stdin.readline().split())
my_list = []
for ___ in range(n):
    my_list.append(str(sys.stdin.readline().rstrip()))

tra_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
bfs(n, m, k, my_list)
