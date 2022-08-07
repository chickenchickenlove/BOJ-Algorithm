import sys

def channel(num_list,repeat_num,add_list):
        global answer
        global skew
        global ch
        if repeat_num == 1  :
            for i in range(len(num_list)):
                add_list.append(num_list[i])
                temp = int(''.join(map(str,add_list)))
                add_list.pop()
                temp_data = abs(int(temp) - ch)
                if temp_data < skew :
                    answer = int(temp)
                    skew = temp_data
        else :
            next_repeat = repeat_num-1
            for i in range(len(num_list)) :
                add_list.append(num_list[i])
                channel(num_list,next_repeat,add_list)
                add_list.pop()

skew = 1000000
answer = 1000000
ch = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())
my_list = []
if n > 0 :
    my_list = list(map(int,sys.stdin.readline().split()))
num_list = []
add_list = []
for i in range(0,10) :
    if i not in my_list :
        num_list.append(str(i))

if len(str(ch)) >= 2 :
    channel(num_list,len(str(ch))-1,add_list)
channel(num_list,len(str(ch)),add_list)
channel(num_list,len(str(ch))+1,add_list)

a = len(str(answer)) + abs(answer-ch)
b = abs(ch-100)
if a < b :
    print(a)
else :
    print(b)

