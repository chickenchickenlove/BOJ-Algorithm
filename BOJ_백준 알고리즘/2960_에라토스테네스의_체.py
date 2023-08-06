import sys
n,k = map(int,sys.stdin.readline().split())
my_list = [0 for _ in range(n+1)]
my_cnt = 0
answer = 0


for i in range(2,n+1) :
    if my_list[i] == 0 :
        my_cnt +=1
        my_list[i] = 1
        if my_cnt == k :
            answer = i



        for z in range(2,n+1) :
            if i*z>= n+1 :
                break
            if my_list[i*z] == 0 :
                my_list[i*z] = 1
                my_cnt+=1
                if my_cnt == k :
                    answer = i*z
    if answer != 0 :
        print(answer)
        break