import sys

con_list = []
def makeFunc(my_list) :
    global n
    if len(my_list) == n :
        print("".join(map(str, my_list)))
        exit()
    else :
        for i in range(1,4) :
            if my_list and my_list[-1] == i: continue
            my_list.append(i)
            my_string = "".join(map(str, my_list))
            flag = 1
            for size in range(2, n + 1):
                flag = min(flag,check(my_string, size))
                if not flag : break
            if flag: makeFunc(my_list)
            my_list.pop()

def check(my_string, size) :
    for i in range(len(my_string)-size+1) :
        if my_string[i:i+size] == my_string[i+size:i+size*2] : return 0
    return 1

# sys.stdin = open("input.txt")
input = sys.stdin.readline
n = int(input().strip())
makeFunc([])








