import sys
from collections import deque


def bfs(s,e,a) :

    que = deque()
    my_dict = make_dict()


    que.append((s,0))


    while que :
        now_value, now_time = que.popleft()
        if now_value == e :
            print(now_time)
            return


        for k in range(0,10) :
            next_value = str(now_value)[:3] + str(k)
            next_value = int(next_value)
            if my_dict[next_value] == 0 and a[next_value] == 0 :
                que.append((next_value, now_time + 1 ))
                my_dict[next_value] = 1

        for k in range(0,10) :
            next_value = str(now_value)[:2] + str(k) + str(now_value)[3:]
            next_value = int(next_value)
            if my_dict[next_value] == 0 and a[next_value] == 0:
                que.append((next_value, now_time + 1))
                my_dict[next_value] = 1

        for k in range(0, 10):
            next_value = str(now_value)[:1] + str(k) + str(now_value)[2:]
            next_value = int(next_value)
            if my_dict[next_value] == 0 and a[next_value] == 0:
                que.append((next_value, now_time + 1))
                my_dict[next_value] = 1


        for k in range(1,10) :
            next_value = str(k) + str(now_value)[1:]
            next_value = int(next_value)
            if my_dict[next_value] == 0 and a[next_value] == 0:
                que.append((next_value, now_time + 1))
                my_dict[next_value] = 1

    print('IMPOSSIBLE')
    return

def make_dict() :
    my_dict = {}
    for idx in range(1000,10000) :

        my_dict[idx] = 0

    return my_dict

def che() :
    my_list = [0 for _ in range(10000)]

    for i in range(2,10000) :
        if my_list[i] == 0 :
            for j in range(2,10000) :
                if i*j < 10000 :
                    my_list[i*j] = 1
                else :
                    break
    my_list[0] = 1
    my_list[1] = 1
    return my_list


t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    s,e = map(int,sys.stdin.readline().split())
    my_list = che()
    bfs(s,e,my_list)



