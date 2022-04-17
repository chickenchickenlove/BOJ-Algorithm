### main.py

import sys
from solution import init, add, search

CMD_INIT = 1
CMD_ADD = 2
CMD_SEARCH = 3

MAX_N = 100
boothId = [0 for _ in range(MAX_N)]
duration = [0 for _ in range(MAX_N)]
capacity = [0 for _ in range(MAX_N)]
bidResult = [0 for _ in range(MAX_N)]
numResult = [0 for _ in range(MAX_N)]


def run():
    global boothId, bidResult, duration, capacity, numResult
    query = int(input())
    correct = False
    for i in range(query):
        # print(i, correct)

        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            boothN = int(input())
            for j in range(boothN):
                boothId[j], duration[j], capacity[j] = map(int, input().split())
            init(boothN, boothId, duration, capacity)
            correct = True
        elif cmd == CMD_ADD:
            tick = int(next(input_iter))
            idx = int(next(input_iter))
            guestNum = int(next(input_iter))
            priority = int(next(input_iter))
            ans = int(next(input_iter))
            if correct:
                ret = add(tick, boothId[idx], guestNum, priority)
            if ans != ret:
                correct = False
        elif cmd == CMD_SEARCH:
            tick = int(next(input_iter))
            findCnt = int(next(input_iter))
            if correct:
                search(tick, findCnt, bidResult, numResult)
            for j in range(findCnt):
                idx = int(next(input_iter))
                num = int(next(input_iter))
                if boothId[idx] != bidResult[j] or num != numResult[j]:
                    correct = False
        else:
            correct = False

    return correct


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)
