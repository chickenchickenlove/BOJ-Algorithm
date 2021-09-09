import sys
from collections import deque

def bfs(my_list,s,e,n) :

    que = deque()
    que.append((my_list[s], s,f'{s + 1}'))
    v = [0 for _ in range(n)]
    v[s] = 1

    while que :
        now_value, now_node, path = que.popleft()

        if now_node == e :
            return path


        for next_node in range(len(my_list)) :
            if v[next_node] == 0 :

                cnt = 0
                next_value = my_list[next_node]
                for idx in range(len(next_value)) :
                    if now_value[idx] != next_value[idx] :
                        cnt +=1
                if cnt ==  1 :
                    que.append((my_list[next_node], next_node,path + f' {str(next_node + 1 )}'))
                    v[next_node] = 1

    return '-1'




n,m = map(int,sys.stdin.readline().split())
my_list = []
for _ in range(n) :
    my_list.append(str(sys.stdin.readline().rstrip()))


s,e = map(int,sys.stdin.readline().split())
a = bfs(my_list,s-1,e-1,n)
if a == '-1' :
    print(-1)
else :
    print(' '.join(map(str,a.split())))

