import sys
from collections import deque

#spin 함수
def rotate() :
    global n,m,r,c,d
    fd = d
    while 1 :
        d -=1
        if d < 0 : d = 3
        next_r, next_c = r + k[d][0], c + k[d][1]
        if -1 < next_r < n and -1 < next_c < m :
            if my_map[next_r][next_c] == 0 and v[next_r][next_c] == 0 :
                r,c = next_r, next_c
                return True
        if d == fd : break
    return False

def backward() :
    global n,m,r,c,d
    if d == 0:
        next_r, next_c = r + k[2][0], c + k[2][1]
    elif d == 1 :
        next_r, next_c = r + k[3][0], c + k[3][1]
    elif d == 2 :
        next_r, next_c = r + k[0][0], c + k[0][1]
    elif d == 3 :
        next_r, next_c = r + k[1][0], c + k[1][1]

    if -1 < next_r < n and -1 < next_c < m :
        if my_map[next_r][next_c] == 0 :
            r,c = next_r, next_c
            return True
    return False


k=[[-1,0], [0,1],[1,0], [0,-1]]






#뒤로 도는 함수


n,m = map(int,sys.stdin.readline().split())
r,c,d = map(int,sys.stdin.readline().split())
my_map = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
v = [[0 for _ in range(m)] for _ in range(n)]
ans = 0

for i in range(n) :
    for j in range(m) :
        if my_map[i][j] == 1 :
            v[i][j] = 2



v[r][c] = 1
ans +=1
while 1 :
    if rotate() :
        v[r][c] = 1
        ans +=1

    else :
        if backward() :
            continue
        else :
            print(ans)
            exit()

# 청소를 한다
# rotate를 한다.
# rotate 결과가 true이면 전진하고 청소를 한다
# rotate 결과가 false이면 후진한다.
# 후진이 true이면 rotate 한다.
# 후진이 false이면 종료한다.