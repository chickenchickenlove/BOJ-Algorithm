import sys
input = sys.stdin.readline
t = int(input().rstrip())
stack = []
cnt = 0

for i in range(t) :
    a = input().rstrip()
    if a.split()[0] == 'push' :
        stack.append(a.split()[1])
    elif a.split()[0] == 'pop' :
        if len(stack) - cnt != 0 :
            print(stack[cnt])
            cnt +=1
        else :
            print(-1)
    elif a.split()[0] == 'size' :
        print(len(stack)-cnt)
    elif a.split()[0] == 'empty' :
        if len(stack)-cnt == 0 :
            print(1)
        else :
            print(0)
    elif a.split()[0] == 'front' :
        if len(stack)-cnt == 0 :
            print(-1)
        else :
            print(stack[cnt])

    elif a.split()[0] == 'back' :
        if len(stack)-cnt == 0 :
            print(-1)
        else :
            print(stack[len(stack)-1])


