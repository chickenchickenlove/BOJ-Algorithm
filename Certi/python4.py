import sys
from collections import deque

for _ in range(int(sys.stdin.readline().rstrip())):
    my_string = str(sys.stdin.readline().rstrip())
    lq,rq = deque(), deque()
    for c in my_string :
        if c == "<":
            if lq : rq.appendleft(lq.pop())
        elif c == ">":
            if rq : lq.append(rq.popleft())
        elif c == "-":
            if lq : lq.pop()
        else : lq.append(c)

    print(''.join([*lq,*rq]))

