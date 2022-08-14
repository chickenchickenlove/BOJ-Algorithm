import sys
import heapq



def sol(str_r,str_c,v) :
    global f_r
    global f_c
    global r
    global c
    my_list = []
    v[str_r][str_c] = 0
    heapq.heappush(my_list,(v[str_r][str_c],str_r,str_c))
    while my_list :
        my_value, now_r, now_c = heapq.heappop(my_list)
        for k in tra_list :
            next_r = now_r + k[0]
            next_c = now_c + k[1]
            if -1 < next_r < r and -1 < next_c < c :

                if v[next_r][next_c] > my_value + d[next_r][next_c] :
                    v[next_r][next_c] = my_value + d[next_r][next_c]
                    heapq.heappush(my_list,(v[next_r][next_c], next_r,next_c))



r,c = map(int,sys.stdin.readline().split())
d = [[0 for _ in range(c)] for _ in range(r)]
v = [[1000000000 for _ in range(c)] for _ in range(r)]
tra_list = [[1,0],[0,1],[-1,0],[0,-1]]

for i in range(r) :
    temp = str(sys.stdin.readline().rstrip())
    for k in range(len(temp)) :
        if temp[k] == 'g' :
            d[i][k] = 10000000
            for z in tra_list :
                next_r = i + z[0]
                next_c = k + z[1]
                if -1 < next_r < r and -1 < next_c < c and d[next_r][next_c] == 0 :
                    d[next_r][next_c] = 1
        elif temp[k] == 'S' :
            s_r = i
            s_c = k
        elif temp[k] == 'F' :
            f_r = i
            f_c = k


d[f_r][f_c] = 0


sol(s_r,s_c,v)
aa = v[f_r][f_c]
gg = v[f_r][f_c]//10000000
gh = v[f_r][f_c] % 10000000

print(gg,gh)





