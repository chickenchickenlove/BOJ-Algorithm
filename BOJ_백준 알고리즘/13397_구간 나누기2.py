import sys


def sol(value,m,my_list) :
    min_= 9876543210
    max_= -1
    cnt = 1
    for num in my_list :
        min_ = min(num, min_)
        max_ = max(num, max_)
        if max_ - min_ <= value :
            continue
        else :
            min_ = num
            max_ = num
            cnt += 1



    if cnt <= m : return True
    else : return False




n,m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))


l = 0
r = 9876543210
answer = 9876543210
while l <= r :
    mid = (l+r)//2
    if sol(mid,m,my_list) :
        r = mid - 1
        answer = min(answer,mid)
    else :
        l = mid + 1

print(answer)

#최소, 최대를 구간별로 설정한다
#최대, 최소에 대한 연산을 설정해서 그 값보다 커지면 구간 초기화한다. 한번만 만족시키면 된다.



