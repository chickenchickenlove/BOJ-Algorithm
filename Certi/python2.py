import sys
from collections import deque
from collections import defaultdict
from heapq import nlargest

def my_register(pid, salary, c, j, p ):
    # pid = str(pid)
    my_dict[pid] = [c,j,p,salary,pid]

def my_cancel(pid):
    try :
        del my_dict[pid]
    except :
        pass

def my_update(pid,flag, x):
    try :
        my_dict[pid][flag] = x
    except :
        pass

def hire_min():
    my_pid = min(my_dict.items(), key = lambda item : [item[1][3],item[1][4]])[0]
    print(my_pid)
    del my_dict[my_pid]

def hire_max():
    answer_list = []
    for _ in range(3) :
        try :
            my_pid = max(my_dict.items(), key=lambda item: [item[1][0] + item[1][1] + item[1][2], item[1][4]])[0]
            answer_list.append(my_pid)
            del my_dict[my_pid]
        except :
            pass
    print(*answer_list)


my_dict = {}

# input
for _ in range(q := int(sys.stdin.readline().rstrip())):
    cmdList = list(map(str, sys.stdin.readline().split()))
    cmd = cmdList[0]
    data = list(map(int,cmdList[1:]))

    if cmd == "register" :
        my_register(*data)
    elif cmd == "hire_min" :
        hire_min(*data)
    elif cmd == "hire_max":
        hire_max(*data)
    elif cmd == "update" :
        my_update(*data)
    elif cmd == "cancel":
        my_cancel(*data)






