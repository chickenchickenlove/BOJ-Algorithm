import sys
from collections import deque

def sol(stack,time) :
    global n,m, infested
    next_stack = []
    while stack :
        r,c = stack.pop()

        for rr,cc in tra_list :
            next_r, next_c = r + rr , c + cc

            if -1 < next_r < n and -1 < next_c < m :
                if my_list[next_r][next_c] == 1 :
                    next_stack.append((next_r, next_c))
                    my_list[next_r][next_c] = 0
                    infested = time
    return next_stack

def sol2() :
    global n,m
    ans = 0
    for i in range(n) :
        for j in range(m) :
            if my_list[i][j] == 1 :
                ans+=1
    return ans



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]
m,n = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
in_map = [[0 for _ in range(m)] for _ in range(n)]
for idx in range(n) :
    temp = sys.stdin.readline().rstrip()
    for k in temp :
        my_list[idx].append(int(k))
sc,sr = map(int,sys.stdin.readline().split())
sc = sc-1
sr = sr-1
my_list[sr][sc] = 0
infested = 0
stack =[(sr,sc)]
time = 1


while 1 :
    stack = sol(stack,time)
    time +=1
    if not stack :
        break



# 전멸 시간
print(infested + 3)
print(sol2())



