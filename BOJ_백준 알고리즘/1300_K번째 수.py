import sys


def binary_search(start,end,m) :
    l = start
    r = start * end
    answer = 0

    while l <= r :
        mid = (l+r+1) // 2
        if mid > m :
            r = mid - 1
        else :
            l = mid + 1
            answer = mid



    return answer // start


def sol(m,n) :
    answer = 0
    for i in range(1,n+1) :
        answer += binary_search(i,n,m)
    return answer


n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())
l,r = 1,n**2

answer = 9876543210
while l <= r :
    m = (l+r)//2

    temp = sol(m,n)
    if temp < k :
        l = m +1
    else :
        r = m - 1
        answer = min(answer,m)



print(answer)