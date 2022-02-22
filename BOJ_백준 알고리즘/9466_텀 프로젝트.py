import sys

def init(my_list):
    for i in list(map(int,sys.stdin.readline().split())):
        my_list.append(i)
    return my_list

def solsol(start_point):
    global ans

    #DFS 용
    stack = [start_point]

    #경로 체크용
    d_stack = [start_point]

    while stack :
        now_point = stack.pop()
        next_point = my_list[now_point]

        # 한번도 방문한 적이 없는 경우, 계속 방문한다.
        if v[next_point] == 0  :
            v[next_point] = now_point
            stack.append(next_point)
            d_stack.append(next_point)

        # 한번이라도 방문한 적이 있는 경우
        else :
            # 이미 경로가 없다고 판별된 곳
            if v[next_point] == -1 :
                break

            # 사이클이 형성된 곳
            if v[next_point] != 9876543210:


                while d_stack:
                    point = d_stack.pop()
                    if v[point] != 9876543210 :
                        ans +=1
                        v[point] = 9876543210
                    if point == next_point:
                        break
    while d_stack :
        point = d_stack.pop()
        v[point] = -1





for _ in range(int(sys.stdin.readline().rstrip())):
    n = int(sys.stdin.readline().rstrip())
    my_list = [0]
    v = [0 for _ in range(n+1)]

    my_list = init(my_list)
    ans = 0

    for student in range(1, n+1):
        if my_list[student] == student :
            v[student] = 9876543210
            ans +=1

    for student in range(1, n+1):
        if v[student] == 0 :
            solsol(student)
    print(n - ans)




