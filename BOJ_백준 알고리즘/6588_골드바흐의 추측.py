import sys
my_list = [0 for _ in range(1000001)]
my_list[0] = 1
my_list[1] = 1
for i in range(2,100001) :
    for k in range(i,1000001) :
        if i*k >= 1000001 :
            break
        my_list[i*k] = 1



while (1) :
    end_flag = 'F'
    n = int(sys.stdin.readline().rstrip())
    if n == 0 :
        break
    for k in range(n,-1,-1) :
        if k%2 == 1 and my_list[k] == 0 and my_list[n-k] == 0 and (n-k) % 2 == 1  :
            my_num = n - k
            end_flag = 'T'
            print(f"{n} = {my_num} + {k}")
               # print(n, '=', my_num, '+', a_list[i], sep=' ')
            break

    if end_flag == 'F' :
        print("Goldbach's conjecture is wrong.")
