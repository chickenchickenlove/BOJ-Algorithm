import sys

def dfs(cow, farm, cow_num, v) :
    global ans
    if v[cow_num] == 1: return False
    v[cow_num] = 1

    for farm_num in cow[cow_num] :
        if farm[farm_num] == 0 or dfs(cow, farm, farm[farm_num],v) :
            farm[farm_num] = cow_num
            return True
    return False

n,m = map(int,sys.stdin.readline().split())

#소 배열
#농장 배열
cow = [[] for _ in range(n+1)]
farm = [0 for _ in range(m+1)]

for i in range(1, n+1):
    a, *b = map(int,sys.stdin.readline().split())
    for k in b :
        cow[i].append(k)




for cow_num in range(1, n+1) :
    v = [0 for _ in range(n + 1)]
    dfs(cow, farm, cow_num, v)

ans = 0
for k in farm :
    if k > 0 :
        ans +=1


print(ans)



