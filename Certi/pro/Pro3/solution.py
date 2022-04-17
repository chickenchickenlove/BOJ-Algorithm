from collections import defaultdict


my_string_list = []
myDict = defaultdict(list)


def init(N: int, stri: list) -> None:
    global my_string_list, myDict, realDict
    my_string_list = []
    myDict = defaultdict(list)
    realDict = defaultdict(int)

    my_string_list = stri

def addDict(word: list) -> None:
    global my_string_list, myDict, realDict
    myWord = ''.join(map(str, word))
    for i in range(len(word)):
        temp_string = "".join(map(str, word[:i] + ["*"] + word[i+1:]))
        myDict[temp_string].append(myWord)
    myDict[myWord].append(myWord)


def removeDict(word: list) -> None:
    global my_string_list, myDict, realDict
    myWord = ''.join(map(str,word))
    for i in range(len(word)):
        temp_string = "".join(map(str, word[:i] + ["*"] + word[i + 1:]))
        myDict[temp_string].remove(myWord)
    myDict[myWord].pop()

def correctWord(start: int, end: int) -> int:
    global my_string_list
    myString = ''.join(map(str, my_string_list[start:end+1]))
    fixList = myString.split("_")
    cnt = 0
    for idx,fixString in enumerate(fixList) :
        if myDict[fixString] : continue
        flag = False

        for i in range(len(fixString)):
            searchString = ''.join(map(str,fixString[:i] + "*" + fixString[i+1:]))

            if len(myDict[searchString]) > 0 :
                myDict[searchString].sort()
                if not flag :
                    fixList[idx] = myDict[searchString][0]
                    flag = True
                if flag :
                    fixList[idx] = min(myDict[searchString][0], fixList[idx])
        if flag :
            cnt +=1

    return_list = [c for c in "_".join(map(str,fixList))]
    for i in range(len(return_list)) :
        my_string_list[start+i] = return_list[i]

    return cnt


def destroy(result: list) -> None:
    global my_string_list, myDict, realDict
    result[::] = my_string_list



### solution.py ###



### main.py ###
import sys
from typing import List

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