import sys

n = int(sys.stdin.readline().rstrip())

num_list = list(map(int,sys.stdin.readline().split()))
answer = sorted(set(num_list))

dict_num = { key : value for value, key in enumerate(answer)}


for k in num_list :
    print(dict_num[k], end = ' ')




