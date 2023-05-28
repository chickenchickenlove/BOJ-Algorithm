import sys
def sol(lv,R,C,cnt) :
    global r
    global c
    if lv == 1 :
        if R == r and c== C:
            print(cnt)
        elif C+1 == c and R == r :
            print(cnt+1)
        elif R+1 == r and C == c :
            print(cnt+2)
        elif R+1 == r and C+1 ==c :
            print(cnt+3)
        return

    else :
        idx = (2**(lv-1)) // 2
        cnt_lv = ((2**lv)**2) // 4
        if r <= R and c <= C :
            sol(lv-1,R - idx, C - idx,cnt)
        elif r <= R and c > C :
            sol(lv-1, R - idx  , C + idx , cnt + cnt_lv)
        elif r > R and c <= C :
            sol(lv - 1, R + idx, C - idx    , cnt + cnt_lv * 2   )
        elif r > R and c > C :
            sol(lv - 1, R + idx, C + idx, cnt + cnt_lv * 3 )


n,r,c = map(int,sys.stdin.readline().split())
r = r+1
c = c+1
sol(n, (2**n)//2, (2**n)//2,0)

