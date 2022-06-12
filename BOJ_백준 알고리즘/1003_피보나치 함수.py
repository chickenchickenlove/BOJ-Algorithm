import sys
test_case = int(sys.stdin.readline().rstrip())
dp_table_zero = [-1 for _ in range(100)]
dp_table_one =  [-1 for _ in range(100)]

dp_table_zero[0] = 1
dp_table_zero[1] = 0
dp_table_one[1] = 1
dp_table_one[0] = 0

for p in range(2,100) :
    dp_table_zero[p] = dp_table_zero[p-1] + dp_table_zero[p-2]
    dp_table_one[p] = dp_table_one[p - 1] + dp_table_one[p - 2]


for _ in range(test_case) :
    n = int(sys.stdin.readline().rstrip())
    answer_list = [str(dp_table_zero[n]), str(dp_table_one[n])]
    print(' '.join(answer_list))
