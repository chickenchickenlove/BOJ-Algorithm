import sys



def headf(head_li) :
    if len(head_li) > 1 :
        return(head_li[-1])
    else :
        print('error')

def judgeli(judge_li, check_str,bomb_last_str) :
    strlen = len(check_str)
    if len(judge_li) > 0 :
        if judge_li[-1] == bomb_last_str :
            if  (judge_li[-strlen : ]) == check_str :
                return True
            else :
                return False
        else :
            return False
    else :
        print('error')


my_str = str(sys.stdin.readline().rstrip())
bomb_str = list(str(sys.stdin.readline().rstrip()))
last_str = bomb_str[-1]

answer = []


for i in my_str :
    answer.append(i)
    if judgeli(answer,bomb_str, last_str) :
        for p in range(len(bomb_str)) :
            answer.pop()


if len(answer) == 0 :
    print('FRULA')
else :
    print(''.join(answer))







