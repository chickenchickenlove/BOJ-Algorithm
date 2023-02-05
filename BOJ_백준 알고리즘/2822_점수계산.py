import sys

num_list = []
for p in range(8) :
    num_list.append(int(sys.stdin.readline().rstrip()))


answer_list = []
sum = 0

for k in range(5) :
    max_indx = num_list.index(max(num_list))
    answer_list.append(max_indx+1)
    sum += num_list[max_indx]
    num_list[max_indx] = -1

print(sum)
for p in sorted(answer_list) :
    print(p)