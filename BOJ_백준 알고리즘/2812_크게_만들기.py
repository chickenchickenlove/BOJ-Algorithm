import sys
from collections import defaultdict



n,k = map(int,sys.stdin.readline().split())
kk = k
my_num = str(sys.stdin.readline().rstrip())
my_list = [int(c) for c in my_num]
answer_list = []

if n == 0 and k == 0 :
    print(0)
    exit()

for idx in range(0,len(my_list)-1) :
    value = my_list[idx]
    if k > 0 :
        if len(answer_list) == 0 :
            answer_list.append(value)

        else :
            if answer_list[-1] >= value  :
                answer_list.append(value)

            elif answer_list[-1] < value :
                while answer_list[-1] < value :
                    answer_list.pop()
                    k-=1
                    if len(answer_list) == 0 :
                        break
                    if k == 0 :
                        break
                answer_list.append(value)

    else :
        answer_list.append(my_list[idx])
if k > 0 :
    while k > 0 :
        if answer_list[-1] <= my_list[len(my_list) - 1]:
            answer_list.pop()
            k-=1
        else :
            break

    if k > 0 :
        pass
    else :
        answer_list.append(my_list[-1])

else :
    answer_list.append(my_list[-1])

while len(answer_list) > (n-kk) :
    answer_list.pop()


print(''.join(map(str,answer_list)))





