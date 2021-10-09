import sys



n,m,l = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.append(0)
my_list.append(l-1)
my_list = sorted(my_list)
start, end = 0,sys.maxsize
while start < end :
    mid = (start + end) // 2
    cnt = 0
    for i in range(0,len(my_list)-1) :
        if my_list[i+1] - my_list[i] > mid :
            cnt += (my_list[i+1] - my_list[i])// mid
            if (my_list[i+1] - my_list[i]) // mid == (my_list[i+1] - my_list[i])/mid :
                cnt -=1


    if cnt > m :
        start = mid + 1
    else :
        end = mid
        answer = mid



print(answer)


