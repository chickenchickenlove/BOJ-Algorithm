import sys
def check():

    temp = int(''.join(map(str,my_list)))
    start_num = 2
    if temp in [2,3,5,7] :
        return True
    n = temp ** 0.5
    while n +1  > start_num:
        if temp % start_num == 0 :
            return False
        start_num += 1
    return True

def sol(lv) :
    global n
    if lv == n :
        print(''.join(map(str,my_list)))
    else :
        for i in range(1,10) :
            my_list.append(str(i))
            if check() and my_list[0] != '1':
                sol(lv + 1)
            my_list.pop()

n = int(sys.stdin.readline().rstrip())


my_list = []
sol(0)