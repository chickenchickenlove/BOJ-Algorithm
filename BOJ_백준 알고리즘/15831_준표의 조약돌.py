import sys
n,b,w = map(int,sys.stdin.readline().split())
my_str = str(sys.stdin.readline().rstrip())
l,r,b_cnt,w_cnt = 0,-1,0,0
answer = 0
path = 0
while 1 :
    if b_cnt <= b :
        r +=1
        if r == len(my_str) :
            break
        path +=1
        if my_str[r] == 'W' :
            w_cnt +=1
        else :
            b_cnt +=1
            if b_cnt > b :
                while b_cnt > b  :
                    if my_str[l] == 'B' :
                        b_cnt -=1
                    else :
                        w_cnt -=1
                    l += 1
                    path -= 1

    if b_cnt <= b and w_cnt >= w:
        answer = max(answer, path)
print(answer)
