import sys
from collections import deque


def sol(n,m,my_map, p_castle, distance, p):

    que = deque()
    stack = []
    fix_count = 0

    while p_castle[p]:
        pr, pc = p_castle[p].pop()
        que.append((pr,pc,0))
        v[pr][pc] = 0

    while que :
        r,c,dis = que.popleft()
        next_dis = dis + 1

        for rr,cc in tra_list:
            next_r, next_c = r + rr, c + cc

            if next_dis > distance:
                break

            # 이 경우에만 뭔가 할 수 있음.
            if -1 < next_r < n and -1 < next_c < m:

                # 한번도 방문한 적이 없고
                if v[next_r][next_c] == 9876543210 and my_map[next_r][next_c] == ".":

                    # 변경점이 발생한 경우
                    if my_map[next_r][next_c] != p:
                        fix_count +=1
                        stack.append((next_r, next_c))
                        que.append((next_r, next_c, next_dis))
                        v[next_r][next_c] = 0


    # 맵에 업데이트
    if fix_count!= 0 :
        answer_castle[p] += fix_count
        while stack :
            r,c = stack.pop()
            my_map[r][c] = p
            p_castle[p].append((r,c))
        return True

    return False



tra_list = [[1,0],[0,1],[-1,0],[0,-1]]


#변수 초기화
n,m,p = map(int,sys.stdin.readline().split())
temp = list(map(int,sys.stdin.readline().split()))
p_list = [0]
for i in temp:
    p_list.append(i)

p_castle = [[] for _ in range(p+1)]
my_map = [[] for _ in range(n)]
for i in range(n):
    ss = str(sys.stdin.readline().rstrip())
    for s in ss:
        if s == "." or s == "#":
            my_map[i].append(s)
        else:
            my_map[i].append(int(s))

v = [[9876543210 for _ in range(m)] for _ in range(n)]
for r in range(n) :
    for c in range(m) :
        if my_map[r][c] != "."  and my_map[r][c] != "#":
            now_castle = my_map[r][c]
            p_castle[now_castle].append((r,c))



# 정답값
answer_castle = [0 for _ in range(p+1)]
for idx in range(len(p_castle)):
    answer_castle[idx] = len(p_castle[idx])


while 1 :

    going_flag = False
    for ppp in range(1, p+1):
        check = sol(n, m, my_map, p_castle, p_list[ppp], ppp)
        if check :
            going_flag = True

    if not going_flag:
        break

print(" ".join(map(str, answer_castle[1:])))