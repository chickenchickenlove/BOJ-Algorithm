import sys
from collections import defaultdict

d = defaultdict(int)
k = defaultdict(int)
myKey = "aaaaaaaaaaaaaa"

for _ in range(int(sys.stdin.readline().rstrip())) :
    my_string = sys.stdin.readline().rstrip()

    temp = ""
    ans = myKey
    for c in my_string :
        temp += c

        if not k[temp] :
            k[temp] =1
            if len(ans) > len(temp) :
                ans = temp

    d[my_string] += 1
    if ans != myKey :
        print(ans)
    else :
        if d[my_string] == 1 :
            print(my_string)
        else :
            print(''.join(map(str,[my_string, d[my_string]])))





