import sys


def dfs(num,cnt,my_list,visit_list) :
    if cnt == 4 :
        print(1)
        exit()
    else :
        visit_list[num] = 1
        for k in my_list[num] :
            if visit_list[k] == 0 :
                dfs(k,cnt +1, my_list,visit_list)
                visit_list[k] = 0
        visit_list[num] = 0
    return False


n,m = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
visit_list = [0 for _ in range(n)]
for i in range(m) :
    a,b = map(int,sys.stdin.readline().split())
    my_list[a].append(b)
    my_list[b].append(a)

for i in range(len(my_list)) :
    flag = dfs(i,0,my_list,visit_list)
    if flag == True :
        break
if flag == False :
    print(0)