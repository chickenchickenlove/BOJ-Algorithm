import sys

def sol(depth, now_level, cctv, cctv_cnt) :
    global wall_cnt, answer, n, m, cctv_global_num
    if now_level == depth :
        answer = min(answer, n*m - (wall_cnt + cctv_cnt + cctv_global_num))
    else :
        r,c = cctv.pop()
        cctv_numm = my_list[r][c]
        for i in range(1,5) :
            stack = []
            stack = bfs(cctv_numm, i, my_list, stack, r,c)
            sol(depth, now_level + 1, cctv, cctv_cnt + len(stack))
            while stack :
                rr,cc = stack.pop()
                my_list[rr][cc] = 0


        cctv.append((r,c))


def bfs(cctv_num, cctv_status ,my_list, stack,sr,sc) :
    global n,m
    if cctv_status == 1 :
        directions = cctv1[cctv_num-1]
    elif cctv_status == 2 :
        directions = cctv2[cctv_num-1]
    elif cctv_status == 3 :
        directions = cctv3[cctv_num-1]
    else :
        directions = cctv4[cctv_num-1]

    for rr,cc in directions :

        next_r, next_c = sr,sc
        while 1 :
            next_r += rr
            next_c += cc
            if -1 < next_r < n and -1 < next_c < m :
                if my_list[next_r][next_c] == 6 :
                    break
                elif my_list[next_r][next_c] == 0 :
                    stack.append((next_r, next_c))
                    my_list[next_r][next_c] = 9
            else : break
    return stack









cctv1 = [[[1,0]],[[1,0],[-1,0]], [[1,0],[0,1]] , [[1,0],[0,1],[-1,0]], [[1,0],[0,1],[-1,0],[0,-1]]]
cctv2 = [[[0,1]],[[0,1],[0,-1]], [[0,1],[-1,0]] , [[0,1],[-1,0],[0,-1]], [[1,0],[0,1],[-1,0],[0,-1]]]
cctv3 = [[[-1,0]],[[1,0],[-1,0]], [[-1,0],[0,-1]] , [[-1,0],[0,-1],[1,0]], [[1,0],[0,1],[-1,0],[0,-1]]]
cctv4 = [[[0,-1]],[[0,1],[0,-1]], [[0,-1],[1,0]] , [[0,-1],[1,0],[0,1]], [[1,0],[0,1],[-1,0],[0,-1]]]








n,m = map(int,sys.stdin.readline().split())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
cctv = []
wall_cnt = 0
answer = 98756443210
cctv_global_num = 0
for i in range(n) :
    for j in range(m) :
        if my_list[i][j] != 0 and my_list[i][j] != 6 :
            cctv.append((i,j))
            cctv_global_num +=1
        elif my_list[i][j] == 6 :
            wall_cnt +=1

sol(cctv_global_num, 0, cctv, 0)
print(answer)













