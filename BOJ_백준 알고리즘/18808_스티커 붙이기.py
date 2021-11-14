import sys


def sol1(temp) :
    r,c = len(temp), len(temp[0])
    next_r, next_c = c,r
    next_temp = [[0 for _ in range(next_c)] for _ in range(next_r)]
    for i in range(r) :
        for j in range(c) :
            next_temp[j][next_c - 1 - i] = temp[i][j]
    return next_temp


def sol2(limit, now) :
    global n,m,ans
    if limit == now :
        now_cnt = cnt()
        ans = max(ans,now_cnt)
        return
    else :
        for no in range(4) :
            now_temp = ddd[now][no]
            for sr in range(n) :
                for sc in range(m) :
                    stack = sol3(sr,sc,now_temp, my_list)
                    if stack :
                        break
                if stack :
                    break
            if stack : break
        sol2(limit, now+1)
        return

def sol3(sr,sc,now_temp, my_list) :
    global n,m
    my_stack = []
    f_flag = True
    for i in range(len(now_temp)) :
        for j in range(len(now_temp[i])):
            next_r, next_c = i + sr , j + sc
            if -1 < next_r < n and - 1 < next_c < m:
                if (my_list[next_r][next_c] == 0 and now_temp[i][j] == 1) :
                    continue
                elif (my_list[next_r][next_c] == 1 and now_temp[i][j] == 0) :
                    continue
                elif my_list[next_r][next_c] == 1 and now_temp[i][j] == 1 :
                    f_flag = False
            else : f_flag = False

    if f_flag :
        for i in range(len(now_temp)):
            for j in range(len(now_temp[i])):
                next_r, next_c = i + sr, j + sc
                if now_temp[i][j] == 1 :
                    my_list[next_r][next_c] = 1
        return True
    else :
        return False

def cnt() :
    global n,m
    cntcnt = 0
    for i in range(n) :
        for j in range(m) :
            if my_list[i][j] == 1 :
               cntcnt +=1
    return cntcnt



n,m,k = map(int,sys.stdin.readline().split())
my_list = [[0 for _ in range(m)] for _ in range(n)]
ddd = [[] for _ in range(k)]
for q in range(k) :
    r,c = map(int,sys.stdin.readline().split())
    temp = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
    ddd[q].append(temp)
    for _ in range(3) :
        temp = sol1(temp)
        ddd[q].append(temp)


ans = 0

sol2(k,0)
print(ans)