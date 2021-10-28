import sys
from collections import deque


def move(r, c):
    cnt = 1
    while 1:
        next_r = r + cnt
        if r + cnt >= 12:
            break
        if my_list[next_r][c] == '.':
            my_list[next_r][c] = my_list[r][c]
            my_list[r][c] = '.'
        else:
            break
        r = next_r
    return


def bfs(my_list, sr, sc):
    que = deque()
    v = [[0 for _ in range(6)] for _ in range(12)]
    ss = my_list[sr][sc]
    v[sr][sc] = 1
    que.append((sr, sc))
    stack = [(sr, sc)]
    while que:
        r, c = que.popleft()
        for rr, cc in tra_list:
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < 12 and -1 < next_c < 6:
                if my_list[next_r][next_c] == ss and v[next_r][next_c] == 0:
                    v[next_r][next_c] = 1
                    que.append((next_r, next_c))
                    stack.append((next_r, next_c))
    if len(stack) >= 4:
        while stack:
            r, c = stack.pop()
            my_list[r][c] = '.'
        return True
    return False


tra_list = [[1, 0], [0, 1], [-1, 0], [0, -1]]
my_list = [[] for _ in range(12)]
for i in range(12):
    temp = str(sys.stdin.readline().rstrip())
    for k in temp:
        my_list[i].append(k)

answer = 0
while 1:
    f = 'T'
    for q in range(11, -1, -1):
        for w in range(6):
            move(q, w)
    for r in range(11, -1, -1):
        for c in range(6):
            if my_list[r][c] != '.':
                if bfs(my_list, r, c):
                    f = 'F'

    if f == 'T':
        print(answer)
        exit()
    answer += 1