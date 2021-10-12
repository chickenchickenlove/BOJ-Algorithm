import sys
def binary_search(my_list, value, target) :
    l = 0
    r = len(my_list)-1
    answer_target = 9876543210
    answer_value = 9876543210



    while l <= r :
        m = (l+r) // 2
        if my_list[m] + value < target :
            if answer_target > abs(target - (my_list[m] + value)) :
                answer_target = abs(target - (my_list[m] + value))
                answer_value = my_list[m] + value

            l = m+1
        elif my_list[m] + value > target :
            if answer_target > abs(target - (my_list[m] + value)) :
                answer_target = abs(target - (my_list[m] + value))
                answer_value = my_list[m] + value
            r = m-1

        else :
            answer_target = 0
            answer_value = target
            break

    return answer_target, answer_value



#9007
# 중간에서 만나기로 모수 줄이고, 이분탐색으로 짝을 정한다
# 정렬 + 두 포인터
# answer 절대값, value값을 저장해서 구분한다.

for _____ in range(int(sys.stdin.readline().rstrip())) :
    k,n = map(int,sys.stdin.readline().split())
    c = []
    for _ in range(4) :
        c.append(list(map(int,sys.stdin.readline().split())))

    answer_target = 9876543210
    answer_value = 9876543210

    #가능한 합의 배열을 만든다

    q1 = []
    q2 = []
    for i in range(n) :
        for j in range(n) :
            q1.append(c[0][i] + c[1][j])
            q2.append(c[2][i] + c[3][j])

    q1 = sorted(q1)
    q2 = sorted(q2, reverse= True)



    start, end,length = 0,0,len(q1)
    while start < length and end < length :
        temp = q1[start] + q2[end]

        if abs(k-temp) < answer_target :
            answer_target = abs(k-temp)
            answer_value = temp
        elif abs(k-temp) == answer_target and temp < answer_value :
            answer_value = temp

        if temp < k : start += 1
        else : end +=1

    print(answer_value)

