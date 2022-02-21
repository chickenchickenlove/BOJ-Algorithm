import sys

n,k = map(int,sys.stdin.readline().split())
my_list = list(map(int,sys.stdin.readline().split()))


l,r,ans,odd_cnt = 0,-1,0,0
temp_cnt = 0

while True :


    if odd_cnt <= k :
        ans = max(ans, temp_cnt - odd_cnt)

    #Validation
    if odd_cnt <= k :
        r += 1

        #경계 조건 확인
        if r >= n :
            break

        if my_list[r] % 2 == 1 :
            odd_cnt +=1
        temp_cnt +=1


    # Validation
    else :

        if my_list[l] % 2 == 1 :
            odd_cnt -=1
        temp_cnt -=1
        l+=1

        #경계 조건 확인
        if l > r :
            break

print(ans)










