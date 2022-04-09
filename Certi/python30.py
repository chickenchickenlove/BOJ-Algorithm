import sys


# sys.stdin = open("input.txt")
input = sys.stdin.readline



n = int(input().strip())
my_list = list(map(int,input().split()))
my_list.sort()
q = int(input().strip())
query = list(map(int,input().split()))

ans_list = []
for q in query :

    l,r = 0, len(my_list)-1
    ans = 9876543210
    while l <= r :
        mid = (l+r)//2

        if q < my_list[mid]:
            r = mid - 1
        elif my_list[mid] < q:
            l = mid + 1
        else :
            ans = mid
            break
    if ans == 9876543210 : ans_list.append(-1)
    else : ans_list.append(ans)

print(" ".join(map(str,ans_list)))
















