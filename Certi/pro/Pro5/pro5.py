# solution.py


# main.py
import sys
from solution import init, addCafe, eraseCafe, order, beBuddy, recommend

CMD_INIT = 100
CMD_ADD_RESTAURANT = 200
CMD_REMOVE_RESTAURANT = 300
CMD_ORDER = 400
CMD_BE_FRIEND = 500
CMD_RECOMMEND = 600


def run():
    query = int(input())
    ok = False
    n = 0
    for i in range(query):
        # print(f"now query = {i}")
        input_iter = iter(input().split())
        cmd = int(next(input_iter))
        if cmd == CMD_INIT:
            n = int(next(input_iter))
            list_px = list(map(int, input().split()))
            list_py = list(map(int, input().split()))
            init(n, list_px, list_py)
            ok = True
        elif cmd == CMD_ADD_RESTAURANT:
            cid = int(next(input_iter))
            x = int(next(input_iter))
            y = int(next(input_iter))
            addCafe(cid, x, y)
        elif cmd == CMD_REMOVE_RESTAURANT:
            cid = int(next(input_iter))
            eraseCafe(cid)
        elif cmd == CMD_ORDER:
            uid = int(next(input_iter))
            cid = int(next(input_iter))
            order(uid, cid)
        elif cmd == CMD_BE_FRIEND:
            tid = int(next(input_iter))
            uid = int(next(input_iter))
            beBuddy(tid, uid)
        elif cmd == CMD_RECOMMEND:
            uid = int(next(input_iter))
            # print("recommand", uid, i)
            ret = recommend(uid)
            ans = int(next(input_iter))
            if ans != ret:
                # print("Here", ans , ret, i)

                ok = False
    return ok


if __name__ == '__main__':
    sys.stdin = open('input.txt', 'r')
    inputarray = input().split()
    TC = int(inputarray[0])
    MARK = int(inputarray[1])

    for testcase in range(1, TC + 1):
        score = MARK if run() else 0
        print("#%d %d" % (testcase, score), flush=True)