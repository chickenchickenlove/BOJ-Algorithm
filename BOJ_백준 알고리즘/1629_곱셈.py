import sys


a,b,c = list(map(int,sys.stdin.readline().split()))
my_num = a
answer = 1
cnt = 0
num_list = []
cnt_idx = 0
my_list = [10**i for i in range(11)]

while cnt < b :
    if cnt == 0 :
        answer = my_num%c
        num_list.append(answer)
        answer = answer * my_num%c
        cnt +=2
    else :
        answer = answer * my_num % c
        cnt +=1 * 10**cnt_idx
        if cnt in my_list :
            num_list.append(answer)
            cnt_idx += 1
            my_num = answer


answer_list = []
for p in str(b) :
    answer_list.append(int(p))

answer_list = answer_list[::-1]

last_answer = 1

for x in range(len(answer_list)) :
    for y in range(answer_list[x]) :
        last_answer *=  num_list[x]


print(last_answer%c)

