import sys

n,m = list(map(int,sys.stdin.readline().split()))

name_dict = {}
num_dict = {}

for x in range(1,n+1) :
    num = x
    name = str(sys.stdin.readline().rstrip())
    name_dict[num] = name
    num_dict[name] = num


for i in range(m) :
    answer = str(sys.stdin.readline().rstrip())
    if answer.isdigit() :
        print(name_dict[int(answer)])
    else :
        print(num_dict[answer])

