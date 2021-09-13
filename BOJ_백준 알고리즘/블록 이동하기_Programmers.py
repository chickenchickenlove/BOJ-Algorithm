from collections import deque
def bfs(board) :

    # 초기 변수 셋팅
    n = len(board)
    que = deque()
    v = [[[9876543210 for _ in range(n)] for _ in range(n)] for _ in range(2)]

    #시작점 방문처리.
    que.append((0,0,0,1,0,0))
    v[0][0][0] = 0
    v[0][0][1] = 0



    while que :
        #ar,ac = 점 a의 좌표
        #br,bc = 점 b의 좌표
        #status = 현재 로봇이 놓여있는 상태(0은 가로, 1은 세로)
        ar, ac, br, bc, now_time, status = que.popleft()


        #목적지 도착했는지 판단
        if (ar == n-1 and ac == n -1) or (br == n-1 and bc == n-1) :
             return now_time
        if br == n-1 and bc == n-1 :
            return now_time

        next_time = now_time + 1

        #회전하지 않고 그대로 가는 경우
        for rr, cc in tra_list :
            next_ar = ar + rr
            next_ac = ac + cc
            next_br = br + rr
            next_bc = bc + cc
            next_status = status
            if -1 < next_ar < n and -1 < next_br < n and -1 <  next_ac < n and -1 < next_bc < n :
                if board[next_ar][next_ac] == 0 and board[next_br][next_bc] == 0 :
                    if v[next_status][next_ar][next_ac] > next_time or v[next_status][next_br][next_bc] > next_time :
                        que.append((next_ar, next_ac, next_br, next_bc, next_time, next_status))
                        v[next_status][next_ar][next_ac] = min(next_time, v[next_status][next_ar][next_ac])
                        v[next_status][next_br][next_bc] = min(next_time, v[next_status][next_br][next_bc])


        if status == 1 :
            next_status = 0
        else :
            next_status = 1

        # a를 중심축으로 회전해서 가는 경우
        for rr, cc, in rotate :
            next_ar = ar + rr
            next_ac = ac + cc
            if -1 < next_ar < n and -1 < next_ac < n:
                # 회전하는 곳에서 벽이 있을 때, 뒤로 안감
                if board[next_ar][ac] == 1 or board[ar][next_ac] == 1 :
                    continue
                # 회전이 정상적으로 이루어 졌을 때
                if next_ar == br or next_ac == bc:
                    if board[next_ar][next_ac] == 0 and board[br][bc] == 0 :
                        if v[next_status][next_ar][next_ac] > next_time or v[next_status][br][bc] > next_time :
                            que.append((next_ar, next_ac, br, bc, next_time, next_status))
                            v[next_status][next_ar][next_ac] = min(next_time, v[next_status][next_ar][next_ac])
                            v[next_status][br][bc] = min(next_time, v[next_status][br][bc])


        # b를 중심축으로 회전해서 가는 경우
        for rr, cc, in rotate :
            next_br = br + rr
            next_bc = bc + cc
            if -1 < next_br < n and -1 < next_bc < n:

                # 회전하는 곳에서 벽이 있을 때, 뒤로 안감
                if board[next_br][bc] == 1 or board[br][next_bc] == 1 :
                    continue
                # 회전이 정상적으로 이루어 졌을 때
                if next_br == ar or next_bc == ac :
                    if board[next_br][next_bc] == 0 and board[ar][ac] == 0 :
                        if v[next_status][next_br][next_bc] > next_time or v[next_status][ar][ac] > next_time :
                            que.append((ar, ac, next_br, next_bc, next_time, next_status))
                            v[next_status][ar][ac] = min(next_time, v[next_status][ar][ac])
                            v[next_status][next_br][next_bc] = min(next_time,v[next_status][next_br][next_bc])





tra_list = [[1,0],[0,1],[-1,0],[0,-1]]
rotate = [[1,1], [1,-1],[-1,1],[-1,-1]]


def solution(board):
    answer = bfs(board)
    return answer



solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])

board = [[0,0,0,0,0],
[0,0,1,0,0],
[0,1,1,1,0],
[0,1,1,1,1],
[0,0,0,0,0]
]

print(solution(board))