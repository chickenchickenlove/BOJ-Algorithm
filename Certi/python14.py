import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
A = [[] for _ in range(n)]
for idx in range(n) :
    temp = input().strip()
    for k in temp : A[idx].append(k)

#딕셔너리 설정.
#총 16개 나올꺼니, 17진수로 표현하자.
D = {"+": 0 , "-": 1}
key = 0

for r in range(n) :
    for c in range(n) :
        pass






