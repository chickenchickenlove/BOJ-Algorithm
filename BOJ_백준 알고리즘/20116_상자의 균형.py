import sys
n,m = map(int,sys.stdin.readline().split())
num_list = list(map(int,sys.stdin.readline().split()))

my_sum = num_list[-1]
my_cnt = 1

for i in range(len(num_list)-2 , -1 ,- 1) :
    if not (num_list[i] - m < my_sum/my_cnt < num_list[i] + m) :
        print('unstable')
        exit()
    my_sum = my_sum + num_list[i]
    my_cnt += 1

print('stable')