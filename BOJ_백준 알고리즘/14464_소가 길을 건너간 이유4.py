import sys
c,n = map(int,sys.stdin.readline().split())
c_list = [int(sys.stdin.readline().rstrip()) for _ in range(c)]
v_list = [0 for _ in range(c)]
c_list = sorted(c_list)
n_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
n_list = sorted(n_list, key = lambda x : (x[1],x[0]))
answer = 0
idx = 0

for s,e in n_list :

    for idx, value in enumerate(c_list) :
        if s<= value <= e and v_list[idx] == 0 :
            v_list[idx] = 1
            answer +=1
            break
print(answer)