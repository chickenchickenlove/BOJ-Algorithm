import sys


#수아가 이동한다.
def sua_move(sua, v, bo, my_map) :
    global n,m
    global ans_flag
    next_sua = []

    # 입력 받은 수아 배열의 값이 있으면, 4방향으로 이동한다.
    while sua :
        r,c = sua.pop()

        # 도착했는데 보물이면, 정답이므로 출력해준다.
        if (r,c) == bo :
            print("YES")
            ans_flag = True
            return

        # 4방향으로 이동한다.
        for rr,cc in tra_list :
            next_r, next_c = r + rr , c + cc

            if -1 < next_r < n and -1 < next_c < m :

                # 방문한 적이 없고, 이동가능한 곳이면 이동한다.
                if v[next_r][next_c] == 9876543210 and (my_map[next_r][next_c] == "." or my_map[next_r][next_c] == "T"):
                    v[next_r][next_c] = 0
                    next_sua.append((next_r, next_c))
    return next_sua


#해적 이동
def pirate_move(pirate,v,row_p, col_p) :
    next_pirate = []

    while pirate :

        r,c, time = pirate.pop()
        #현재 해적의 시간 확인
        next_time = time + 1

        for rr,cc in tra_list :
            next_r, next_c = r+rr, c+cc

            # 경계 체크
            if -1 < next_r < n and -1 < next_c < m :

                #한번도 방문한 적 없고 이동할 수 있는 곳이면
                if v[next_r][next_c] == 9876543210 and (my_map[next_r][next_c] == "." or my_map[next_r][next_c] == "T"):

                    # 각 행,렬에 도착한 최소 시간을 업데이트 해준다.
                    row_a[next_r] = min(row_a[next_r], next_time)
                    col_a[next_c] = min(col_a[next_c], next_time)

                    # 방문 처리 및 배열에 넣어줌.
                    next_pirate.append((next_r, next_c, next_time))
                    v[next_r][next_c] = next_time

    return next_pirate

# 수아 배열에 있는 수아들이 살아있을 수 있는지 확인한다.
def judge(sua, my_map, row_a, col_a, vp):
    next_sua = []

    while sua :
        sr,sc = sua.pop()

        # 현재 수아의 위치를 기준으로 row_a, col_a의 시간을 확인해본다.
        # 아직 해적이 이 행,렬에 도착하지 않았으면 수아는 반드시 살아남는다.
        if row_a[sr] == 9876543210 and col_a[sc] == 9876543210 :
            next_sua.append((sr,sc))
            continue


        # 수아의 4방향을 살핀다.
        # 1. 섬 or 해적을 만나기 전까지 한쪽 방향을 계속 올린다.
        # 2. 섬을 먼저 만나면 이 방향에서는 안전한다.
        # 3. 해적을 먼저 만나면 수아는 죽는다
        # 4. 해적을 만난다의 기준은, 해적이 이 배열을 방문한 적이 있는지를 확인한다.
        false_flag = False
        #처음 만나는게 섬인지 확인
        jc = sc
        while jc < m :
            jc +=1
            if jc == m :
                break

            if vp[sr][jc] != 9876543210 :
                false_flag = True
                break

            if my_map[sr][jc] == "I" :
                false_flag = False
                break

        if false_flag : continue

        jc = sc
        while jc >-1 :
            jc -=1
            if jc == -1 :
                break

            if vp[sr][jc] != 9876543210 :
                false_flag = True
                break

            if my_map[sr][jc] == "I" :
                false_flag = False
                break

        if false_flag: continue

        jr = sr
        while jr < n :
            jr += 1
            if jr == n:
                break

            if vp[jr][sc] != 9876543210:
                false_flag = True
                break

            if my_map[jr][sc] == "I":
                false_flag = False
                break

        if false_flag: continue

        jr = sr
        while jr > -1:
            jr -= 1
            if jr == -1:
                break

            if vp[jr][sc] != 9876543210:
                false_flag = True
                break

            if my_map[jr][sc] == "I":
                false_flag = False
                break
        if false_flag: continue

        #수아가 살았으면 배열에 넣어준다.
        next_sua.append((sr,sc))

    return next_sua


#그래프 탐색용 배열
tra_list = [[1,0],[0,1],[-1,0],[0,-1]]
dcol = [[0,-1], [0,1]]
drow = [[1,0], [-1,0]]


#입력 받기
n,m = map(int,sys.stdin.readline().split())
my_map = [[] for _ in range(n)]
for idx in range(n):
    temp = sys.stdin.readline().rstrip()
    for k in temp :
        my_map[idx].append(k)
        if k == "Y":
            sua = [(idx, len(my_map[idx]) - 1)]
        elif k == "V" :
            pirate = [(idx, len(my_map[idx])- 1, 0)]
        elif k == "T" :
            bo = (idx, len(my_map[idx]) - 1 )



# 해적 방문 체크 배열
vp = [[9876543210 for _ in range(m)] for _ in range(n)]
# 수아 방문 체크 배열
vs = [[9876543210 for _ in range(m)] for _ in range(n)]

# 해적이 각 행,열에 도착한 시간 확인 → 이 시간 이후로 항상 해적은 이 위치에 있을 수 있다.
row_a = [9876543210 for _ in range(n)]
col_a = [9876543210 for _ in range(m)]


#해적 + 수아 좌표 초기화
row_a[pirate[0][0]] = 0
col_a[pirate[0][1]] = 0
vp[pirate[0][0]][pirate[0][1]] = 0
vs[sua[0][0]][sua[0][1]] = 0

#수아가 보물에 갈 수 있는지 체크
ans_flag = False
while sua :

    #수아가 움직인다.
    sua = sua_move(sua, vs, bo, my_map)

    #해적이 움직인다.
    pirate = pirate_move(pirate, vp, row_a, col_a)

    #둘의 동작이 끝난 상태에서 살아있을 수 있는 수아의 상태를 찾아서 넘겨준다.
    sua = judge(sua, my_map, row_a, col_a, vp)


if not ans_flag :
    print("NO")