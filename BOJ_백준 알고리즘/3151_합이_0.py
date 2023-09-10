import sys
n = int(sys.stdin.readline().rstrip())
my_list = sorted(list(map(int,sys.stdin.readline().split())))

def sol(i,j,my_list) :
    global answer
    now_combi = my_list[i] + my_list[j]
    l = i + 1
    r = j - 1
    lower = -1
    upper = -1
    while l <= r:
        mid = (l + r) // 2
        if now_combi + my_list[mid] > 0:
            r = mid - 1
        elif now_combi + my_list[mid] == 0:
            if l == mid == lower :
                break
            r = mid
            lower = mid
        else:
            l = mid + 1

    l = i + 1
    r = j - 1

    while l <= r:
        mid = (l + r + 1) // 2
        if now_combi + my_list[mid] > 0:
            r = mid - 1
        elif now_combi + my_list[mid] == 0:
            if r == mid == upper:
                break
            l = mid
            upper = mid
        else:
            l = mid + 1

    return lower, upper

#예를 들어 -2 1, 이렇게 했을 때 -1이 5개가 있으면 어떻게 할 것인가?
#lower bound, upper bound 찾아서 빼야할 듯?
answer = 0
for i in range(len(my_list)-2) :
    for j in range(i+2, len(my_list)) :
        lower, upper = sol(i,j,my_list)

        if lower != -1 and upper != -1 :
            answer += (upper-lower+1)


print(answer)
