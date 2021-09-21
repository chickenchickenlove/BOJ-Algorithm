import sys


def find(a) :
    if d[a] < 0 :
        return a
    else :
        d[a] = find(d[a])
        return d[a]


def union(a,b) :
    a = find(a)
    b = find(b)

    if a == b :
        return

    else :
        if d[a] >= d[b] :
            d[b] = a

        else :
            d[a] = b

    return




n,m,k = map(int,sys.stdin.readline().split())
money_list = [0]

d = [-1 for _ in range(n+1)]
temp = list(map(int,sys.stdin.readline().split()))
for idx,value in enumerate(temp) :
    money_list.append(value)
    d[idx + 1 ] = -value

for _ in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    union(a,b)

answer = 0
for i in range(1,len(d)) :
    if d[i] < 0 :
        answer = answer - d[i]


if k >= answer :
    print(answer)
else :
    print('Oh no')




