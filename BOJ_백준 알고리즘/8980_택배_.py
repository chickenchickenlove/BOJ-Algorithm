import sys
n,c = map(int,sys.stdin.readline().split())
v = [0 for _ in range(n+1)]
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline().rstrip()))]
my_list = sorted(my_list, key = lambda x : (x[1], -x[0]))


answer = 0
for a,b,k in my_list :
    loads = k
    for idx in range(a-1,b-1) :
        loads = min(loads, c - v[idx])
    for idx in range(a-1,b-1) :
        v[idx] += loads
    answer += loads

print(answer)





