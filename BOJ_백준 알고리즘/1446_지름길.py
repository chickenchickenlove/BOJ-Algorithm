import sys
N,D = map(int,sys.stdin.readline().split())
my_list = []
for i in range(N) :
    my_list.append(list(map(int,sys.stdin.readline().split())))
my_list = sorted(my_list,key = lambda x : (x[0],x[1],x[2]))
d = [i for i in range(D+1)]


for i in my_list :
    a,b,c = i
    if b <= D :
        d[b] = min(d[a] + c,d[b])
    for kk in range(a,D+1) :
        d[kk] = min(d[kk-1] + 1 , d[kk])



print(d[D])