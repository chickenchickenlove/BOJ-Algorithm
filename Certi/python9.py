import sys
from collections import defaultdict


score_dict = defaultdict(int)
id_dict = defaultdict(int)
id = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    a,b = map(str,sys.stdin.readline().split())
    a = a.lower()
    if not id_dict[a] :
        id += 1
        id_dict[a] = id
        score_dict[a] = max(score_dict[a], int(b))
    else :
        score_dict[a] = max(score_dict[a], int(b))


    print(id_dict[a], score_dict[a])









