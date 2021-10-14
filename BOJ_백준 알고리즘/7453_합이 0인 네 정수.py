import sys

n = int(sys.stdin.readline().rstrip())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a = []
b = []
for i in range(n) :
    for j in range(n) :
        a.append(my_list[i][0] + my_list[j][1])
        b.append(my_list[i][2] + my_list[j][3])

a = sorted(a)
b = sorted(b)
answer = 0

for num in a :
    l,r = 0, len(b)-1
    lower = 9876543210
    l_flag = False
    while l <= r :
        mid = (l+r) // 2
        if b[mid] >= (-num) :
            r = mid - 1
            if b[mid] == (-num) :
                lower = min(lower, mid)
                l_flag = True
        else :

            l = mid + 1

    l,r = 0, len(b)-1
    upper = 0
    u_flag = False
    while l <= r :
        mid = (l+r) // 2
        if b[mid] > (-num) :
            r = mid - 1
        else :
            if b[mid] == (-num) :
                upper = max(upper, mid)
                u_flag = True
            l = mid + 1

    if u_flag and l_flag :
        answer += (upper - lower + 1 )



print(answer)


