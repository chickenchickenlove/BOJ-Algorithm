import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().strip())
A = [input().strip() for _ in range(n)]


# Hash Table 등록
# 1. for 문 돌리면서 좌상단 좌표를 등록해준다.
# n = 10이면, 6까지는 해줘야함. --> 10-4 = 6까지 해줘야함. n-4 + 1 까지 해줘야함.
# 리스트가 몇개가 들어가야하나? 9개만 쓴다고 하면 2^9개가 들어가야함.
htab = [[] for _ in range(2**9)]


#Hash Table 등록#########################################
#9개를 기준으로 한다.
#누적합으로 개선할 수도 있을 듯.
# - : 0 , + :1 로 표현한다.
def gethash(arr, x,y):
    hash = 0
    for i in range(3) :
        for j in range(3) :
            hash = hash*2 + int(arr[x+i][y+j] == "+") # 이런 식으로 Hash 값을 구할 수 있다.
    return hash

for i in range(n-4+1) :
    for j in range(n-4+1) :
        htab[gethash(A,i,j)].append((i,j))
#########################################

def check(x,y):
    # 범위가 벗어나는 경우
    if x+m > n or y+m > n: return 0

    # m개의 줄에 대해서 비교한다.
    for i in range(m) :
        #각 열의 문자열이 나옴
        if A[x+i][y:y+m] != B[i] : return 0
    return 1

for _ in range(int(input())):
    m = int(input())
    B = [input().strip() for _ in range(m)]

    hash = gethash(B,0,0)
    cnt = 0
    for x,y in htab[hash] :
        if check(x,y) : cnt +=1
    print(cnt)




