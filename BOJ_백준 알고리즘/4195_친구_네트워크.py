import sys
from collections import defaultdict
sys.setrecursionlimit(100000)


def find(a) :
    if d[a] == a :
        return a
    else :
        d[a] =  find(d[a])
        return d[a]

def union(a,b) :
    a = find(a)
    b = find(b)

    if a == b :
        return rank[a]

    else :
        if rank[a] >= rank[b] :
            rank[a] += rank[b]
            rank[b] = 0
            d[b] = a
            return rank[a]
        else :
            rank[b] += rank[a]
            rank[a] = 0
            d[a] = b
            return rank[b]


t = int(sys.stdin.readline().rstrip())
for _ in range(t) :
    my_set = set()
    n = int(sys.stdin.readline().rstrip())
    d = defaultdict(str)
    rank = defaultdict(int)
    for __ in range(n) :
        a,b = map(str,sys.stdin.readline().split())
        if a not in my_set :
            d[a] = a
            rank[a] = 1
            my_set.add(a)
        if b not in my_set :
            d[b] = b
            rank[b] = 1
            my_set.add(b)

        temp = union(a,b)
        print(temp)







