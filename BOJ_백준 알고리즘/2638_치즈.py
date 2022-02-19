import sys
from collections import deque


# 외곽 부분에서 시작되는 공기를 모두 2로 처리해준다.
def remove_outer_air(n,m, check_map, my_map):
    que = deque()
    que.append((0,0))
    check_map[0][0] = 2

    while que :
        r,c   = que.popleft()
        for rr, cc in tra_list:
            next_r, next_c = r + rr , c + cc
            if -1 < next_r < n and -1 < next_c < m:
                if my_map[next_r][next_c] == 0 and check_map[next_r][next_c] == 0 :
                    check_map[next_r][next_c] = 2
                    que.append((next_r, next_c))
    return check_map

def find_inner_space(n, m, check_map, my_map):

    visit_map = createMap(n, m)

    for r in range(n):
        for c in range(m):
            #공기 + 방문한 적이 없을 때 탐색한다.
            if my_map[r][c] == 0 and check_map[r][c] == 0 and visit_map[r][c] == 0 :

                que = deque()
                inner, cheese = 1,0
                que.append((r,c))
                stack = [(r,c)]
                cheese = set()

                while que :
                    rr,cc = que.popleft()

                    for rrr,ccc in tra_list:
                        next_r,next_c = rr + rrr, cc + ccc
                        # 맵 안에 있을 때
                        if -1 < next_r < n and -1 < next_c < m  :
                            # 치즈 일 경우
                            # 치즈는 다른 사람들이 체크를 해야하기 때문에 집합으로 중복 제거한다.
                            if (next_r, next_c) not in cheese and my_map[next_r][next_c] == 1:
                                cheese.add((next_r, next_c))


                            #방문한 적 없고, 공기일 경우
                            #방문한 적이 없고, 공기면 아니면 카운트 올리고 que에 넣는다.
                            elif check_map[next_r][next_c] == 0 and my_map[next_r][next_c] == 0 and visit_map[next_r][next_c] == 0  :

                                inner +=1
                                que.append((next_r, next_c))
                                stack.append((next_r, next_c))
                                visit_map[next_r][next_c] = 1


                # 치즈가 더 많은 경우, 반드시 내부다.
                if inner < len(cheese):
                    while stack :

                        rrrr,cccc = stack.pop()
                        check_map[rrrr][cccc] = 1


def check_remove(n,m,check_map, my_map):

    stack = []
    for r in range(n):
        for c in range(m):

            #치즈면 확인
            if my_map[r][c] == 1:
                # 초기값 셋팅
                cnt = 0
                # 4방향을 확인한다.
                for rr,cc in tra_list:
                    next_r, next_c = r + rr, c + cc
                    if -1 < next_r < n and -1 < next_c < m:
                        # 공기 + 외부인지 확인한다 ( check_map == 1이면 내부공기다 )
                        if my_map[next_r][next_c] == 0 and check_map[next_r][next_c] == 2:
                            # 공기 + 외부가 맞으면, 카운트 하나 늘려준다
                            cnt +=1

                # 2변 이상 접촉 했으면, 제거될 치즈로 넣어준다.
                if cnt >= 2 :
                    stack.append((r,c))

    # 제거될 치즈가 없음
    if len(stack) == 0 :
        return True

    # 제거될 치즈가 있음.
    else :
        while stack:
            # 치즈를 모두 제거해준다.
            r, c = stack.pop()
            my_map[r][c] = 0
        return False



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]


def createMap(n,m):
    return [[0 for _ in range(m)] for _ in range(n)]


n,m = map(int,sys.stdin.readline().split())
my_map = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]



ans = 0
while 1:

    # 내/외부 공기 체크용 맵 생성
    check_map = createMap(n, m)

    # 외부 공기 삭제
    check_map = remove_outer_air(n,m , check_map, my_map)

    # 내부 공기인지 확인함.
    find_inner_space(n, m, check_map, my_map)

    # 내부 공기정보 넣어주고, 치즈 삭제함.
    remove_none = check_remove(n, m, check_map, my_map)

    # 만약 제거된 것이 없다면 종료한다.
    if remove_none:
        print(ans)
        break

    # 제거된 것이 있다면 시간을 눌려준다.
    ans +=1

