import sys
from solution import init, allocate, deallocate

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
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])
    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score))