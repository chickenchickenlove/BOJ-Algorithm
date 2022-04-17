### solution.py ###



### main.py ###
import sys
from typing import List
from solution import init, addDict, removeDict, correctWord, destroy

ADD = 100
REMOVE = 200
CORRECT = 300


def run():
    len = int(sys.stdin.readline())
    buf_b1 = list(sys.stdin.readline()[0:len])

    init(len, buf_b1)

    cmdCount = int(sys.stdin.readline())

    ret_val = 1

    for i in range(cmdCount):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == ADD:
            buf_s = list(next(inputs))
            addDict(buf_s)

        elif cmd == REMOVE:
            buf_s = list(next(inputs))
            removeDict(buf_s)

        elif cmd == CORRECT:
            start = int(next(inputs))
            end = int(next(inputs))
            ret = correctWord(start, end)
            ans = int(next(inputs))
            if ret != ans:
                ret_val = 0

    buf_b2 = list(0 for _ in range(len + 1))
    destroy(buf_b2)

    buf_b1 = list(sys.stdin.readline())

    for i in range(len):
        if buf_b1[i] != buf_b2[i]:
            ret_val = 0

    return ret_val


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)