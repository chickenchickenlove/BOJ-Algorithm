import sys


def sol(max_value) :
    global m
    tsum = 0
    gcnt = 0
    if my_list[0] <= max_value :
        tsum = my_list[0]
        gcnt +=1
    else : return False

    for idx in range(1,len(my_list)) :
        value = my_list[idx]
        if value > max_value :return False
        if max_value > tsum + value : tsum += value
        elif max_value == tsum + value:
            tsum += value
        elif max_value < tsum + value :
            gcnt +=1
            tsum = value

    if gcnt > m : return False
    return True


# sys.stdin = open("input.txt")
input = sys.stdin.readline

n,m = map(int,input().split())
my_list = list(map(int, input().split()))

ans = 9876543210
l,r = 0,ans


while l < r :
    mid = (l+r)//2
    if sol(mid):
        r = mid
        ans = min(ans,mid)
    else :
        l = mid + 1
print(ans)







