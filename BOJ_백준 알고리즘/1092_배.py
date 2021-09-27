import sys
n = int(sys.stdin.readline().rstrip())
crain = list(map(int,sys.stdin.readline().split()))
crain = sorted(crain, reverse= True)
c_idx = [0 for _ in range(n)]
m = int(sys.stdin.readline().rstrip())
load_list = list(map(int,sys.stdin.readline().split()))
load_list = sorted(load_list, reverse = True)
v = [0 for _ in range(m)]
cnt = 0
time = 0

if load_list[0] > crain[0] :
    print(-1)
    exit()

idx_list = []
while cnt != m :

    for name, value in enumerate(crain) :
        while 1 :
            now_idx = c_idx[name]
            if now_idx > m-1 :
                break
            if value >= load_list[now_idx] and v[now_idx] == 0 :
                v[now_idx] = 1
                cnt +=1
                if cnt == m :
                    print(time + 1 )
                    exit()
                c_idx[name] = now_idx + 1
                break

            c_idx[name] = now_idx + 1
    time +=1


