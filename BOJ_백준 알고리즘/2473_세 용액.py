import sys


def binary_search(ll,rr,my_list) :
    global answer
    global answer_data
    l = ll+1
    r = rr-1
    temp = my_list[ll] + my_list[rr]
    m = (l + r ) // 2
    while l < r :
        m = (l + r ) // 2

        if abs(temp + my_list[m]) < answer :
            answer_data = (my_list[ll],my_list[m],my_list[rr])
            answer = abs(temp + my_list[m])

        if abs(temp + my_list[m]) == 0:
            return
        else :
            if abs(temp + my_list[m+1]) > abs(temp + my_list[m-1]) :
                r = m
            else :
                l = m
            if (r + l)//2 == m :
                break

    if abs(temp + my_list[m]) < answer :
        answer = abs(temp + my_list[m])
        answer_data = [my_list[ll], my_list[m],my_list[rr]]
    return






n = int(sys.stdin.readline().rstrip())
my_list = list(map(int,sys.stdin.readline().split()))
my_list = sorted(my_list)


answer = 9876543210
answer_data = [0,0,0]

for i in range(0, n-2) :
    for j in range(i+2, n) :
        binary_search(i,j,my_list)

print(' '.join(map(str,answer_data)))

