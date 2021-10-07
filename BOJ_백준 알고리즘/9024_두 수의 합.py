import sys


def binary_search(num,l,r, target,my_list) :
    while l < r :
        m = (l+r+1) // 2
        if target > num + my_list[m] :
            l = m
        elif target == num + my_list[m] :
            answer_list.append(0)
            return
        else :
            r = m
        if m == (l+r+1) //2 :
            break


    if l == r :


        answer_list.append((abs(target - num - my_list[r])))
    else :
        if abs(target - num + my_list[l]) > abs(target - num + my_list[r]) :
            answer_list.append((abs(target - num - my_list[r])))
        elif abs(target - num + my_list[l]) > abs(target - num + my_list[r]) :
            answer_list.append((abs(target - num - my_list[l])))
        else :
            answer_list.append((abs(target - num - my_list[l])))
            answer_list.append((abs(target - num - my_list[r])))



t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    m,k = map(int,sys.stdin.readline().split())
    my_list = list(map(int,sys.stdin.readline().split()))
    my_list = sorted(my_list)

    answer_list = []
    for i in range(0,len(my_list)-1) :
        binary_search(my_list[i],i+1,len(my_list)-1,k,my_list)

    answer_list = sorted(answer_list)
    #print(answer_list)
    cnt = 1


    if len(answer_list) >= 2 :
        while answer_list[cnt] == answer_list[0] :
            cnt +=1
            if len(answer_list) <= cnt :
                break

        print(cnt)
    else :
        print(1)













