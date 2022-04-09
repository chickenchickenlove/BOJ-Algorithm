import sys
from collections import deque

def fill(stack, values):
    V = [0 for _ in range(10)]
    return_value = []
    for r,c in stack :
        for value in values :
            if V[value] == 0 and row[r][value] == 0 and col[c][value] == 0 :
                V[value] = 1
                row[r][value] = 1
                col[c][value] = 1
                my_list[r][c] = value
                return_value.append((r, c, value))
                break

    return return_value

def recovery(recovery_list):
    while recovery_list :
        r,c,value = recovery_list.pop()
        row[r][value] = 0
        col[c][value] = 0
        my_list[r][c] = 0

def sol(row, col, rec_cnt):
    if len(rec) == rec_cnt :
        for k in my_list : print(*k)
        exit()
    else :
        #먼저 사각형을 하나 잡는다.
        #사각형을 잡고 빈 것이 없을 때까지 채운다. (어떤게 부족한지 미리 찾는다) --> 채울 수 있는 경우에만 채우도록 한다.
        #사각형을 꺼내온다.

        nr, nc = rec[rec_cnt]
        my_set = set([i for i in range(1,10)])
        stack = []

        for rrr in range(nr, nr+3) :
            for ccc in range(nc, nc +3):
                if my_list[rrr][ccc] == 0 :
                    stack.append((rrr,ccc))
                else :
                    my_set.remove(my_list[rrr][ccc])
        my_set = deque(list(my_set))

        if my_set :
            for _ in range(len(my_set)+1) :
                print(rec_cnt)
                my_set.append(my_set.popleft())
                recovery_list = fill(stack, my_set)
                if len(recovery_list) == len(stack) :
                    sol(row,col, rec_cnt +1)
                recovery(recovery_list)
        else :
            sol(row,col,rec_cnt+1)






# sys.stdin = open("input.txt")
input = sys.stdin.readline


my_list = [list(map(int,input().split())) for _ in range(9)]

row = [[0 for _ in range(10)] for _ in range(9)]
for i in range(9) :
    for j in range(9) :
        value = my_list[i][j]
        row[i][value] = 1

col = [[0 for _ in range(10)] for _ in range(9)]
for i in range(9) :
    for j in range(9) :
        value = my_list[j][i]
        col[i][value] = 1


rec = []
for i in range(3) :
    for j in range(3) :
        r = i*3 if i != 0 else 0
        c = j*3 if j != 0 else 0
        rec.append((r,c))

sol(row,col,0)
