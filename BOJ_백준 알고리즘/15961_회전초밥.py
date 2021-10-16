import sys
n,d,k,c = map(int,sys.stdin.readline().split())
my_list = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
dd = [0 for _ in range(d+1)]
l,r =0,0
now_cnt = 0
answer = 0
for i in range(0,k) :
    if dd[my_list[i]] == 0 :
        now_cnt +=1
    r = i
    dd[my_list[i]] +=1

r_cnt = 0
while r_cnt < n :
    r +=1
    if r == n : r = 0
    if dd[my_list[r]] == 0 :
        now_cnt +=1
    dd[my_list[r]] +=1
    if dd[my_list[l]] - 1 == 0 :
        now_cnt -=1
    dd[my_list[l]] -=1
    l +=1
    if l == n : l = 0
    if dd[c] == 0 : answer = max(now_cnt+1, answer)
    else :answer = max(now_cnt,answer)
    r_cnt +=1
print(answer)

