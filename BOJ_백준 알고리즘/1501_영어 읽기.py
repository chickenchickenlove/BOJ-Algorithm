import sys
from collections import defaultdict


n = int(sys.stdin.readline().rstrip())
my_dict = defaultdict(dict)
for _ in range(n) :
    my_str = str(sys.stdin.readline().rstrip())
    if len(my_str) == 1 :
        first_key = my_str[0]
    else :
        first_key = my_str[0] + my_str[-1]


    if len(my_str) >= 3 :
        second_key = ''.join(sorted(my_str[1:-1]))
    else :
        second_key = ''

    if second_key not in my_dict[first_key].keys() :
        my_dict[first_key][second_key] = 1
    else :
        my_dict[first_key][second_key] += 1




m = int(sys.stdin.readline().rstrip())
for _ in range(m) :
    my_str_ = list(map(str,sys.stdin.readline().split()))
    answer = 1
    for my_str in my_str_ :
        if len(my_str) == 1 :
            first_key = my_str[0]
        else :
            first_key = my_str[0] + my_str[-1]


        if len(my_str) >= 3 :
            second_key = ''.join(sorted(my_str[1:-1]))
        else :
            second_key = ''

        if second_key not in my_dict[first_key].keys():
            answer *= 0
        else :
            answer *= my_dict[first_key][second_key]

    print(answer)

