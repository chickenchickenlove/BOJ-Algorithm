import sys

n,d = map(int,sys.stdin.readline().split())
my_list = []
for _ in range(n):
    my_list.append(tuple(map(int,sys.stdin.readline().split())))
my_list = sorted(my_list, key = lambda x: (x[0],x[1]))
l,r,ans,skew,my_sum  = 0,0,0,0,0

while 1 :
    if r <= len(my_list) - 1 :
        if l <= r :
            if skew < d :
                my_sum += my_list[r][1]
                ans = max(ans, my_sum)
                r +=1
            else :
                my_sum -= my_list[l][1]
                l += 1
    if r == len(my_list) or l > r :
        break
    skew = my_list[r][0] - my_list[l][0]

print(ans)



