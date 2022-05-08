import sys
from collections import deque


def now_condition(time_mod, now_status):
    posi = con_list[now_status]
    next_posi = (posi + time_mod)%4
    return con_list2[next_posi]


con_list = {}
con_list["E"] = 0
con_list["N"] = 1
con_list["W"] = 2
con_list["S"] = 3
con_list2 = ["E", "N", "W", "S"]
tra_list = ((-1,0, "S"),(1,0, "N"),(0,1, "E"),(0,-1, "W"))


while True:

    n,m = map(int,sys.stdin.readline().split())

    if n == 0 and m == 0 :
        break

    my_map = [[] for _ in range(n)]
    for idx in range(n) :
        temp = sys.stdin.readline().rstrip()
        for k in temp :
            my_map[idx].append(k)


    k = int(sys.stdin.readline().rstrip())
    # [어떤 보물 가졌는지 비트][몇 초에 도착했는지][행][열]
    my_p = [tuple(map(lambda x:x-1,map(int,sys.stdin.readline().split()))) for _ in range(k)]


    #
    # n,m = 100,100
    # my_map = [["E" for _ in range(m)] for _ in range(n)]
    # k = 8
    # my_p =[(1,0),(25,25), (2,2), (3,3), (4,49), (5,5), (6,6),(49,7)]



    my_key = [[-1 for _ in range(m)] for _ in range(n)]
    for index, value in enumerate(my_p) :
        r,c = value
        my_key[r][c] = index


    #
    # sum_time = 0
    # check_precious_time = 0

    v = [[[[9876543210 for _ in range(m)] for _ in range(n)] for _ in range(4)] for _ in range(2 ** k)]
    # 기본 셋팅 완료

    # 변수 생성
    que = deque()
    que.append((0, 0, 0, 0))
    v[0][0][0][0] = 0

    while que:
        r, c, p, time = que.popleft()

        # 다음 관련된 거 설정
        next_time = time + 1

        # TODO 뺑글뺑글 돌 때 2~3초 정도 기다려도 될 수도 있음. 이거 나중에 고민해보자.
        # 판별 위한 거
        now_mod = time % 4
        next_mod = next_time % 4
        now_dir = now_condition(now_mod, my_map[r][c])

        if r == n - 1 and c == m - 1 and p == (2 ** len(my_p)) - 1:
            print(time)
            break

        for rr, cc, dir in tra_list:
            next_r, next_c = r + rr, c + cc

            if -1 < next_r < n and -1 < next_c < m and now_dir == dir:

                # 다음 갈 위치가 보물인지 확인한다.
                # 음수면 보물이 아니다.

                if my_key[next_r][next_c] != -1:
                    next_key = p | 1 << my_key[next_r][next_c]
                else:
                    next_key = p

                # 보물이 아닌 경우

                if v[next_key][next_mod][next_r][next_c] > next_time:
                    v[next_key][next_mod][next_r][next_c] = next_time
                    que.append((next_r, next_c, next_key, next_time))

        # 그냥 대기
        if v[p][next_mod][r][c] > next_time:
            que.append((r, c, p, next_time))
            v[p][next_mod][r][c] = next_time
    # print("s")
    #
    # et = time.time() - st
    # # cnt +=1
    # # print()
    # # print()
    # print(et)
    # # print(sum_time)
    # # print(check_precious_time)



    # 키 위치를 내가 만들어서 그걸 줄 수 있다.