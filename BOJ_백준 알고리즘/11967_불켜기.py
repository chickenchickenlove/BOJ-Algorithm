import sys
from collections import deque

def sol(my_map, r,c):
    global  ans
    temp = 0
    while my_map[r][c] :
        rrr, ccc = my_map[r][c].pop()
        if f[rrr][ccc] == 0:
            f[rrr][ccc] = 1
            ans += 1
            temp +=1
    return temp


def bfs(n):
    global ans, my_map

    # 초기화
    que = deque()
    v[1][1] = 1
    f[1][1] = 1
    ans +=1


    que.append((1,1))
    sol(my_map, 1,1)

    while que :
        r,c = que.popleft()

        for rr,cc, in tra_list:
            next_r, next_c = r + rr, c + cc

            if 0 < next_r < n+1 and 0 < next_c < n+1:
                # 불이 켜져있고 예전에 방문한 적이 있는 경우 (이 때만 방문이 가능하다)
                if f[next_r][next_c] == 1 and ans > v[next_r][next_c]:
                    #한번도 이 방에서 불켠 적이 없으면, 불을 켜준다.
                    sol(my_map, next_r, next_c)
                    v[next_r][next_c] = ans
                    que.append((next_r, next_c))





# 변수 입력 받기
n, m = map(int,sys.stdin.readline().split())
my_map = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    sr,sc,dr,dc = map(int,sys.stdin.readline().split())
    my_map[sr][sc].append((dr,dc))
tra_list = [[1,0],[0,1],[-1,0],[0,-1]]


# 방문 배열을 만든다.
v = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 불 켜진 곳인지 확인 배열
f = [[0 for _ in range(n+1)] for _ in range(n+1)]

ans = 0
bfs(n)
print(ans)









# 불은 1,1에만 켜져있다.
# 불이 켜져있는 방에만 들어갈 수 있따.
# 이동은 상하좌우만 가능하다.
# #배시가 불을 켤 수 있는 방의 최대 개수는?


# 방문체크를 할 때..
# 불을 켠 상태가 바뀌지 않으면, 이전에 방문했던 곳은 방문할 필요가 없다.
# 불을 켠 상태가 되면 이전에 방문 했던 곳은 방문해야한다.
# 방 : N * N
# 한 방에는 여러 개의 스위치, 하나의 불을 조절하는 스위치 역시 여러개 있을 수 있다.
# 1. BFS를 돈다
# 2. 특정 위치에 도착하면, 방문한 적이 있는지 확인한다.
# 2-1. 방문한 적이 있으면, 현재 불이 켜져있는 수치와 방문 위치를 비교한다.
# 2-1. 이 때, 켜져있는 숫자가 더 크면 한번더 큐에 넣는다.
# 2-2. 해당 방에 방문한 적이 없으면, 방문의 스위치를 돌린다.
# 2-2-1. 스위치를 돌릴 때, 켜고자 하는 방의 스위치가 켜져있는지 확인한다. 없으면, COUNT를 올려준다.
# COUNT를 출력한다.





#