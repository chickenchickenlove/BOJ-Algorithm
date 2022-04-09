import sys
from collections import defaultdict

def resolver() :
    return ','.join(map(str,(al_dict["A"], al_dict["C"], al_dict["G"],al_dict["T"])))

n = int(sys.stdin.readline().rstrip())
my_string = sys.stdin.readline().rstrip()
my_dict = defaultdict(int)
al_dict = defaultdict(int)

l,r = 0,-1

while r-l+1 != n:
    r +=1
    if len(my_string) == r:
        break
    else :
        al_dict[my_string[r]] +=1

if r-l+1 < n :
    print(0)
    exit()

ans = 0
key = resolver()
my_dict[key] +=1

ans = max(ans, my_dict[key])


while r < len(my_string) :
    al_dict[my_string[l]] -=1
    l +=1
    r += 1
    if r == len(my_string) :
        break
    al_dict[my_string[r]] +=1

    key = resolver()
    my_dict[key] +=1

    ans = max(ans, my_dict[key])

print(ans)
