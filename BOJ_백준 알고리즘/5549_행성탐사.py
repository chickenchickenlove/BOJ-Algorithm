import sys

def find_prefix(my_list,n,m) :
    prefix_list = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            prefix_list[i][j] = prefix_list[i][j-1] + my_list[i-1][j-1]

    for i in range(1,n+1) :
        for j in range(1,m+1) :
            prefix_list[i][j] += prefix_list[i-1][j]

    return prefix_list

n,m = map(int,sys.stdin.readline().split())
k = int(sys.stdin.readline().rstrip())

jj = [[0 for _ in range(m)] for _ in range(n)]
ii = [[0 for _ in range(m)] for _ in range(n)]
oo = [[0 for _ in range(m)] for _ in range(n)]

my_map = [str(sys.stdin.readline().rstrip()) for _ in range(n)]
for q in range(n) :
    for w in range(m) :
        if my_map[q][w] == 'I' :
            ii[q][w] +=1
        elif my_map[q][w] == 'J' :
            jj[q][w] +=1
        else :
            oo[q][w] +=1


iii = find_prefix(ii,n,m)
jjj = find_prefix(jj,n,m)
ooo = find_prefix(oo,n,m)


for ___ in range(k) :
    qwer = list(map(int,sys.stdin.readline().split()))
    a,b,c,d = qwer
    j_num = jjj[c][d] - (jjj[c][b-1] + jjj[a-1][d]) + jjj[a-1][b-1]
    i_num = iii[c][d] - (iii[c][b-1] + iii[a-1][d]) + iii[a-1][b-1]
    o_num = ooo[c][d] - (ooo[c][b-1] + ooo[a-1][d]) + ooo[a-1][b-1]
    print(j_num, o_num, i_num)


