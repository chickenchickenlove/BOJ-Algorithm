import sys


#이동하는 함수 생성 완료
def sol1() :
    global n
    stack = []
    for r in range(n) :
        for c in range(n) :
            while my_list[r][c] :
                mm,ss,dd = my_list[r][c].pop()
                next_rr, next_cc = r + ss * d[dd][0], c + ss * d[dd][1]
                while next_rr >= n:
                    next_rr = next_rr % n
                while next_rr <= -1:
                    next_rr = next_rr %n
                while next_cc >= n:
                    next_cc = next_cc % n
                while next_cc <= -1:
                    next_cc = next_cc % n
                stack.append((next_rr,next_cc,mm,ss,dd))
    while stack :
        rr,cc,mm,ss,dd = stack.pop()
        my_list[rr][cc].append((mm,ss,dd))


def sol2() :
    global n
    for r in range(n) :
        for c in range(n) :
            if len(my_list[r][c]) >= 2 :
                m_sum, odd, even, s_sum, cnt = 0,0,0,0,0
                while my_list[r][c] :
                    mm,ss,dd = my_list[r][c].pop()
                    m_sum += mm
                    s_sum += ss
                    cnt +=1
                    if dd % 2 == 0 : even +=1
                    else : odd +=1
                if odd * even == 0 : ddd = [0,2,4,6]
                else : ddd = [1,3,5,7]
                next_mm, next_ss = m_sum//5 , s_sum // cnt
                if next_mm > 0 :
                    for dddd in ddd :
                        my_list[r][c].append((next_mm, next_ss,dddd))



d = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]




# 파이어볼 입력 완료
n,m,k = map(int,sys.stdin.readline().split())
my_list = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m) :
    r,c,m,s,b = map(int,sys.stdin.readline().split())
    my_list[r-1][c-1].append((m,s,b))

for _ in range(k) :
    sol1()
    sol2()

ans = 0
for r in range(n) :
    for c in range(n) :
        if len(my_list[r][c]) > 0 :
            for i in range(len(my_list[r][c])) :
                ans += my_list[r][c][i][0]

print(ans)