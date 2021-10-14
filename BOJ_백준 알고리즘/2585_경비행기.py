import sys
from collections import deque
import math

def bfs(n,my_list,value,k) :
    que = deque()
    my_set = set()
    for x,y in my_list :
        my_set.add((x,y))
    my_set.add((10000,10000))
    que.append((0,0,0))

    while que :
        x,y,cnt = que.popleft()
        stack = []
        if x == 10000 and y == 10000:
            return True

        for xx,yy in my_set :
            #print(math.ceil(((xx-x)**2 + (yy-y)**2)**0.5))
            if xx == 10000 and yy == 10000 and math.ceil(((xx-x)**2 + (yy-y)**2)**0.5) <= value :
                return True
            if math.ceil(((xx-x)**2 + (yy-y)**2)**0.5) <= value and cnt + 1 <= k :
                que.append((xx,yy, cnt+1))
                stack.append((xx,yy))




        while stack :
            xx,yy = stack.pop()
            my_set.discard((xx,yy))

    return False





n,k = map(int,sys.stdin.readline().split())
my_list = []
for _ in range(n) :
    x,y = map(int,sys.stdin.readline().split())
    my_list.append((x,y))


l = 0
r = 10000
answer = 9876543210
while l < r :
    m = (l+r)//2
    if bfs(n,my_list,m,k) :
        r = m-1
        answer = min(answer,m)
    else :
        l = m+1

print(math.ceil((answer*0.1)))
