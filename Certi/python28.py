import sys
from collections import deque


def bfs() :
    global n
    que = deque()
    v = [[0 for _ in range(n)] for _ in range(n)]
    score = [[0 for _ in range(n)] for _ in range(n)]
    que.append((0,0,my_map[0][0]))

    while que :
        r,c,sco = que.popleft()

        for rr,cc in tra_list :
            next_r, next_c = r + rr, c + cc
            if -1 < next_r < n and -1 < next_c < n :
                # 방문한 적이 없고
                # 현재값보다 더 클 경우
                next_score = my_map[next_r][next_c] + sco
                if v[next_r][next_c] == 0 and score[next_r][next_c] < next_score :
                    que.append((next_r, next_c, next_score))
                    v[next_r][next_c] = 1
                    score[next_r][next_c] = next_score



    return score


    #마지막 값을 가지고 다음 값으로 간다. 더 크면 기록한다.




tra_list = [[1,0],[0,1],[0,-1]]


n = int(sys.stdin.readline().rstrip())
my_map = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for k in my_map :
    print(k)


print(bfs())

