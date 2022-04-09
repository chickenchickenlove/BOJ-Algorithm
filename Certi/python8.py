import sys
from collections import defaultdict

my_dict = defaultdict(int)
cnt = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    my_string = sys.stdin.readline().rstrip()

    if my_dict[my_string] :
        my_dict[my_string] = 0
        cnt -=1
    else :
        my_dict[my_string] = 1
        cnt +=1

print(cnt)













