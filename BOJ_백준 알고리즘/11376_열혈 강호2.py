import sys

def dfs(man, work, man_num, v, depth) :
    if v[man_num] == 2 : return False
    v[man_num] +=1

    if depth == 0 :
        start_cnt = 0
        for work_num in man[man_num] :
            if work[work_num] == 0 or dfs(man, work, work[work_num], v, depth+1) :
                work[work_num] = man_num
                start_cnt +=1
            if start_cnt == 2 :
                return True
    # depth가 0이상인 경우
    else :
        for work_num in man[man_num]:
            if work[work_num] == man_num :
                continue

            if work[work_num] == 0 or dfs(man, work, work[work_num], v, depth+1):
                work[work_num] = man_num
                return True
    return False

n,m = map(int,sys.stdin.readline().split())
man = [[] for _ in range(n+1)]
work = [0 for _ in range(m+1)]
man_cnt = [0 for _ in range(n+1)]

for man_num in range(1, n+1):
    num, *works = map(int,sys.stdin.readline().split())
    for work_num in works :
        man[man_num].append(work_num)


for man_num in range(1, n+1) :

    v = [0 for _ in range(n+1)]
    dfs(man, work, man_num, v, 0)



ans = 0
for k in work :
    if k > 0:
        ans +=1
print(ans)



