import sys

def return_value(copy_list, my_list,n) :
    for i in range(n) :
        for j in range(n) :
            my_list[i][j] = copy_list[i][j]
    return

def direction(my_list, n, d) :
    #위로 올라가는 것으로 가정
    v = [[0 for _ in range(n)] for _ in range(n)]


    if d == 0 :
        for j in range(n) :
            for i in range(1,n) :
                cnt = 0
                while (i - cnt) != 0 :
                    cnt +=1
                    # 0이면 옮긴다.
                    if my_list[i-cnt][j] == 0 :
                        my_list[i-cnt][j] = my_list[i-cnt+1][j]
                        my_list[i - cnt + 1][j] = 0
                    elif my_list[i-cnt][j] == my_list[i-cnt +1][j] and v[i-cnt][j] == 0 :
                        my_list[i-cnt][j] *= 2
                        my_list[i-cnt + 1 ][j] = 0
                        v[i-cnt][j] = 1
                        break
                    else : break


    elif d == 1 :
        for j in range(n) :
            for i in range(n-2,-1,-1) :
                cnt = 0
                while (i + cnt) != n-1 :
                    cnt +=1
                    # 0이면 옮긴다.
                    if my_list[i+cnt][j] == 0 :
                        my_list[i+cnt][j] = my_list[i+cnt-1][j]
                        my_list[i + cnt -1][j] = 0
                    elif my_list[i+cnt][j] == my_list[i+cnt -1][j] and v[i+cnt][j] == 0  :
                        my_list[i+cnt][j] *= 2
                        my_list[i+cnt - 1 ][j] = 0
                        v[i+cnt][j] = 1
                        break
                    else : break

    elif d == 2 :
        for i in range(n) :
            for j in range(1,n) :
                cnt = 0
                while (j - cnt) != 0 :
                    cnt +=1
                    # 0이면 옮긴다.
                    if my_list[i][j-cnt] == 0 :
                        my_list[i][j-cnt] = my_list[i][j-cnt+1]
                        my_list[i][j-cnt+1] = 0
                    elif my_list[i][j-cnt] == my_list[i][j-cnt +1] and  v[i][j-cnt] == 0:
                        my_list[i][j-cnt] *= 2
                        my_list[i][j-cnt + 1 ] = 0
                        v[i][j-cnt] = 1
                        break
                    else :
                        break




    elif d == 3 :
        for i in range(n) :
            for j in range(n-2,-1,-1) :
                cnt = 0
                while (j + cnt) != n-1 :
                    cnt +=1
                    # 0이면 옮긴다.
                    if my_list[i][j+cnt] == 0 :
                        my_list[i][j+cnt] = my_list[i][j+cnt-1]
                        my_list[i][j+cnt-1] = 0
                    elif my_list[i][j+cnt] == my_list[i][j+cnt -1] and v[i][j + cnt] == 0 :
                        my_list[i][j+cnt] *= 2
                        my_list[i][j+cnt -1] = 0
                        v[i][j+cnt] = 1
                        break
                    else :
                        break


def copy(my_list, n) :
    temp_list = [[] for _ in range(n)]
    for i in range(n) :
        for j in range(n) :
            temp_list[i].append(my_list[i][j])
    return temp_list


def sol(depth, now_cnt, n, my_list) :
    global answer
    if depth == now_cnt :
        for i in range(n) :
            for j in range(n) :
                if my_list[i][j] > answer : answer = my_list[i][j]
        return
    else :
        copy_list = copy(my_list, n)
        for i in range(0,4) :

            direction(my_list, n, i)
            sol(depth, now_cnt + 1 , n, my_list)
            return_value(copy_list, my_list, n)

        return


answer = 0
n = int(sys.stdin.readline().rstrip())
my_list = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
#direction(my_list,n,2)
sol(5,0,n,my_list)




print(answer)