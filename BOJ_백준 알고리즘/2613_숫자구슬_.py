import sys


def sol(group_cnt, value, my_list) :
    global answer_l
    #d 총합 관리 , dd는 갯수 관리
    d = [0 for _ in range(group_cnt)]
    dd = [0 for _ in range(group_cnt)]
    t_sum, t_cnt,g_cnt = 0,0,0
    answer_list = []
    for idx,num in enumerate(my_list) :
        if t_sum + num <= value :
            t_sum += num
            t_cnt +=1
        else :
            if num > value :
                return False
            d[g_cnt] = t_sum
            dd[g_cnt] = t_cnt
            t_sum = num
            t_cnt = 1
            g_cnt +=1
            if g_cnt > len(d)-1 :
                return False


        if idx == len(my_list) - 1 :
            t_cnt -=1
            d[g_cnt] = t_sum
            dd[g_cnt] = t_cnt
    if g_cnt > group_cnt  :
        return False

    for i in range(1, len(d)) :
        if dd[i] == 0 :
            q = i
            while dd[q] <= 1 :
                q -=1
                if q == -1 :
                    return False
            dd[q] -=1
            dd[i] = 1

    for i in range(len(dd)) :
        answer_l[i] = dd[i]





    return True





n,m = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))
my_list.append(0)

l = 0
r = 9876543210
answer = 9876543210
answer_l = [0 for _ in range(m)]
while l <= r :
    mid = (l+r) // 2
    if sol(m,mid,my_list) :
        r = mid -1
        answer = min(answer, mid)
    else :
        l = mid+1


print(answer)
print(' '.join(map(str,answer_l)))

