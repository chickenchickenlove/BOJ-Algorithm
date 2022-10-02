import sys

def dfs(my_house,cordi,last_condition) :
    global my_cnt
    if cordi == [n,n] and my_house[n][n] == 0 :
        my_cnt += 1
    else :
        x, y = cordi
        my_condition = last_condition
        for k in tra_list :
            next_x = x + k[0]
            next_y = y + k[1]
            if 0 < next_x < n+1 and 0 < next_y < n+1 : #바운드리 조건 완료
                if k == [1,1] and my_house[x][y+1] == 0 and my_house[x+1][y] == 0 and my_house[next_x][next_y] == 0:
                    dfs(my_house,[next_x,next_y],0)
                elif k == [1,0] and my_house[next_x][next_y] == 0 and my_condition !=2 :
                        dfs(my_house,[next_x,next_y],1)
                elif k == [0,1] and my_house[next_x][next_y] == 0 and my_condition != 1 :
                        dfs(my_house,[next_x,next_y],2)

n = int(sys.stdin.readline().rstrip())
my_house = [[0] for _ in range(n+1)]
tra_list = [[1,0],[0,1],[1,1]]
my_cnt = 0


for p in range(1,n+1) :
    temp = list(map(int,sys.stdin.readline().split()))
    for k in temp :
        my_house[p].append(k)

if my_house[n][n] == 0 :
    dfs(my_house,[1,2],2)
print(my_cnt)
