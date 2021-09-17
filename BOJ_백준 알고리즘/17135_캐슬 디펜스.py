import sys
import itertools
from collections import deque

# 궁수의 공격범위가 매초 1씩 늘어난다고 봐도 될 것 같다. 시작부터


def sol(combi, my_list,n,m,d) :
    que = deque()

    v = [[0 for _ in range(m)] for _ in range(n)]
    que.append((d, 0))
    answer = 0

    while que :
        dis,cnt = que.popleft()
        if cnt == n :
            break

        stack = []
        for rr,cc in combi :
            ef = 'F'
            for dd in range(dis + 1):
                for j in range(m):
                    for i in range(n-1 - cnt,-1,-1) :


                        if abs(rr-i) + abs(cc-j) <= dd and v[i][j] == 0 and my_list[i][j] == 1  :
                            stack.append((i,j))
                            ef = 'T'
                            break
                    if ef == 'T':
                        break
                if ef == 'T':
                    break

        while stack :
            rr,cc = stack.pop()
            if v[rr][cc] == 0 :
                answer +=1
            v[rr][cc] = 1


        que.append((dis + 1, cnt +1))


    return answer


n,m,d = map(int, sys.stdin.readline().split())
my_list = []
for _ in range(n) :
    my_list.append(list(map(int,sys.stdin.readline().split())))

my_list.append([0]*m)
arch = []
for i in range(m) :
    arch.append((n,i))

combis = list(itertools.combinations(arch,3))

answer = 0
for combi in combis :
    answer = max(answer,sol(combi, my_list,n,m,d))

print(answer)
