import sys
from collections import defaultdict


#입력을 받는다
n = int(sys.stdin.readline().rstrip())
my_list = []
for _ in range(n) :
    my_list.append(list(map(int,sys.stdin.readline().split())))


my_list2 = sorted(my_list, key = lambda x : (x[1],x[0]))
s = [0 for _ in range(200000+1)]
last_ball = 0
last_value = -1
answer = 0
answer_list = []
stack = []
for ball, value in my_list2 :
    # 공색깔이 다를 때

    #다른 공이 들어왔을 때,
    if last_ball != ball :
        answer += s[last_ball]
        if len(stack) > 0 :
            if value > stack[-1][1] :
                while stack :
                    b,v = stack.pop()
                    s[b] +=v
                    answer +=v
        answer -= s[ball]


    #같은 공이 들어왔을 때,
    #stack에는



    elif last_ball == ball :
        if len(stack) > 0 :
            if value > stack[-1][1] :
                while stack :
                    b,v = stack.pop()
                    s[b] +=v
                    if b != ball :
                        answer +=v




    stack.append((ball,value))
    answer_list.append(answer)

    last_ball = ball
    last_value = value

d = defaultdict(int)
for idx, v in enumerate(my_list2) :
    ball, value = v
    d[f'{ball},{value}'] = answer_list[idx]


for a,b in my_list :
    print(d[f'{a},{b}'])
