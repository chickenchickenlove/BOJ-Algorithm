import sys

# 강사 코드 보고 개선이 필요함.

answer_list = []
answer_set = set()
def sol1(my_list) :
    global n
    if len(my_list) == n :
        answer_list.append([k for k in my_list])
        return
    for i in dice :
        my_list.append(i)
        sol1(my_list)
        my_list.pop()


def sol2(my_list) :
    global n
    if len(my_list) == n :
        temp_list = [i for i in my_list]
        temp_list.sort()
        answer_set.add(''.join(map(str, temp_list)))
        return
    for i in dice :
        my_list.append(i)
        sol2(my_list)
        my_list.pop()

def sol3(my_list, V) :
    global n
    if len(my_list) == n :
        answer_list.append([k for k in my_list])
        return
    for i in dice :
        if V[i] == 0 :
            V[i] = 1
            my_list.append(i)
            sol3(my_list,V)
            my_list.pop()
            V[i] = 0


# sys.stdin = open("input.txt")
input = sys.stdin.readline
dice = [1,2,3,4,5,6]
n,m = map(int,input().split())


if m == 1 :
    sol1([])
elif m == 2 :
    sol2([])
    answer_list = [i for i in answer_set]
elif m == 3 :
    sol3([],[0 for _ in range(7)])


answer_list.sort()
for k in answer_list:
    print(*k)
