import sys
n = str(sys.stdin.readline().rstrip())
num_list = [0 for _ in range(10)]
for i in n :
    num_list[int(i)] += 1

max_num = 0
for i in range(0,10) :
    if i != 6 and i != 9 :
        if num_list[i] > max_num :
            max_num = num_list[i]

if (num_list[6] + num_list[9])%2 == 0 :
    num_69 = (num_list[6] + num_list[9])//2
else :
    num_69 = (num_list[6] + num_list[9])//2 + 1

print(max(num_69,max_num))
