import sys
from collections import deque


def bfs(sz,sr,sc, a,b,d,):

    # 변수 초기화
    que = deque()
    que.append((sz,sr,sc,0))


    #방문 배열 선언 + 체크
    v = [[[9876543210 for _ in range(d)] for _ in range(b)] for _ in range(b)]
    v[sz][sr][sc] = 1

    while que :

        z,r,c,now_time = que.popleft()
        next_time = now_time + 1

        # 목적지 도착
        if my_map[z][r][c] == "E":
            return now_time


        for zz,rr,cc in tra_list:
            next_z, next_r, next_c = z + zz , r + rr, c + cc
            #경계 조건 확인
            if -1 < next_z < a and -1 < next_r < b and -1 < next_c < d:

                # 경계 조건 넣고 가능하면 한번 더 이동.
                if my_map[next_z][next_r][next_c] != "#" and v[next_z][next_r][next_c] > next_time:
                    que.append((next_z, next_r, next_c, next_time))
                    v[next_z][next_r][next_c] = next_time

    # 목적지 도착 X
    return 9876543210



# 그래프 탐색용
tra_list = [[1,0,0], [-1,0,0], [0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]


while 1 :

    #변수 입력
    l,r,c = map(int,sys.stdin.readline().split())


    #종료 조건
    if l == 0 and r == 0 and c == 0 :
        break


    #입력 정규화
    my_map = [[] for _ in range(l)]
    for i in range(l) :
        for j in range(r) :
            temp = sys.stdin.readline().rstrip()
            my_map[i].append(temp)

            # 시작 위치 찾기
            for idx, value in enumerate(temp):
                if value == "S":
                    sz,sr,sc = i, j, idx

        # 공백 제거용
        q = input().rstrip()

    #BFS
    ans = bfs(sz,sr,sc,l,r,c)

    #결과 출력
    if ans != 9876543210 :
        print(f'Escaped in {ans} minute(s).')
    else :
        print("Trapped!")