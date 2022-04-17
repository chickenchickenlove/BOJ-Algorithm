# main.py
import sys
from solution import init, addRestaurant, addValue, bestValue, regionalValue

CMD_INIT = 1
CMD_ADD_RESTAURANT = 2
CMD_ADD_VALUE = 3
CMD_BEST_VALUE = 4
CMD_REGIONAL_VALUE = 5


def run():
    numQuery = int(sys.stdin.readline())
    isCorrect = False
    mRoads = [[0, 0] for _ in range(50)]

    for q in range(numQuery):
        inputs = iter(sys.stdin.readline().split())
        cmd = int(next(inputs))

        if cmd == CMD_INIT:
            N = int(next(inputs))
            M = int(next(inputs))
            for i in range(M):
                mRoads[i][0] = int(next(inputs))
                mRoads[i][1] = int(next(inputs))
            init(N, M, mRoads)
            isCorrect = True

        elif cmd == CMD_ADD_RESTAURANT:
            mCityID = int(next(inputs))
            mName = next(inputs)
            addRestaurant(mCityID, mName)

        elif cmd == CMD_ADD_VALUE:
            mName = next(inputs)
            mScore = int(next(inputs))
            addValue(mName, mScore)

        elif cmd == CMD_BEST_VALUE:
            mStr = next(inputs)
            userAns = bestValue(mStr)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

        elif cmd == CMD_REGIONAL_VALUE:
            mCityID = int(next(inputs))
            mDist = int(next(inputs))
            userAns = regionalValue(mCityID, mDist)
            ans = int(next(inputs))
            if userAns != ans:
                isCorrect = False

    return isCorrect


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)