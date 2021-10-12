import sys


def sol(value, k) :
    my_sum = 0
    cnt = 0
    for num in my_list :
        if my_sum + num >= value :
            cnt +=1
            my_sum = 0
        else :
            my_sum += num
    if cnt >= k : return True
    else : return False

n,k = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))

l = 0
r = 9876543210


answer = 0
while l <= r :
    m = (l+r+1) // 2
    if sol(m,k) :
        l = m + 1
        answer = max(answer, m)
    else :
        r = m - 1




print(answer)









