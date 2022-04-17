import sys
from solution import getRank

N = 1000

ansRank = [0 for _ in range(N)]
isused = [0 for _ in range(N)]

MAXQUERY = 1000000

okay = False
querycount = 0


def query(K: int, sub: [int], opt: int):
    global querycount, okay

    if not okay or K < 5 or K > N or (opt != 0 and opt != 1) or querycount >= MAXQUERY:
        okay = False
        return -1

    querycount += 1

    if opt == 0:
        ret = N - 1
        for k in range(K):
            if sub[k] < 0 or sub[k] >= N or isused[sub[k]] == querycount:
                okay = False
                return -1

            isused[sub[k]] = querycount

            if ret > ansRank[sub[k]]:
                ret = ansRank[sub[k]]
        return ret
    else:
        ret = 0
        for k in range(K):
            if sub[k] < 0 or sub[k] >= N or isused[sub[k]] == querycount:
                okay = False
                return -1

            isused[sub[k]] = querycount

            if ret < ansRank[sub[k]]:
                ret = ansRank[sub[k]]
        return ret


callcount = 0
retRank = [0 for _ in range(N)]


def run():
    global N, okay, querycount, callcount

    okay = True

    for c in range(10):
        limit = 1200

        inputs = iter(sys.stdin.readline().split())
        for i in range(N):
            ansRank[i] = int(next(inputs))

        querycount = 0

        for i in range(N):
            isused[i] = 0

        if okay:
            getRank(retRank, query)

        if limit < querycount:
            okay = False

        if okay:
            for i in range(N):
                if ansRank[i] != retRank[i]:
                    okay = False

        callcount += querycount

    return okay


def main():
    global callcount

    sys.stdin = open('input.txt', 'r')
    TC, MARK = map(int, sys.stdin.readline().split())

    totalcount = 0
    for testcase in range(1, TC + 1):
        callcount = 0

        score = MARK if run() else 0
        print("#%d %d %d" % (testcase, score, callcount), flush=True)
        totalcount += callcount

    print("totalcount = %d, average = %.3lf" % (totalcount, (totalcount / (TC * 10))))


if __name__ == '__main__':
    main()