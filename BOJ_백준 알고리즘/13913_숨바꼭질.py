import sys
from collections import deque

def bfs(n,k) :
    que = deque()

    v = [sys.maxsize for _ in range(100000 + 1)]
    v[n] = 0
    que.append((n, 0 , ''))

    while que :
        #현재 위치, 현재 시간, 이동한 방법
        now_posi, time, path = que.popleft()


        # 순간이동할 경우
        if now_posi * 2 <= 100000 :
            if v[now_posi * 2] > time + 1 :
                que.append((now_posi * 2 , time + 1, path + '*'))
                v[now_posi * 2] = time + 1
                if now_posi * 2 == k :
                    return (time +1   , path + '*')

        # +1 할 경우
        if now_posi + 1 <= 100000 :
            if v[now_posi + 1] > time + 1 :
                que.append((now_posi + 1 , time + 1 , path + '+'))
                v[now_posi + 1 ] = time + 1
                if now_posi + 1 == k :
                    return (time+1 , path + '+')
        # -1 할 경우
        if now_posi - 1 >= 0 :
            if v[now_posi - 1 ] > time + 1 :
                que.append((now_posi - 1, time + 1, path + '-'))
                v[now_posi - 1] = time + 1
                if now_posi - 1 == k :
                    return (time+1 , path + '-')


def convert_paht(n, path) :
    answer = [n]
    temp = n
    for cal in path :
        if cal == '-' :
            temp = temp - 1

        elif cal == '+' :
            temp = temp + 1
        elif cal == '*' :
            temp = temp * 2

        answer.append(temp)
    return answer



n, k = map(int,sys.stdin.readline().split())

# 처음부터 같은 위치에 있을 때
if n == k :
    print(0)
    print(n)
# 처음에는 다른 위치에 있을 때
else :
    time, path = bfs(n, k)
    answer = convert_paht(n,path)


    #답 출력
    print(time)
    print(' '.join(map(str,answer)))




