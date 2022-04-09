import sys
from collections import deque



def my_insert(que, pos, value):
    if pos == 0:
        que.appendleft(value)
    else :
        que.append(value)
    return que

def my_erase(que, pos, value) :
    my_que = deque()
    if pos == 0 :
        my_que = calc(my_que, que, value)
    else :
        que.reverse()
        my_que = calc(my_que, que, value)
        my_que.reverse()
    return my_que

def calc(my_que, que, value) :
    cnt = 0
    while que:
        now_value = que.popleft()
        if now_value < value:
            my_que.append(now_value)
        else:
            if cnt < 3:
                cnt += 1
            else:
                my_que.append(now_value)
    return my_que

def my_sort(que, value) :
    return deque(sorted(que, key = lambda x : [abs(value - x), x]))

def my_print(que, pos) :
    if pos == 0 :print(*que)
    else :
        print(*list(que)[::-1])

que = deque()
for _ in range(int(sys.stdin.readline().rstrip())):

    temp = list(map(int,sys.stdin.readline().split()))
    if temp[0] == 1 :
        que = my_insert(que, temp[1], temp[2])
    elif temp[0] == 2 :
        que = my_erase(que, temp[1], temp[2])
    elif temp[0] == 3 :
        que = my_sort(que, temp[1])
    elif temp[0] == 4 :
        my_print(que, temp[1])