import sys
import itertools
from collections import deque


def bfs(combi, my_map, n, total_virus, virus_cnt):
    que = deque()
    cnt = 0
    max_time = 0

    # 바이러스 + 전파 가능한 곳이 총 n개가 있다.
    # 빼야하는 것은 비활성된 곳.
    # 비활성화된 곳은 전체 바이러스 - 활성 바이러스

    v = [[9876543210 for _ in range(n)] for _ in range(n)]

    for i, j in combi:
        v[i][j] = 0
        que.append((i, j, 0))

    while que:
        r, c, now_time = que.popleft()

        next_time = now_time + 1
        for rr, cc in tra_list:
            next_r = r + rr
            next_c = c + cc

            if -1 < next_r < n and -1 < next_c < n:
                if my_map[next_r][next_c] != 1:
                    if v[next_r][next_c] > next_time:
                        v[next_r][next_c] = next_time
                        que.append((next_r, next_c, next_time))
                        if my_map[next_r][next_c] == 0:
                            cnt += 1
                            if cnt == total_virus:
                                return next_time

    if total_virus == cnt:
        return 0

    return -1


tra_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def count_all(my_map, n):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if my_map[i][j] == 0:
                cnt += 1
    return cnt


def find_v(my_map, n):
    stack = []
    for i in range(n):
        for j in range(n):
            if my_map[i][j] == 2:
                stack.append((i, j))
    return stack


n, m = map(int, sys.stdin.readline().split())
my_map = []
for _ in range(n):
    my_map.append(list(map(int, sys.stdin.readline().split())))

virus = find_v(my_map, n)

combis = list(itertools.combinations(virus, m))
total_count = count_all(my_map, n)

answer = 9876543210
answer1 = 0

for combi in combis:
    temp = bfs(combi, my_map, n, total_count, len(virus) - m)
    if temp != -1:
        answer = min(answer, temp)

if answer != 9876543210:
    print(answer)
else:
    print(-1)


