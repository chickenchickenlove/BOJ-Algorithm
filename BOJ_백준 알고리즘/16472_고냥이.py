import sys
from collections import defaultdict


n = int(sys.stdin.readline().rstrip())
my_str = str(sys.stdin.readline().rstrip())
my_dict = defaultdict(int)

l = -1
r = -1
now_cnt = 0
answer = 0
now_length = 0


while l < len(my_str)-1 and r < len(my_str)-1 :

    #r을 늘렸을 때, 카운트보다 작으면 r을 움직인다.
    #그렇지 않으면 l을 움직인다.
    if r + 1 < len(my_str) :

        if my_dict[my_str[r+1]] == 0 and now_cnt +1 <= n :
            r += 1
            my_dict[my_str[r]] +=1
            now_cnt +=1
            now_length +=1
        elif my_dict[my_str[r+1]] == 0 and now_cnt + 1 > n :
            l +=1
            my_dict[my_str[l]] -=1
            if my_dict[my_str[l]] == 0 :
                now_cnt -=1
            now_length -=1
        elif my_dict[my_str[r+1]] > 0 and now_cnt <= n :
            r +=1
            my_dict[my_str[r]] +=1
            now_length +=1
    else :
        l +=1
        my_dict[my_str[l]] -= 1
        if my_dict[my_str[l]] == 0:
            now_cnt -= 1
        now_length -= 1


    answer = max(now_length, answer)

print(answer)








