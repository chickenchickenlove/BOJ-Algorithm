import sys
from collections import deque

def rotate() :
    que1 = deque()
    que2 = deque()
    for i in range(n-1,-1,-1) :
        que1.append(f1[i])
        que2.append(r1[i])
    for i in range(n) :
        que1.append(f2[i])
        que2.append(r2[i])
    que1.append(que1.popleft())
    que2.append(que2.popleft())
    for i in range(n-1,-1,-1) :
        f1[i] = que1.popleft()
        r1[i] = que2.popleft()
    for i in range(n):
        f2[i] = que1.popleft()
        r2[i] = que2.popleft()

    r1[-1] = 0
    r2[-1] = 0
    return

def move() :
    for i in range(n-1,-1,-1) :
        if i == n-1 :
            r1[i] = 0
            r2[i] = 0
        elif i != n-1 :
            if f1[i+1] > 0 and r1[i] == 1 and r1[i+1] == 0 :
                f1[i+1] -=1
                r1[i] = 0
                r1[i+1] = 1
    if f1[0] > 0 :
        f1[0] -=1
        r1[0] = 1

    if r1[-1] == 1 :
        r1[-1] = 0

    return

def count_k() :
    cnt = 0
    for i in range(n) :
        if f1[i] == 0 :
            cnt +=1
        if f2[i] == 0 :
            cnt +=1
    return cnt




n,k = map(int,sys.stdin.readline().split())
temp = list(map(int,sys.stdin.readline().split()))
f1,f2,r1,r2 = [], [], [], []
for _ in range(n) :
    r1.append(0)
    r2.append(0)
cnt = 0
for num in temp :
    cnt +=1
    if cnt <= n :
        f1.append(num)
    else :
        f2.append(num)

f2 = f2[::-1]

ans = 0
while 1 :
    ans +=1
    rotate()
    move()
    now_k = count_k()

    #print(ans)
    #print(r1)
    #print(f1)
    #print(f2)
    #print('\n')
    if now_k >= k :

       break
print(ans)






