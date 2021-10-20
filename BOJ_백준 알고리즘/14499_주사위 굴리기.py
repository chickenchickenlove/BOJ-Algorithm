import sys
from collections import deque



def sol(command, r, c, Row, Col):
    global n,m

    #동쪽으로 도는 거
    if command == 1:
        next_r, next_c = r, c + 1
        if -1 < next_r < n and -1 < next_c < m :
            temp = Col.popleft()
            Col.append(temp)
            if my_map[next_r][next_c] == 0 :
                my_map[next_r][next_c] = Col[1]
                Row[1] = Col[1]
            else :
                Col[1] = my_map[next_r][next_c]
                Row[1] = my_map[next_r][next_c]
                my_map[next_r][next_c] = 0
            print(Col[3])
            Row[3] = Col[3]
        else :
            return r,c

    #서쪽으로 도는 거
    elif command == 2 :
        next_r, next_c = r, c - 1
        if -1 < next_r < n and -1 < next_c < m :
            temp = Col.pop()
            Col.appendleft(temp)
            if my_map[next_r][next_c] == 0 :
                my_map[next_r][next_c] = Col[1]
                Row[1] = Col[1]
            else :
                Col[1] = my_map[next_r][next_c]
                Row[1] = my_map[next_r][next_c]
                my_map[next_r][next_c] = 0
            print(Col[3])
            Row[3] = Col[3]
        else :
            return r,c

    elif command == 3 :
        next_r, next_c = r-1, c
        if -1 < next_r < n and -1 < next_c < m :
            temp = Row.pop()
            Row.appendleft(temp)
            if my_map[next_r][next_c] == 0 :
                my_map[next_r][next_c] = Row[1]
                Col[1] = Row[1]
            else :
                Col[1] = my_map[next_r][next_c]
                Row[1] = my_map[next_r][next_c]
                my_map[next_r][next_c] = 0
            print(Row[3])
            Col[3] = Row[3]
        else :
            return r,c
    else :
        next_r, next_c = r + 1, c
        if -1 < next_r < n and -1 < next_c < m:
            temp = Row.popleft()
            Row.append(temp)
            if my_map[next_r][next_c] == 0:
                my_map[next_r][next_c] = Row[1]
                Col[1] = Row[1]
            else:
                Col[1] = my_map[next_r][next_c]
                Row[1] = my_map[next_r][next_c]
                my_map[next_r][next_c] = 0
            print(Row[3])
            Col[3] = Row[3]
        else:
            return r, c

    return next_r, next_c

n,m,r,c,k = map(int,sys.stdin.readline().split())
Row,Col = deque(), deque()
for _ in range(4) :
    Row.append(0)
    Col.append(0)
my_map = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
command_list = list(map(int,sys.stdin.readline().split()))


rr,cc = r,c
for command in command_list :
    rr,cc = sol(command,rr,cc,Row, Col)

