import itertools
import sys
from collections import deque
from collections import defaultdict

def bfs(my_stack, trace_list) :
    global my_list
    global ans
    global k_list


    que = deque()
    sz, sr,sc =  trace_list[0]
    v = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]



    qqq = defaultdict(int)
    www = defaultdict(int)
    for idx, value in enumerate(k_list) :
        qqq[idx] = value

    for idx, value in enumerate(my_stack) :
        www[idx] = value

    # my_list 0번째는 전체 배열의 값
    # my_list 1번째는 돌아간 순서의 값
    # my_list 2번째는 행
    # my_list 3번째는 열
    v[sz][sr][sc] = 1
    if my_list[qqq[sz]][www[sz]][sr][sc] == 1 :
        que.append((sz,sr,sc,0))
    ez, er, ec = trace_list[1]


    while que :
        z,r,c,time = que.popleft()


        if z == ez and r == er and c == ec  :
            ans = min(ans, time)
            if time == 12 :
                print(12)
                exit()
            return True

        for zz,rr,cc in tra_list :
            next_z, next_r, next_c = z + zz, r + rr, c + cc
            if -1 < next_z < 5 and -1 < next_r < 5 and -1 < next_c < 5 :
                if my_list[qqq[next_z]][www[next_z]][next_r][next_c] == 1 and v[next_z][next_r][next_c] == 0 :
                    v[next_z][next_r][next_c] = 1
                    que.append((next_z, next_r, next_c, time +1 ))
    return False


def sol(depth, stack) :
    global k_list
    if depth == 5 :
        for finds in find_list:
            bfs(stack, finds)
    else :
        for i in range(4) :
            stack.append(i)
            sol(depth+1, stack)
            stack.pop()

tra_list = [[0,1,0],[0,0,1],[0,-1,0],[0,0,-1],[1,0,0],[-1,0,0]]
def rotate(now_list) :
    t =[[] for _ in range(5)]
    for j in range(5) :
        for i in range(4,-1,-1) :
            t[j].append(now_list[i][j])
    return t

my_list = [[] for _ in range(5)]

for i in range(5) :
    temp_list = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]
    my_list[i].append(temp_list)
    for q in range(3) :
        temp_list = rotate(temp_list)
        my_list[i].append(temp_list)

ans = 9876543210
cnt = 0

find_list =[[[0,0,0],[4,4,4]],
            [[0,4,0],[4,0,4]],
            [[0,0,4],[4,4,0]],
            [[0,4,4],[4,0,0]]]


## 굳이 맵을 복사하지 않아도 괜찮을 것 같다.


k = [0,1,2,3,4]
k1 = list(itertools.permutations(k,5))
for idx, k_list in enumerate(k1) :
    level = 0
    sol(0,[])

if ans == 9876543210 :
    print(-1)
else :
    print(ans)