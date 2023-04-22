import sys



# 입력 단


n,m = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
for i in range(n):
    temp = sys.stdin.readline().rstrip()
    for k in temp :
        my_list[i].append(k)

for k in my_list:
    print(k)