''' main.py '''
import sys
from typing import List
from solution import init, occur, cancel, position

INIT = 1
OCCUR = 2
CANCEL = 3
POSITION = 4


def run():
    queryCnt = int(sys.stdin.readline())
    isCorrect = False

    for i in range(queryCnt):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == INIT:
            N = int(next(inputs))
            parent = [int(next(inputs)) for _ in range(N)]
            init(N, parent)
            isCorrect = True

        elif cmd == OCCUR:
            timeStamp = int(next(inputs))
            caseID = int(next(inputs))
            townNum = int(next(inputs))
            prior = int(next(inputs))
            occur(timeStamp, caseID, townNum, prior)

        elif cmd == CANCEL:
            timeStamp = int(next(inputs))
            caseID = int(next(inputs))
            cancel(timeStamp, caseID)

        elif cmd == POSITION:
            timeStamp = int(next((inputs)))
            userAns = position(timeStamp)
            ans = int(next(inputs))

            # print(f'index : {i}, userAns = {userAns}, ans = {ans}')
            if userAns != ans:
                isCorrect = False

        else:
            isCorrect = False

    return isCorrect


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    SUCCESS = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = SUCCESS if run() else 0
        print("#%d %d" % (testcase, score), flush=True)