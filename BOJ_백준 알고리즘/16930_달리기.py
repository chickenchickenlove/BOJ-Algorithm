import sys
import heapq
import time
from collections import deque

# 다익스트라를 쓴다.
# 우선순위 힙을 쓴다. 왜냐하면 가중치를 가졌기 때문이다.
# 갈 수 있는 만큼 가는 것이 좋을까? 아니면 쪼끔씩 다 가는 것이 좋을까? 쪼끔씩 다 가는 것이 좋다.
# 왜냐하면 갈 수 있는만큼 다 갔을 때는 마지막이기 때문이다.
# 따라서, 한 점이 있으면 k만큼 체크하고 bfs를 돌려준다. (4방향으로)
# 현재 위치는 최소값이니 현재위치를 기준으로 업데이트를 해준다.
# 그리고 다음 값들 중에 방문하지 않은 놈이면 현재 위치 + 시간을 더해서 업데이트 해주고 우선순위 큐에 넣어준다.

# 이동한 거리를 기준으로 넣어야지
# 마지막에 이동한 거리가 얼마인지를 넣자

def bfs(sr,sc,er,ec, visited,value,k, n , m ) :
    global cnt
    que = deque()
    # hq = []

    # 초기화 해줌.
    value[sr][sc] = 0
    visited[sr][sc] = 1

    #최소힙으로 구현한다.
    que.append((0,sr,sc))

    # dis = abs(er-sr) + abs(ec-sc)
    # heapq.heappush(hq,(0,dis,0,sr,sc))


    #다 돌리고 나와야할 듯함.
    # while hq :
    while que :


        # time, dis ,move,r,c = heapq.heappop(hq)
        time, r, c = que.popleft()
        next_time = time + 1

        # print(r, c)

        # print(r,c)
        #
        # if r == er and c == ec :
        #     return

        for rr,cc in tra_list :
            # cnt치고 k만큼 올라간다. 그런데 이 때, 올라가다가 벽을 한번이라도 만나면 그 순간 멈춰야한다.

            for multiple in range(1,k+1) :
                next_r, next_c = r + rr * multiple, c + cc * multiple

                # 경계 조건 안에서
                if -1 < next_r < n  and -1 < next_c < m :

                    #벽인 경우면 이 방향으로 더 못 뛴다.
                    if my_list[next_r][next_c] == "#":
                        break

                    if value[next_r][next_c] <= value[r][c] :
                        break

                    # 벽이 아니면 더 뛸 수 있음.
                    # 방문한 적이 없고
                    # 현재 위치의 값 + 시간을 더 했을 때 값이 최소값이면 한번 더 간다.
                    if visited[next_r][next_c] == 0 and value[next_r][next_c] > next_time and value[next_r][next_c] > value[r][c]:
                        cnt +=1
                        que.append((next_time, next_r, next_c))
                        visited[next_r][next_c] = 1
                        value[next_r][next_c] = next_time

                        #dis가 두번째임
                        next_dis = abs(er - next_r) + abs(ec - next_c)
                        # heapq.heappush(hq, (next_time, next_dis,-multiple ,next_r, next_c))



                else :
                    #경계조건을 만나면 더 갈 필요가 없다.
                    break










tra_list = [[1,0],[-1,0],[0,-1],[0,1]]




n,m,k = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
for idx in range(n) :
    temp = sys.stdin.readline().rstrip()
    for q in temp :
        my_list[idx].append(q)

sr,sc,er,ec = map(lambda x: x-1 ,map(int,sys.stdin.readline().split()))


#k가 너무 증가하면 문제가 있다.
#k를 어떻게 좀 더 줄일 수 있을까?
# n,m,k=200,200,200
# my_list = [["." for _ in range(m)] for _ in range(n)]
# sr,sc,er,ec = 0,0,n-1,m-1
#

# 방문 배열





visited = [[0 for _ in range(m)] for _ in range(n)]
# 최단거리 배열
value = [[9876543210 for _ in range(m)] for _ in range(n)]




cnt = 0
# st = time.time()
bfs(sr,sc,er,ec, visited, value, k,n, m)
# print(time.time() - st)

if value[er][ec] == 9876543210 :
    print(-1)
else :
    print(value[er][ec])

# print(cnt)