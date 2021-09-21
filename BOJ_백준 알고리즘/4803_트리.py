import sys

def find(a) :
    if d[a] == a :
        return a
    else :
        d[a] = find(d[a])
        return d[a]


def union(a,b) :
    a,b = find(a), find(b)

    if a== b :
        return a
    else :
        if a in fail_set or b in fail_set :
            fail_set.add(a)
            fail_set.add(b)
        d[b] = a
        return -1


cnt = 1
while 1 :

    n,m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0 :
        break

    else :
        answer = 0
        my_set = set()
        fail_set = set()
        d = [i for i in range(n + 1 )]
        for _ in range(m) :
            a,b = map(int,sys.stdin.readline().split())
            temp = union(a,b)
            if temp != -1 :
                fail_set.add(temp)

        for i in range(1,len(d)) :
            find(i)
            if d[i] not in fail_set :
                my_set.add(d[i])



    aa = len(my_set)
    if aa > 1 :
        print(f'Case {cnt}: A forest of {aa} trees.')
    elif aa == 1 :
        print(f'Case {cnt}: There is one tree.')
    else :
        print(f'Case {cnt}: No trees.')


    cnt +=1

