import sys
n = int(sys.stdin.readline().rstrip())
num_list = []
for i in range(n) :
    num_list.append(int(sys.stdin.readline().rstrip()))

num_list = sorted(num_list)
sum = 0
for p in range(len(num_list)) :
    sum += abs(num_list[p] -(p+1))

print(sum)