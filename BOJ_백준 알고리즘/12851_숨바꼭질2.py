import sys
from collections import deque


def bfs(n,k) :
    que = deque()

    #방문 배열 선언, 배열에는 방문한 최소 시간 기입
    v = [9876543210 for _ in range(100000 + 1)]

    #방문 설정 및 que에 start 지점 넣어줌.
    v[n] = 0
    que.append((n,0))


    #정답 초기화. answer는 최소 시간, answer_cnt는 경로수
    answer = 9876543210
    answer_cnt = 0


    while que :

        now_posi, now_time = que.popleft()

        #que에서 나온 값의 현재 시간이 현재 경로에 도착한 최소 시간보다 작다면 더 이상 볼 필요가 없음.
        if now_time > answer :
            continue


        #현재 위치가 동생의 위치에 도달했다면 정답 갱신함.
        if now_posi == k :
            if answer > now_time :
                answer = now_time
                answer_cnt = 1
            elif answer == now_time :
                answer_cnt += 1


        next_time = now_time + 1


        # BFS 시작. +1, -1, *2 방향으로 진행.
        if now_posi + 1 <= 100000:
            if v[now_posi + 1 ] >= next_time :
                v[now_posi + 1] = next_time
                que.append((now_posi + 1, next_time))

        if now_posi - 1 >= 0 :
            if v[now_posi - 1] >= next_time :
                v[now_posi - 1] = next_time
                que.append((now_posi - 1, next_time))


        if now_posi * 2 <= 100000 :
            if v[now_posi * 2 ] >= next_time :
                v[now_posi *2 ] = next_time
                que.append((now_posi *2 , next_time))

    #최단시간 출력
    print(answer)

    #최단시간 경로수 출력
    print(answer_cnt)
    return

n,k = map(int,sys.stdin.readline().split())
bfs(n,k)

