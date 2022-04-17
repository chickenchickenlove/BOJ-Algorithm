from heapq import heappop, heappush
from collections import defaultdict, deque
global hqMin,hqSort , memLoc, memOri, unUsedStart,  unUsedEnd, usedStart

# hq = []

def init(N):
    global unUsedStart, unUsedEnd, usedStart,n
    usedStart = {}
    unUsedStart = {}
    unUsedEnd = {}

    unUsedStart[0] = N
    unUsedEnd[N-1] = 0
    n = N

def allocate(size):
    global unUsedStart, unUsedEnd, usedStart,n
    START = -1

    START, SIZE = min(unUsedStart.items(), key=lambda x: (x[1], x[0]) if x[1] >= size else (99999999, 999999999))

    if SIZE < size : return -1

    END = START + SIZE - 1
    usedStart[START] = START + size - 1
    NEXT_START = START + size

    # unused 업데이트
    del unUsedStart[START]

    if SIZE - size > 0 :
        unUsedStart[NEXT_START] = SIZE - size
        unUsedEnd[END] = NEXT_START
    else :
        del unUsedEnd[END]

    return START

def deallocate(start):
    global unUsedStart, unUsedEnd, usedStart
    # 없는 경우 해제 하지 않음.

    if start not in usedStart : return -1

    # 있는 경우 메모리 해제
    # 현재 메모리를 해제한다.
    size = usedStart[start] - start + 1
    del usedStart[start]

    # 병합
    now_start, now_end = start, start+size-1

    # 있는 경우 왼쪽을 살펴본다.
    if (now_start - 1) in unUsedEnd :

        pre_end = now_start - 1
        pre_start = unUsedEnd[pre_end]
        # 없어져야 하는 노드
        # now_start, pre_end
        del unUsedEnd[pre_end]
        now_start = pre_start


    # 있는 경우 오른쪽을 살펴본다.
    if now_end + 1 in unUsedStart :
        next_start = now_end + 1
        next_end = next_start + unUsedStart[next_start] - 1
        #합쳐지는 경우 없어져야 하는 노드
        #1. next_start, now_end
        del unUsedStart[next_start]
        now_end = next_end

    SIZE = now_end - now_start + 1
    unUsedStart[now_start] = SIZE
    unUsedEnd[now_end] = now_start

    return size





import sys


CMD_INIT = 1
CMD_ALLOCATE = 2
CMD_DEALLOCATE = 3

def run():
    q = int(input())
    okay = False
    for i in range(q):
        inputarray = input().split()
        cmd = int(inputarray[0])
        if cmd == CMD_INIT:
            n = int(inputarray[1])
            init(n)
            okay = True
        elif cmd == CMD_ALLOCATE:
            size = int(inputarray[1])
            ans = int(inputarray[2])
            ret = allocate(size)
            if ans != ret:
                okay = False
        elif cmd == CMD_DEALLOCATE:
            start = int(inputarray[1])
            ans = int(inputarray[2])
            ret = deallocate(start)
            if ans != ret:
                okay = False
    return okay

if __name__ == '__main__':
    # sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score))


