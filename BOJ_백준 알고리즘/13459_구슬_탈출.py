import sys
sys.setrecursionlimit(100000)

def sol(depth, level, Rr, Rc, Br, Bc) :
    global ans, Or, Oc
    if depth == level :
        return
    else :
        for num in range(4) :
            rt, nRr, nRc, nBr, nBc, bt = bfs(tra_list, my_list, num, Rr, Rc, Br, Bc)
            if rt == True and bt == False :
                ans = min(ans, level)
                my_list[nRr][nRc] = '.'
                my_list[nBr][nBc] = '.'
                my_list[Rr][Rc] = 'R'
                my_list[Br][Bc] = 'B'
                my_list[Or][Oc] = 'O'
                print(1)
                exit()
                return
            elif rt == False and bt == False :
                sol(depth, level + 1 , nRr, nRc, nBr, nBc)
                my_list[nRr][nRc] = '.'
                my_list[nBr][nBc] = '.'
                my_list[Rr][Rc] = 'R'
                my_list[Br][Bc] = 'B'
                my_list[Or][Oc] = 'O'
            elif bt == True :
                my_list[nRr][nRc] = '.'
                my_list[nBr][nBc] = '.'
                my_list[Rr][Rc] = 'R'
                my_list[Br][Bc] = 'B'
                my_list[Or][Oc] = 'O'







def bfs(tra_list, my_list, d, Rr, Rc, Br, Bc) :
    global n,m, Or, Oc
    tra = tra_list[d]
    ar,ac, br,bc = Rr, Rc, Br, Bc
    flag = True
    r_flag = False
    b_flag = False
    while flag  :

        flag = False
        next_ar, next_ac, next_br, next_bc = ar + tra[0], ac + tra[1] , br + tra[0], bc + tra[1]
        if -1 < next_ar < n and -1 < next_ac < m :
            if next_ar == Or and next_ac == Oc :
                my_list[next_ar][next_ac] = 'R'
                my_list[ar][ac] = '.'
                flag = True
                ar, ac = next_ar, next_ac
                r_flag = True

            elif my_list[next_ar][next_ac] == '.'  :
                my_list[next_ar][next_ac] = 'R'
                my_list[ar][ac] = '.'
                flag = True
                ar, ac = next_ar, next_ac


        if -1 < next_br < n and -1 < next_bc < m:
            if next_br == Or and next_bc == Oc:
                my_list[next_br][next_bc] = 'B'
                my_list[br][bc] = '.'
                flag = True
                br, bc = next_br, next_bc
                b_flag = True

            elif my_list[next_br][next_bc] == '.':
                my_list[next_br][next_bc] = 'B'
                my_list[br][bc] = '.'
                flag = True
                br, bc = next_br, next_bc



    return r_flag, ar, ac, br, bc, b_flag


ans = 9876543210
tra_list = [[1,0],[0,1],[-1,0],[0,-1]]
n,m = map(int,sys.stdin.readline().split())
my_list = [[] for _ in range(n)]
for i in range(n) :
    temp = str(sys.stdin.readline().rstrip())
    for c in temp :
        my_list[i].append(c)
        if c == 'R' :
           Rr, Rc = i, len(my_list[i]) - 1
        elif c == 'B' :
           Br, Bc = i, len(my_list[i]) - 1
        elif c == 'O' :
            Or, Oc = i, len(my_list[i]) - 1



sol(11,1,Rr,Rc,Br,Bc)
if ans == 9876543210 :
    print(0)
else : print(ans)
