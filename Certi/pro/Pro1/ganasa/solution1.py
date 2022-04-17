from collections import defaultdict, deque

mainStr = deque()
htab = defaultdict(int)
global rev


def update(one):
    idx = 0 if rev else len(mainStr) - 1
    sub = ""
    for i in range(4) :
        if idx >= len(mainStr) or idx < 0 : break

        if rev:
            sub+= mainStr[idx]
            idx+=1
        else :
            sub = mainStr[idx] + sub
            idx -=1

        htab[sub] += one


def init(mStr: str):
    global rev
    mainStr.clear()
    htab.clear()
    rev = False

    for ch in mStr :
        mainStr.append(ch)
        update(1)

def pushBack(mWord: str):
    global rev
    for ch in mWord :
        if rev: mainStr.appendleft(ch)
        else : mainStr.append(ch)
        update(1)


def popBack(k: int):
    global rev
    for _ in range(k) :
        #빼고나서 업데이트 하면 안되니까, 빼고나서 업데이트 해준다
        update(-1)
        if rev: mainStr.popleft()
        else : mainStr.pop()


def reverseStr():
    global rev
    return False if rev else True


def getCount(mWord: str) -> int:
    if rev: return htab[mWord[::-1]]
    else : return htab[mWord]
