import sys
from collections import deque

def bfs(m_posi,bro) :
    global visited_list
    if m_posi == bro :
        print(0)
    else :
        que = deque([[m_posi,0]])
        visited_list[m_posi] = 1
        while que :
            cur_num, cur_depth= que.popleft()
            next_depth = cur_depth + 1
            find_li = [[cur_num-1,next_depth],[cur_num+1,next_depth],[cur_num*2,next_depth]]
            for i in find_li :
                if i[0] == bro :
                    break
                else :
                    if i[0] > 0 and i[0] <= 100000 :
                        if visited_list[i[0]] == 0 :
                            visited_list[i[0]] = 1
                            que.append(i)
            if i[0] == bro :
                print(i[1])
                return

n,k = map(int,sys.stdin.readline().split()) #k = brother , n= me
visited_list = [0 for _ in range(100001)]
bfs(n,k)



