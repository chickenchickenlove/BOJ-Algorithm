import sys
from collections import deque
from collections import defaultdict
from heapq import nlargest


def oneFunc(myString):
    if len(myString) <= 15 :
        D.append(myString.lower())

def twoFunc(c):
    if c == 0 :
        D.sort()
    elif c == 1 :
        D.sort(reverse=True)
    elif c == 2 :
        D.sort(key = lambda x : [len(x),x])
    print(*D[:3])

def threeFunc(myString):
    if D :
        temp_string = "".join([D[0], myString.lower()])
        if len(temp_string) > 15 :
            temp_string = temp_string[:15]
        D[0] = temp_string
    print(temp_string)

D = []
for _ in range(int(sys.stdin.readline().rstrip())) :
    a,b = sys.stdin.readline().split()

    if a == "1" :
        oneFunc(str(b))
    elif a == "2" :
        twoFunc(int(b))
    elif a == "3" :
        threeFunc(str(b))