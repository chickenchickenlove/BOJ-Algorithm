import sys

def add_snake(add_list, jud_var) :
    try :
        if jud_var == 0:
            var = add_list[-1][1] + 1
            add_list.append([add_list[-1][0],var])
            if check(add_list) == 'end' :
                return 'end'
        elif jud_var == 1: #아래로 내려갈 때
            var = add_list[-1][0] + 1
            add_list.append([var, add_list[-1][1]])
            if check(add_list) == 'end' :
                return 'end'
        elif jud_var == 2 : #왼쪽으로 갈 때
            var = add_list[-1][1] - 1
            add_list.append([add_list[-1][0], var])
            if check(add_list) == 'end' :
                return 'end'
        else :
            var = add_list[-1][0] - 1
            add_list.append([var, add_list[-1][1]])
            if check(add_list) == 'end' :
                return 'end'
        return
    except :
        return 'end'


def body_move(body_list) :
    if len(body_list) > 0 :
        for p in range(len(body_list)-1) :
            body_list[p] = body_list[p+1]
        return
    else :
        return 'end'


def check(check_list) :
    global n
    if check_list[-1][0] >= n or check_list[-1][1] >= n or check_list[-1][0] < 0 or check_list[-1][1] < 0 :
        return 'end'
    else :
        return 'go'

def check_body(check_body) :

    if check_body[-1] in check_body[:-2] :
        return 'end'
    else :
        return 'go'



n = int(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline().rstrip())


umap = [[0 for col in range(n)] for row in range(n)]

for apple in range(k) :
    x,y = list(map(int,sys.stdin.readline().split()))
    umap[x-1][y-1] = 1

first_position = (0,0)
snake = [[0,0]]
tail_idx = 0
turn_flag = ''
turn_cnt = 0
time = 0
com_list = []

for p in range(int(sys.stdin.readline().rstrip())) :
    com_list.append(list(map(str,sys.stdin.readline().split())))

com_list = com_list[::-1]

time=0
while True :
    time += 1
    if add_snake(snake,turn_cnt%4) == 'end':
        print(time)
        break
    if umap[snake[-1][0]][snake[-1][1]] == 1 :
        umap[snake[-1][0]][snake[-1][1]] = 0
    else :
        if check_body(snake) == 'end':
            print(time)
            break
        body_move(snake)
        snake.pop()

    if len(com_list) > 0 :
        if int(com_list[-1][0]) == time  :
            if com_list[-1][1] == 'D' :
                turn_cnt += 1
            else :
                turn_cnt -= 1
            com_list.pop()


